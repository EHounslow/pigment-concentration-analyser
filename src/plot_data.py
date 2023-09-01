from matplotlib.pyplot import (close, legend, plot, savefig, title, xlabel,
                               ylabel)
from numpy import asarray
from pandas import DataFrame


def plot_raw_calibration_data(calibration_raw: DataFrame):
    """
    The plot_raw_calibration_data function plots the raw calibration data.

    Args:
        calibration_raw: DataFrame: Pass the dataframe containing the raw calibration data

    Returns:
        A plot of the raw data
    """
    wavelength_raw = asarray(calibration_raw.columns, float)
    plot(wavelength_raw, calibration_raw.loc[50.0], label="50.0 mg/L")
    plot(wavelength_raw, calibration_raw.loc[25.0], label="25.0 mg/L")
    plot(wavelength_raw, calibration_raw.loc[12.5], label="12.5 mg/L")
    plot(wavelength_raw, calibration_raw.loc[6.25], label="6.25 mg/L")
    plot(wavelength_raw, calibration_raw.loc[3.125], label="3.125 mg/L")
    plot(wavelength_raw, calibration_raw.loc[1.5625], label="1.5625 mg/L")
    plot(wavelength_raw, calibration_raw.loc[0.78125], label="0.78125 mg/L")
    plot(wavelength_raw, calibration_raw.loc[0.390625], label="0.390625 mg/L")
    plot(wavelength_raw, calibration_raw.loc["Blank"], label="Blank")

    legend()
    title("Raw Calibration Sample Data")
    xlabel("Wavelength (nm)")
    ylabel("Absorbance")
    savefig("results/Raw Data")
    close()


def plot_corrected_calibration_data(corrected_calibration_data: DataFrame):
    """
    The plot_corrected_calibration_data function plots the corrected calibration data.

    Args:
        corrected_calibration_data: DataFrame: Plot the corrected calibration data

    Returns:
        The plot of the corrected calibration data
    """
    wavelength = asarray(corrected_calibration_data.columns, float)
    plot(wavelength, corrected_calibration_data.loc[50.0], label="50.0 mg/L")
    plot(wavelength, corrected_calibration_data.loc[25.0], label="25.0 mg/L")
    plot(wavelength, corrected_calibration_data.loc[12.5], label="12.5 mg/L")
    plot(wavelength, corrected_calibration_data.loc[6.25], label="6.25 mg/L")
    plot(wavelength, corrected_calibration_data.loc[3.125], label="3.125 mg/L")
    plot(wavelength, corrected_calibration_data.loc[1.5625], label="1.5625 mg/L")
    plot(wavelength, corrected_calibration_data.loc[0.78125], label="0.78125 mg/L")
    plot(wavelength, corrected_calibration_data.loc[0.390625], label="0.390625 mg/L")

    legend()
    title("Blank-Adjusted Calibration Sample Data")
    xlabel("Wavelength (nm)")
    ylabel("Absorbance")
    savefig("results/Blank Adjusted Samples")
    close()


def plot_calibration_curve(concentration, absorbance, wavelength):
    """
    The plot_calibration_curve function takes in the concentration and absorbance data from a given wavelength,
    and plots it on a graph. It then saves the graph as an image file for the selected wavelength.

    Args:
        concentration: Plot the x-axis of the calibration curve
        absorbance: Plot the absorbance of a certain wavelength
        wavelength: Create a title and file name for the plot

    Returns:
        A plot of the calibration curve
    """
    plot(concentration, absorbance)
    title(f"Calibration Curve {wavelength} nm")
    xlabel("Concentration (mg/L)")
    ylabel("Absorbance")
    savefig(f"results/Calibration Curve {wavelength} nm")
    close()
