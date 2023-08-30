from pandas import concat
from numpy import asarray
from matplotlib.pyplot import close, legend, plot, savefig, title, xlabel, ylabel
from average_sample_replicates import average_replicates
from ingest_data import ingest_data

calibration_data = ingest_data("data/calibration.csv")
calibration = average_replicates(calibration_data)

blank = calibration.loc[calibration["Sample"] == "Blank"]
blank["Concentration"] = "Blank"
samples = calibration.loc[calibration["Sample"] != "Blank"]
samples["Concentration"] = 50 / samples["Dilution"]
full = concat([blank, samples])
full = full.drop(columns=["Dilution", "Sample"]).set_index("Concentration")

print(full)

adjusted = full - full.loc["Blank"].values.squeeze()
wavelength = asarray(adjusted.columns, float)

plot(wavelength, adjusted.loc[50.0], label="50.0")
plot(wavelength, adjusted.loc[25.0], label="25.0")
plot(wavelength, adjusted.loc[12.5], label="12.5")
plot(wavelength, adjusted.loc[6.25], label="6.25")
plot(wavelength, adjusted.loc[3.125], label="3.125 ")
plot(wavelength, adjusted.loc[1.5625], label="1.5625")
plot(wavelength, adjusted.loc[0.78125], label="0.78125")
plot(wavelength, adjusted.loc[0.390625], label="0.390625")

legend()
title("Blank Adjusted Sample Data")
xlabel("Wavelength")
ylabel("Absorbance")
savefig("results/Blank Adjusted Samples")
close()

wavelength_raw = asarray(full.columns, float)
plot(wavelength_raw, full.loc[50.0], label="50.0")
plot(wavelength_raw, full.loc[25.0], label="25.0")
plot(wavelength_raw, full.loc[12.5], label="12.5")
plot(wavelength_raw, full.loc[6.25], label="6.25")
plot(wavelength_raw, full.loc[3.125], label="3.125 ")
plot(wavelength_raw, full.loc[1.5625], label="1.5625")
plot(wavelength_raw, full.loc[0.78125], label="0.78125")
plot(wavelength_raw, full.loc[0.390625], label="0.390625")
plot(wavelength_raw, full.loc["Blank"], label="Blank")

legend()
title("Raw Sample Data")
xlabel("Wavelength")
ylabel("Absorbance")
savefig("results/Raw Data")
close()
