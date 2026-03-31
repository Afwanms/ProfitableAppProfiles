from DataCleaning import load_csv, clean_app_store, clean_play_store

app_data, app_header = load_csv("data/RawData/AppleStore.csv")
play_data, play_header = load_csv("data/RawData/googleplaystore.csv")

app_cleaned = clean_app_store(app_data, app_header)
play_cleaned = clean_play_store(play_data, play_header)

genre_count = {}

def most_genre(data):
    most = {}
    for row in data:
        genre = row[1]
        most[genre] = most.get(genre, 0) + 1

    for genre in most:
        most[genre] /= len(data)
    return most

play_most_genre = most_genre(play_cleaned)
print(play_most_genre)