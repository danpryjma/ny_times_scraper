# ny_times_scraper
A simple web scraper with some heat map analysis done with seaborn.

First I used BeautifulSoup and some loops to go through the whole period of 2014-2019. 
Then I created a dataframe and a json file of the output.

From there it was just create the tables in the form of DataFrames to plot the heatmaps in Seaborn.

I hope you find this entertaining and if you have code comments, I would be glad to improve!

First you need to create the database with nytimes_scraper.py.

To execute the heatmaps you have to run main_rank1.py for the #1 analysis of the whole period.
In addition there is a file called main_all_years.py where you can analyze year by year.
