# I followed the examples in the text to figure out how to complete this 
# assignment

def make_album(artist_name, album_title, number_of_songs=None):
    '''Prints information about albums'''
    album_info = {'Name': artist_name.title(), 'Album': album_title.title()}

    if number_of_songs:
        album_info['Number of Songs'] = number_of_songs
    return album_info

# Calls the function 3 times with different artists and albums
album = make_album('thefatrat', 'unity')
print(album)

album = make_album('thefatrat', 'close to the sun')
print(album)

album = make_album('theamethystwarrior', 'journey', number_of_songs=11)
print(album)