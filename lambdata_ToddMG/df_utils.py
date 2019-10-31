"""
utility functions for working with DataFrames
"""

import pandas

class DFManager():
    """
    Helper class for dataframe functions/methods
    """

    def __init__(self, df):
        self.df = df

    def mergeRows(self, df1, df2):
        """
        A function to merge two data frames by rows
        :param df1: Dataframe to merge with
        :param df2: Dataframe to merge
        :return: Merged dataframe
        """
        df_new = pd.concat([df1, df2])
        return df_new

    def mergeCols(self, df1, df2):
        """
        A function to merge two data frames by columns
        :param df1: Dataframe to merge with
        :param df2: Dataframe to merge
        :return: Merged dataframe
        """
        df_new = pd.concat([df1, df2, axis=1])
        return df_new

    def newCol(self, df, name, list):
        """
        A function to create a new column for a dataframe
        :param df: Dataframe
        :param name: Name of column
        :param list: List or series to create column
        :return: New Dataframe
        """
        df[name] = list
        return df

