import csv

def load_csv(file_path):
    """Load CSV file"""
    with open(file_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data[1:], data[0]

def remove_duplicates(data, subset):
    """Remove duplicate rows based on a specific column (subset)"""
    unique_data = []
    seen = set()

    for row in data:
        key = row[subset]
        if key not in seen:
            seen.add(key)
            unique_data.append(row)

    return unique_data

def clean_app_store(data, subset):
    """clean data in app store dataset"""
    name = subset.index("track_name")
    price = subset.index("price")
    rating_count = subset.index("rating_count_tot")
    rating = subset.index("user_rating")
    genre = subset.index("prime_genre")
    language = subset.index("lang.num")

    data = remove_duplicates(data, name)
    cleaned_data = []

    for row in data:
        try:
            price = float(row[price])
            rating_count = int(row[rating_count])
            rating = float(row[rating])
            language = int(row[language])
        except Exception as e:
            print(f"Error: {e}")
            print(f"Row {row}")

        if price != 0:
            continue
        if language < 1:
            continue
            
        cleaned_data.append([
            row[name],
            row[genre],
            rating_count,
            rating
        ])
    return cleaned_data


def clean_play_store(data, subset):
    """clean data in play store dataset"""
    name = subset.index("App")
    price = subset.index("Price")
    installs = subset.index("Installs")
    rating = subset.index("Rating")
    category = subset.index("Category")

    data = remove_duplicates(data, name)
    cleaned_data = []

    for row in data:
        try:
            installs = int(row[installs].replace("+", "").replace(",", ""))
            price = float(row[price].replace("$", ""))
            installs = int(row[installs])
            rating = float(row[rating])
        except Exception as e:
            print(f"Error: {e}")
            print(f"Row {row}")

        if price != 0:
            continue
            
        cleaned_data.append([
            row[name],
            row[category],
            installs,
            rating
        ])
    return cleaned_data

if __name__ == "__main__":
    app_data, app_header = load_csv("data/RawData/AppleStore.csv")
    play_data, play_header = load_csv("data/RawData/GooglePlayStore.csv")

    app_cleaned = clean_app_store(app_data, app_header)
    play_cleaned = clean_play_store(play_data, play_header)

    print("App Store cleaned data sample:", app_cleaned[:5])
    print("Play Store cleaned data sample:", play_cleaned[:5])

    print("Total cleaned App Store entries:", len(app_cleaned))
    print("Total cleaned Play Store entries:", len(play_cleaned))