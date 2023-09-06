"""
A program that creates a summary of wine reviews from a csv file.
"""

import pandas as pd

df = pd.read_csv('./data/winemag-data-130k-v2.csv')
country_counts = df['country'].value_counts().reset_index()
country_counts.columns = ['country', 'count']
# print(country_counts)

points = df.groupby('country').points.mean()
final = pd.merge(country_counts, points, on='country')
# print(final)

final.to_csv('data/reviews-per-country.csv')

