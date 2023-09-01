from pandas import DataFrame, concat


def subtract_blanks_from_sample(dataframe: DataFrame) -> DataFrame:
    """
    The subtract_blanks_from_sample function takes a dataframe of sample values and subtracts the blank value from each sample.
    The function returns a new dataframe with the adjusted values.

    Args:
        dataframe: DataFrame: Specify the dataframe that is being passed into the function

    Returns:
        A new dataframe with the blank values subtracted from each sample
    """
    adjusted: DataFrame = dataframe - dataframe.loc["Blank"].values.squeeze()
    return adjusted.drop(["Blank"])


def set_concentration_in_dataframe(dataframe: DataFrame) -> DataFrame:
    """
    The set_concentration_in_dataframe function takes a dataframe as input and returns a new dataframe with the
    concentration of each sample set in the index. The concentration is calculated by dividing 50 by the dilution factor.
    The blank samples are given an arbitrary concentration value of "Blank".

    Args:
        dataframe: DataFrame: Pass the dataframe into the function

    Returns:
        A dataframe with the concentration column set as the index
    """
    blank = dataframe.loc[dataframe["Sample"] == "Blank"]
    samples = dataframe.loc[dataframe["Sample"] != "Blank"]
    blank["Concentration"] = "Blank"
    samples["Concentration"] = 50 / samples["Dilution"]
    all_samples = concat([blank, samples])
    all_samples = all_samples.drop(columns=["Dilution", "Sample"]).set_index("Concentration")
    return all_samples
