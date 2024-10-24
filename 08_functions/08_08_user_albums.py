# I applied what I learned in the text to figure out how to complete this 
# assignment

def make_album(artist_name, album_title, number_of_songs=None):
    '''Prints information about albums'''
    album_info = {'Name': artist_name.title(), 'Album': album_title.title()}

    if number_of_songs:
        album_info['Number of Songs'] = number_of_songs
    return album_info

# A while loop that asks for information to input into the album_info dictionary
while True:
    print("\nPlease enter an artist and their album:")
    print("Enter 'q' to quit")

    artist = input("Artist Name: ")
    if artist == 'q':
        break

    album_name = input("Album Title: ")
    if album_name == 'q':
        break

    number = input("Number of Songs: ")
    if number == 'q':
        break

    album = make_album(artist, album_name, number)
    print(album)