## Pigment Concentration Analyser

### Introduction

This code uses a spectrophotometry calibration dataset for a known pigment to determine the relationship between absorbance readings and known pigment concentrations to build a model to calculate the concentration of unknown samples. 

### Model Assumptions

### Setup

`mkdir .venv`\
`pipenv install --dev`

### Running

`python main.py`

### Testing

`pytest .`

### Linting

`black . && isort .`
