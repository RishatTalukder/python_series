# ==========================
# GLOBAL VS LOCAL SCOPE
# ==========================

message = "I am a global variable"  # Global scope


def show_scope():
    local_message = "I am a local variable"  # Local scope

    print(local_message)


show_scope()

print(message)

# print(local_message)  # This would cause an error


# ==========================
# FUNCTION WITH RETURN VALUE
# ==========================

def power(number, exponent):
    return number ** exponent


result = power(4, 3)

print(result)


# ==========================
# RETURNING A DICTIONARY
# ==========================

def format_name(first_name, last_name):
    full_name = (
        f"{first_name.title()} {last_name.title()}"
    )

    return {
        "first": first_name.title(),
        "last": last_name.title(),
        "full": full_name
    }


formatted = format_name("rishat", "talukder")

print(formatted)


# ==========================
# CITY AND COUNTRY
# ==========================

def city_country(city, country):
    return f"{city.title()}, {country.title()}"


print(city_country("santiago", "chile"))
print(city_country("dhaka", "bangladesh"))
print(city_country("tokyo", "japan"))


# ==========================
# ALBUM FUNCTION
# ==========================

def make_album(artist, title):
    return {
        "artist": artist.title(),
        "title": title.title()
    }


album_1 = make_album("arijit singh", "best songs")
album_2 = make_album("linkin park", "meteora")
album_3 = make_album("adele", "25")

print(album_1)
print(album_2)
print(album_3)


# ==========================
# OPTIONAL PARAMETER
# ==========================

def make_album(artist, title, songs=None):
    album = {
        "artist": artist.title(),
        "title": title.title()
    }

    if songs is not None:
        album["songs"] = songs

    return album


album_with_songs = make_album(
    "linkin park",
    "meteora",
    13
)

print(album_with_songs)


# ==========================
# USER ALBUMS
# ==========================

while True:

    artist = input(
        "Enter artist name (q to quit): "
    )

    if artist == "q":
        break

    title = input(
        "Enter album title (q to quit): "
    )

    if title == "q":
        break

    album = make_album(artist, title)

    print(album)


# ==========================
# HOMEWORK
# ==========================

# 1. Write a function called city_country(city, country)
#    that returns a string like:
#    "Dhaka, Bangladesh"
#    Call it with at least three city-country pairs.

# 2. Write a function called make_album(artist, title)
#    that returns a dictionary containing:
#    - artist
#    - title
#    Create and print three albums.

# 3. Modify make_album() to accept an optional
#    number of songs parameter.
#    Add the songs information only if it is provided.

# 4. Write a function called student_info(name, age)
#    that returns a dictionary containing the
#    student's name and age.

# 5. Write a function called rectangle_area(length, width)
#    that returns the area instead of printing it.

# 6. Ask the user for two numbers and print the
#    result returned by a power() function.

# 7. Challenge:
#    Create a while loop that repeatedly asks the user
#    for a city and country, calls city_country(),
#    prints the result, and stops when the user enters
#    "q".