#!/usr/bin/env python

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


taylor = pd.read_csv("taylor_all_songs.csv")

#median tempo for track number across all albums

new_data = taylor[["track_number", "tempo"]]
median_tempo = taylor.groupby(['track_number'])['tempo'].median().reset_index()
tracks = median_tempo['track_number']
tempo = median_tempo['tempo']

fig, ax = plt.subplots()

ax.plot(tracks,tempo, color = "black")
ax.set_xlabel("Track Number")
ax.set_ylabel("Median Tempo")
plt.tight_layout()
ax.set_title("Median Tempo of Songs through Track Numbers")
plt.savefig("tempo_tracknumber.png")
plt.close(fig)


#danceability over taylors version
fig, ax = plt.subplots(figsize = (15,15))
secondplt = taylor[["danceability", "album_name"]]
secondpltf = secondplt.iloc[16:60,:]
secondpltr = secondplt.iloc[78:129,:]
c = ['red', 'darkred', 'gold', 'goldenrod']
frames = [secondpltr, secondpltf]
combo = pd.concat(frames).reset_index()

sns.kdeplot(data = combo, x = 'danceability', hue = 'album_name', fill = True, palette = c)
ax.set_xlabel("Throughout the Album")
ax.set_ylabel("Danceability")
plt.tight_layout()
ax.set_title("How Danceability of the Album changed from Original to Taylor's Version")
plt.savefig("danceability_album.png")
plt.close(fig)



#energy over albums
fig, ax = plt.subplots(figsize = (15,20))
albums = taylor.iloc[0:235,:].reset_index()
colors = ['cornflowerblue', 'gold', 'goldenrod', 'rebeccapurple', 'red', 'darkred', 'mediumturquoise', 'dimgrey', 'palevioletred', 'rosybrown', 'saddlebrown', 'midnightblue']
# energyplt.boxplot(column = "energy", by = 'album_name', figsize = (15,15), notch = True)
sns.boxplot(y = albums['energy'], x = albums['album_name'], palette = colors) 

plt.xticks(rotation ='vertical')
plt.xlabel("Album")
plt.ylabel("Energy")
plt.title("Energy by Album")
plt.tight_layout()
plt.savefig("energy.png")
plt.close(fig)
