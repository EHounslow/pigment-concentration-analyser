def average_replicates(dataframe):
    dataframe = dataframe.drop(columns=['Well'])
    averages =  dataframe.groupby(['Sample', 'Dilution']).mean()
    return averages

