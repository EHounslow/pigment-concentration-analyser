import numpy
import pandas
from ingest_data import ingest_data

calibration_data = ingest_data('data/calibration.csv')
print(calibration_data.head())

sample_data = ingest_data('data/sample.csv')
print(sample_data.head())


