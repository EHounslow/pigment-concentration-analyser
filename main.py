from sklearn.linear_model import LinearRegression

from src.average_sample_replicates import average_replicates
from src.blank_correction import (set_concentration_in_dataframe,
                                  subtract_blanks_from_sample)
from src.ingest_data import ingest_data
from src.plot_data import (plot_calibration_curve,
                           plot_corrected_calibration_data,
                           plot_raw_calibration_data)

calibration_data = ingest_data("data/calibration.csv")

averaged_calibration = average_replicates(calibration_data)

raw_calibration_samples = set_concentration_in_dataframe(averaged_calibration)
plot_raw_calibration_data(raw_calibration_samples)

corrected_calibration_data = subtract_blanks_from_sample(raw_calibration_samples)
plot_corrected_calibration_data(corrected_calibration_data)

corrected_calibration_data = corrected_calibration_data.drop(
    corrected_calibration_data.loc[:, "220":"300"].columns, axis=1
)
corrected_calibration_data["Maximum Absorbance Wavelength"] = corrected_calibration_data.idxmax(axis=1)
print(corrected_calibration_data["Maximum Absorbance Wavelength"])
optimal_wavelength = str(corrected_calibration_data.loc[50.0]["Maximum Absorbance Wavelength"])
concentration = corrected_calibration_data.index.values
absorbance = corrected_calibration_data[optimal_wavelength].values
plot_calibration_curve(concentration, absorbance, optimal_wavelength)

sample_data = ingest_data("data/sample.csv")
samples_averaged = average_replicates(sample_data)
samples_averaged = samples_averaged.drop(columns=["Dilution"]).set_index("Sample")
samples_minus_blanks = subtract_blanks_from_sample(samples_averaged)
sample_minus_blanks_values = samples_minus_blanks[optimal_wavelength].values

calibration_model = LinearRegression().fit(absorbance.reshape(-1, 1), concentration.reshape(-1, 1))
concentration_prediction = calibration_model.predict(sample_minus_blanks_values.reshape(-1, 1))

print(f"The concentration of the pigment sample is {concentration_prediction[0][0]} mg/L")
