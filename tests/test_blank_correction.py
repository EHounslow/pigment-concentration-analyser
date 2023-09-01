from src.average_sample_replicates import average_replicates
from src.blank_correction import (set_concentration_in_dataframe,
                                  subtract_blanks_from_sample)
from src.ingest_data import ingest_data


def test_subtract_blanks_from_sample_success():
    csv = "data/calibration.csv"
    dataframe = ingest_data(csv)
    averaged_samples = average_replicates(dataframe)
    samples_with_index = set_concentration_in_dataframe(averaged_samples)
    corrected_samples_data = subtract_blanks_from_sample(samples_with_index)
    assert "Blank" not in corrected_samples_data.index
