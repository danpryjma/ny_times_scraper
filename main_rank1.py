import rank1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dframe = pd.read_json('nytimes_best_business_books_2014-2019.json')

rank1 = rank1.Rank1Pivot(dframe)

print(type(rank1.pivot_values_rank1()))

fig, ax = plt.subplots(figsize=(20, 10))
ax = sns.heatmap(rank1.pivot_values_rank1(), annot=rank1.pivot, fmt='', cmap="YlGnBu", linewidths=.8,
                 annot_kws={"fontsize": 11})
plt.title('Heatmap of the #1 ranked book of each month from 2014 to 2019\n'
          'Data from NY Times Business book ranking')
plt.show()
