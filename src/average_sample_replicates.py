from pandas import DataFrame


def average_replicates(dataframe: DataFrame) -> DataFrame:
    """
    The average_replicates function takes a dataframe as input and returns the average of all replicates for each sample.
        The function first drops the Well column from the dataframe, then groups by Sample and Dilution, taking an average of the replicates
        for each sample. Finally, it resets the index to return a new dataframe.

    Args:
        dataframe: Specify the dataframe that will be used in the function
    Returns:
        A dataframe with the averages of the replicates for each sample and dilution
    """
    dataframe = dataframe.drop(columns=["Well"])
    return (dataframe.groupby(["Sample", "Dilution"]).mean()).reset_index()
