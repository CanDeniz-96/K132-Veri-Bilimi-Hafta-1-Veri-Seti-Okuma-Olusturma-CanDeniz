"""
This file is used to create a dataset, look the general information of that and visualize it.
In order to start using, you should initialize in this way:
'df = DataOperations()'
You also have a chanse to add a csv, excel or json file as "DataSet = DataOperations(path_to_file)";
a Pandas data frame which already exists as 'DataSet = DataOperations(Pandas_Data_Frame)'
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt

class DataOperations():
    """The methods and the attributes below can be used in this class:
    DataSet.info : Return information of the dataset given.
    DataSet.visualize() : visualize 2 columns of the dataset as "x" and "y".
     """
    def __init__(self, DataSet=None):
        self.DataSet = self.__create_DataSet(DataSet)
        self.info = self.DataSet.describe()
    def __create_DataSet(self, DataSet):
        """This method creates a new random Pandas dataset if it does not exist.
        If a dataset is already provided, this method returns it.
        If a csv, excel or json file is provided, this method create a new Pandas dataset from this file.
        :param self: Initialised DataOperations object.
        :type self: DataOperations.DataOperations
        :param DataSet: a Pandas DataFrame, a file or empty
        :type: null, string, pandas.core.frame.DataFrame
        :returns pandas.core.frame.DataFrame"""
        #This function converts to pandas DataFrame object from a file, numpy darray or null value.
        #Check types according to conditions and convert them to pandas DataFrame object.
        ##Adding '__', this function cannot be reached out of the class.
        if isinstance(DataSet, pd.core.frame.DataFrame):
            return DataSet
        elif isinstance(DataSet, np.ndarray):
            df = pd.DataFrame(DataSet)
            return df
        elif not DataSet:
            x = np.random.randint(1, 1000, 100)
            y = np.random.randint(1, 1000, 100)
            df = pd.DataFrame(zip(x, y), columns=["x", "y"])
            return df
        elif DataSet.endswith(".xlsx") | DataSet.endswith("xls"):
            df = pd.read_excel(DataSet)
            return df
        elif DataSet.endswith(".json"):
            df = pd.read_json(DataSet)
            return df
        elif DataSet.endswith(".jsonl"):
            df = pd.read_json(DataSet, lines=True)
            return df
        elif DataSet.endswith(".csv"):
            df = pd.read_csv(DataSet)
            return df
        
    def __ask(self):
    #Ask to user which 2 columns will be displayed
    #Adding '__', this function cannot be reached out of the class.
        print(f"""Select 2 columns to visualize them
        These columns can be selected:
        {", ".join(self.DataSet.columns)}""")
        columns = input("Write two columns with space").split()
        return columns

    def visualize(self):
        """This function create scatter figure of 2 columns in the dateset.
        Usage:
        DataSet.visualize()
        Write 2 columns listed in order to be displayed"""
        columns=self.__ask()
        try:
            sns.scatterplot(x=columns[0], y=columns[1], data=self.DataSet)
            plt.pyplot.show()
        except ValueError:
            print(f"{' and '.join(columns)} do not exist")

