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

def genre_user_avg(data):
    genre_user = {}
    for row in data:
        genre = row[1]
        users = row[2]
        if genre not in genre_user:
            genre_user[genre] = [0, 0]
        
        genre_user[genre][0] += users
        genre_user[genre][1] += 1

        genre_avg = {}

    for genre in genre_user:
        total, count = genre_user[genre]
        genre_avg[genre] = total / count

    return genre_avg

def sort_dict(data):
    return sorted(data.items(), key=lambda x: x[1], reverse=True)

