from ingest_data import ingest_data
from average_sample_calibration import average_replicates

calibration_data = ingest_data('data/calibration.csv')
calibration = average_replicates(calibration_data)
print(calibration)






