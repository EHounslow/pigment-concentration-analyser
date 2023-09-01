from src.ingest_data import ingest_data


def test_ingest_data():
    csv = "data/calibration.csv"
    dataframe = ingest_data(csv)
    assert dataframe.columns[0] == "Well"
