"""
utility functions for working with DataFrames
"""

import pandas

class DFManager():
    """
    Helper class for dataframe functions/methods
    """

    def __intit__(self, DF):
        self.df = df

    def mergeRows(self, df1, df2):
        df_new = pd.concat([df1, df2])
        return df_new

    def mergeCols(self, df1, df2):
        df_new = pd.concat([df1, df2, axis=1])
        return df_new

    def newCol(self, df, name, list):
        df[name] = list
        return df

