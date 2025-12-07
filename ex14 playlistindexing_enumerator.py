"""
Scenario 5: Music App Displayable
A music app needs to display a list of songs with their rank/number.

Task:
Given list: songs = ["Song A", "Song B"]
Use enumerator(songs, 1) to print:
1. Song A
2. Song B
"""

songs = ["Song A", "Song B"]

for index, song in enumerate(songs,1):
    print(index, song)
    