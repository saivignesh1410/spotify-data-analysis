import pandas as pd

# Load dataset
df = pd.read_csv("spotify.csv")

# Show first rows
print(df.head())

#Understanding Data
print("\nshape:",df.shape)
print("\ncolumns:",df.columns)
print("\ninfo:")
print(df.info())

# Top 10 songs
top_songs = df.sort_values(by='track_popularity',ascending=False).head(10)
print("/nTop 10 songs:")
print(top_songs[['track_name', 'track_artist', 'track_popularity']])

# Top Artists
top_artists = df['track_artist'].value_counts().head(10)
print("\nTop Artists:")
print(top_artists)

# Popularity Trend
year_popularity = df.groupby('playlist_genre')['track_popularity'].mean()
print("\nPopularity by Genre:")
print(year_popularity)

#Correlation
print("\nCorrelation:")
print(df.corr(numeric_only=True))

import matplotlib.pyplot as plt
import seaborn as sns

#Top 10 Songs (Bar Chart)
top_songs = df.sort_values(by='track_popularity', ascending=False).head(10)
plt.figure()
plt.barh(top_songs['track_name'], top_songs['track_popularity'])
plt.xlabel("Popularity")
plt.title("Top 10 Most Popular Songs")
plt.gca().invert_yaxis()
plt.show()

#STEP 4: Top Artists (Bar Chart)
top_artists = df['track_artist'].value_counts().head(10)
plt.figure()
top_artists.plot(kind='bar')
plt.title("Top 10 Artists")
plt.xlabel("Artist")
plt.ylabel("Number of Songs")
plt.xticks(rotation=45)
plt.show()

# Genre Distribution (Pie Chart)
genre_count =df['playlist_genre'].value_counts()
plt.figure()
plt.pie(genre_count, labels= genre_count.index,autopct='%1.1f%%')
plt.title("Genre Distribution")
plt.show()

#Correlation Heatmap
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Feature Correlation")
plt.show()

#Energy vs Popularity (Scatter Plot)
plt.figure()
plt.scatter(df['energy'], df['track_popularity'])
plt.xlabel("Energy")
plt.ylabel("Popularity")
plt.title("Energy vs Popularity")
plt.show()
