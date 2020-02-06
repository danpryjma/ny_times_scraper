import by_year
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dframe = pd.read_json('nytimes_best_business_books_2014-2019.json')

all_years = by_year.AllYearsPivot(dframe, 2019)

fig, ax = plt.subplots(figsize=(20, 10))
ax1 = fig.add_axes([0.05, 0.08, 1.07, .8])
sns.heatmap(all_years.pivot_values_all_years(), annot=all_years.pivot, fmt='', cmap="YlGnBu", linewidths=.8,
            annot_kws={"fontsize": 11})
plt.title(f'NY Times bestsellers for {all_years.year}, heatmap for book mentions for the whole period 2014-2019')

plt.show()

fig, ax = plt.subplots(figsize=(20, 10))
ax1 = fig.add_axes([0.05, 0.08, 1.07, .8])
sns.heatmap(all_years.pivot_values_single_year(), annot=all_years.pivot, fmt='', cmap="YlGnBu", linewidths=.8,
            annot_kws={"fontsize": 11})
plt.title(f'NY Times bestsellers for {all_years.year}, heatmap for book mentions only in {all_years.year}')
plt.show()