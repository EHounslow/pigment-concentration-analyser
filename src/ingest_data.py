from pandas import DataFrame, read_csv


def ingest_data(input_file: str) -> DataFrame:
    """
    The ingest_data function reads in the data from a CSV file and returns it as a Pandas DataFrame.

    Args:
        input_file: str: Specify the file path of the input data
    Returns:
        A dataframe
    """
    return read_csv(input_file, header=10)
