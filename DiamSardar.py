import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('.C:\\climate change\\WBDATA.csv')


def file(df):
    """
    Function to read data and return data (countries as columns and years as
    columns)
    """
    Years_df = df
    # T is a function for Transpose
    Countries_df = Years_df.set_index('Country Name').T

    return Years_df, Countries_df


print(file(df))


def Heatmap(df):
    '''
    Function to analyse heatmap of co2 emission
    '''
    # extract data of interest
    df = df[["Country Name", "Indicator Code", "2015"]]
# extract countries of interest
    df = df[((df['Indicator Code'] == "EN.ATM.CO2E.SF.KT") |
            (df['Indicator Code'] == "EN.ATM.CO2E.LF.KT") |
            (df['Indicator Code'] == "EN.ATM.CO2E.GF.KT") |
            (df['Indicator Code'] == "EN.ATM.CO2E.KT")) &
            ((df["Country Name"] == "United States")
            | (df["Country Name"] == "Brazil")
            | (df["Country Name"] == "Russian Federation")
            | (df["Country Name"] == "India")
            | (df["Country Name"] == "China")
            | (df["Country Name"] == "South Africa"))]

    x = df.pivot("Country Name", "Indicator Code", ["2015"])

    ax = plt.axes()
    sns.heatmap(x.corr(), annot=True,  cmap=sns.cubehelix_palette
                (as_cmap=True),
                ax=ax)
    ax.set_title('Heatmap of C02 Emission of Countries')
    plt.show()


df = pd.read_csv('C:\\climate change\\data.csv')
Heatmap(df)


def pieplot(data, labels, title=""):
    """
    Produces a piechart of data.
    data: list of data values
    labels: list of labels of same length
    title: string for the title, defaulted to ""
    No plt.show() is given at the end to allow plotting to continue

    You were not required to make your functions flexible, but it is a
    good attitude and allows to recycle function for other data. Scoping
    (drawing the data from the calling unit) is the least flexible way.
    The variable name must be an exact match. A new function is required
    for a variable with a different name.
    """

    plt.pie(data, labels=labels)
    plt.title(title)

    return


def PowerCons(df2):
    '''
    Compare Electric power consumption of different countries
    '''
    # extract columns of interest
    df_1990 = df2[["Country Name", "1990"]]
# extract countries of interest
    df_1990 = df_1990[(df_1990["Country Name"] == "Cyprus")
                      | (df_1990["Country Name"] == "Brazil")
                      | (df_1990["Country Name"] == "Germany")
                      | (df_1990["Country Name"] == "India")
                      | (df_1990["Country Name"] == "China")]
# convert GDP column to numeric (non-numeric type before because NaN)
# not that the column name is still a string
    df_1990["1990"] = pd.to_numeric(df_1990["1990"])
# print(df_1990)

    pieplot(df_1990["1990"], labels=df_1990["Country Name"],
            title="Electric Power Consumption 1990")
    plt.savefig("Electric Power Consumption.png")
    plt.show()

    # extract columns of interest
    df_2014 = df2[["Country Name", "2014"]]
    df_2014 = df_2014[(df_2014["Country Name"] == "Cyprus")
                      | (df_2014["Country Name"] == "Brazil")
                      | (df_2014["Country Name"] == "Germany")
                      | (df_2014["Country Name"] == "India")
                      | (df_2014["Country Name"] == "China")
                      ]
# convert GDP column to numeric (non-numeric type before because NaN)
# not that the column name is still a string
    df_2014["2014"] = pd.to_numeric(df_2014["2014"])
# print(df_2020)

# call this time only with positional arguments
    pieplot(df_2014["2014"], df_2014["Country Name"],
            title="Electric Power Consumption 2014")
    plt.savefig("Electric Power Consumption.png")
    plt.show()


df2 = pd.read_csv('C:\\climate change\\EnergyPC.csv')
PowerCons(df2)


def GreenHousegas():
    '''
    Compare greenhouse emission of different countries
    '''
# Calling function
    file(df)

# Clean up Dataset for relavant information
# Extract 2014, 2015 and 2016  data of Countries
    MyCountries = df[["Country Name", "Indicator Code", "2014", "2015",
                      "2016"]]

    MyCountries = MyCountries[(MyCountries['Indicator Code'] ==
                              'EN.ATM.GHGT.KT.CE') &
                              ((MyCountries['Country Name'] == 'China') |
                              (MyCountries['Country Name'] == 'United States')
                              | (MyCountries['Country Name'] == 'Germany')
                              | (MyCountries['Country Name'] == 'Japan'))]

    MyCountries.plot(title='GreenHouse Emissions of Countries',
                     x="Country Name", kind="barh")
    plt.show()


GreenHousegas()


def lineplot(df, x, columns, xlabel, ylabel, file):
    """
    Produces a line plot from a dataframe. x-limits are adjusted to remove
    empty spaces at the edges.
    df: name of the dataframe
    x: 1D array or dataseries with the x-values
    columns: names of the columns in df to be plotted. Also used for the
            legend.
    xlabel, ylabels: labels for x and y axis.
    file: file name to store the plot as png file
    """

    plt.figure()

    # loop over the columns
    for c in columns:
        plt.plot(x, df[c], label=c)

    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # set x-limits
    plt.xlim(min(x), max(x))

    plt.savefig(file)
    plt.show()


def Exports(df3):
    '''
    Function to comapre different countries on the basis of Expenses
    of countries
    '''
    df = df3.transpose()
    # clean up to be done: make the first row of the table the column headers
    df.columns = df.iloc[0]

# print(df_cap)

# clean up to be done: make the first row of the table the column headers
    df.columns = df.iloc[0]

# Now remove the first 4 lines not containing data. I simple way is to
# extract all lines staarting with 4 (python count)
    df = df.iloc[4:]

    df.index = pd.to_numeric(df.index)

# index and the columns of interest
    df.index = pd.to_numeric(df.index)
    df["Afghanistan"] = pd.to_numeric(df["Afghanistan"])
    df["India"] = pd.to_numeric(df["India"])
    df["Bangladesh"] = pd.to_numeric(df["Bangladesh"])
    df["Benin"] = pd.to_numeric(df["Benin"])
    df["South Africa"] = pd.to_numeric(df["South Africa"])


# call the line plot function
    lineplot(df, df.index, ["Brazil", "China", "India", "South Africa",
                            "United States"], "year", "Exports of googs and"
             "services of Countries", "Exports.png")


df3 = pd.read_csv('C:\\climate change\\Exports.csv')
Exports(df3)


def Imports(df4):
    '''
    Function to comapre different countries on the basis of Expenses
    of countries
    '''
    df = df4.transpose()
    # clean up to be done: make the first row of the table the column headers
    df.columns = df.iloc[0]

# print(df_cap)

# clean up to be done: make the first row of the table the column headers
    df.columns = df.iloc[0]

# Now remove the first 4 lines not containing data. I simple way is to
# extract all lines staarting with 4 (python count)
    df = df.iloc[4:]

    df.index = pd.to_numeric(df.index)

# index and the columns of interest
    df.index = pd.to_numeric(df.index)
    df["Afghanistan"] = pd.to_numeric(df["Afghanistan"])
    df["India"] = pd.to_numeric(df["India"])
    df["Bangladesh"] = pd.to_numeric(df["Bangladesh"])
    df["Benin"] = pd.to_numeric(df["Benin"])
    df["South Africa"] = pd.to_numeric(df["South Africa"])


# call the line plot function
    lineplot(df, df.index, ["Brazil", "China", "India", "South Africa",
                            "United States"], "year", "Imports of goods and"
             " services of "
             "Countries", "Imports.png")


df4 = pd.read_csv('C:\\climate change\\Imports.csv')
Imports(df4)
