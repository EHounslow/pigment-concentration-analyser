## Pigment Concentration Analyser

### Introduction

This code uses a spectrophotometry calibration dataset for a known pigment to determine the relationship between absorbance readings and known pigment concentrations to build a model to calculate the concentration of unknown samples. 

Running the code ingests calibration and sample datasets, reformats the datasets to set the indexes with appropriate data labels, averages the replicates for each sample, and plots the absorbance values against wavelength for raw data and blank-corrected data. A model is constructed using the calibration data and the concentration of the unknown sample is shown in a printed statement (in the example case for sample X1: 44.08970187274605 mg/L). 

### Model Assumptions

Plotting the raw data shows that the solvent (and all non-adjusted samples) show high absorbance values in the range of 220-300 nm, which is assumed to be "noise". Some noise is still shown in this range in the blank adjusted samples. All values in the wavelength range 220-300 nm were therefore excluded from use in the model. 

The model assumes that the optimal wavelength to select for a model calibration curve is the wavelength which shows the maximum absorbance values across the known sample conentrations (printed to show that this is consistent across the concentration curve). This figure is selected from the highest concentration row (50.0 mg/L) and used in the subsequent model and calculation.

The model (Linear Regression) assumes that the relationship between the absorbance and sample concentration is linear (this was confirmed by plotting the calibration data for the selected wavelength), and that the sample concentration falls within the calibration range. 

### Setup

`mkdir .venv`\
`pipenv install --dev`

### Running

`python main.py`

### Testing

`pytest .`

### Linting

`black . -l 120 && isort .`
