import numpy as np


class Rank1:
    """
    This class takes the dataframe scraped from NY Times and processes it
    to create a dictionary and two independent dataframes for the SNS heatmap
    to be generated
    """

    def __init__(self, dframe):
        self.dframe = dframe

    def _pivot(self):
        """
        Returns a pivot DataFrame with the listings of all #1
        ranked books pivoted by month/year
        """
        return self.dframe[self.dframe['Ranking'] == 1].pivot(index='Month',
                                                              columns='Year',
                                                              values='Title')

    def _dict_values_rank1(self):
        """
        Creates a dictionary for the heatmap of the #1 ranked books
        """
        ser1 = self.dframe[(self.dframe['Ranking'] == 1)]['Title'].value_counts()
        dicio = {}
        # accounting for null values
        dicio[np.nan] = 0

        for ind, book in enumerate(ser1):
            # input(ser1.index[ind])
            dicio[ser1.index[ind]] = book

        return dicio


class Rank1Pivot(Rank1):

    def __init__(self, dframe):
        super().__init__(dframe)
        self.pivot = super()._pivot()
        self.dicio = super()._dict_values_rank1()

    def pivot_values_rank1(self):
        """
        Takes the output of create_pivot_titles_rank1() and
        dict_title_values_rank1() to create a pivot dataframe
        with the heatmap info of #1 rank books
        """

        pivot_values = self.pivot.copy()

        for year in range(2014, 2020):
            for month in range(1, 13):
                pivot_values[year][month] = self.dicio[self.pivot[year][month]]

        pivot_values = pivot_values.astype('int32')

        return pivot_values
