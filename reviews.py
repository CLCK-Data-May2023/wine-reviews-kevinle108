"""
A program that creates a summary of wine reviews from a csv file.
"""

import pandas as pd

df = pd.read_csv('./data/winemag-data-130k-v2.csv')
final = df.groupby('country').points.agg(['size', 'mean']).sort_values('size', ascending=False)
final['mean'] = final['mean'].round(1)
final = final.rename(columns={'size':'count', 'mean':'points'})
print(final)

final.to_csv('data/reviews-per-country.csv')

