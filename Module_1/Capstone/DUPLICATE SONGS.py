songs = ['Bohemian Rhapsody', 'Stairway to Heaven', 'Bohemian Rhapsody', 'Hotel California', 'November Rain', 'Stairway to Heaven', 'Sweet Child O\' Mine']

# Write your code here
new_list={album for album in songs for char in str(album) if album[0]!="S" or  album[-1]!= "n"  }
print(new_list)
