import numpy as np


class AllYears:
    """
    This class takes the dataframe scraped from NY Times and processes it
    to create a dictionary and two independent dataframes for the SNS heatmap
    to be generated
    """

    def __init__(self, dframe, year):
        self.dframe = dframe
        self.year = year

    def _pivot(self):
        """
        Returns a pivot DataFrame with the listings of all #1
        ranked books pivoted by month/year
        """
        return self.dframe[self.dframe.Year == self.year].pivot(index='Ranking',
                                                                columns='Month',
                                                                values='Title')

    def _dict_values_all(self):
        """
        Creates a dictionary for the heatmap of all the books
        """
        top_books = self.dframe.Title.value_counts()
        dicio = {}
        # accounting for null values
        dicio[np.nan] = 0

        for ind, book in enumerate(top_books):
            dicio[top_books.index[ind]] = book

        return dicio

    def _dict_title_values_year(self):
        """
        Creates a dictionary for the heatmap of the #1 ranked books
        """
        top_books = self.dframe[(self.dframe.Year == self.year)].Title.value_counts()
        dicio = {}
        # accounting for null values
        dicio[np.nan] = 0

        for ind, book in enumerate(top_books):
            # input(ser1.index[ind])
            dicio[top_books.index[ind]] = book

        return dicio


class AllYearsPivot(AllYears):

    def __init__(self, dframe, year):
        super().__init__(dframe, year)
        self.pivot = super()._pivot()
        self.dicio_all_years = super()._dict_values_all()
        self.dicio_single_year = super()._dict_title_values_year()

    def pivot_values_single_year(self):
        """
        Takes the output of create_pivot_titles_all() and
        dict_title_values_all() to create a pivot dataframe
        with the heatmap info of #1 rank books
        """
        # deep copy of the titles dataframe to replace values
        pivot_values = self.pivot.copy()

        # creating the heatmap based on the dict of value_counts
        for rank in range(1, 11):
            for month in range(1, 13):
                pivot_values[month][rank] = self.dicio_single_year[self.pivot[month][rank]]

        pivot_values = pivot_values.astype('int32')

        return pivot_values

    def pivot_values_all_years(self):
        """
        Takes the output of create_pivot_titles_all() and
        dict_title_values_all() to create a pivot dataframe
        with the heatmap info of #1 rank books
        """
        # deep copy of the titles dataframe to replace values
        pivot_values = self.pivot.copy()

        # creating the heatmap based on the dict of value_counts
        for rank in range(1, 11):
            for month in range(1, 13):
                pivot_values[month][rank] = self.dicio_all_years[self.pivot[month][rank]]

        pivot_values = pivot_values.astype('int32')

        return pivot_values
