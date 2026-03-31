import matplotlib.pyplot as plt
from EDA import most_common_genres, most_users_per_genre, sort_dict
from DataCleaning import load_csv, clean_app_store, clean_play_store

def plot_barh(data, title):
    """Plot a horizontal bar chart for the given data"""
    labels = [x[0] for x in data]
    values = [x[1] for x in data]

    plt.figure()
    plt.barh(labels, values)
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def compare_barh(data1, data2, label1, label2, title):
    labels = [x[0] for x in data1]

    dict1 = dict(data1)
    dict2 = dict(data2)

    values1 = [dict1.get(label, 0) for label in labels]
    values2 = [dict2.get(label, 0) for label in labels]

    y = list(range(len(labels)))
    height = 0.4

    plt.figure()

    plt.barh([i - height/2 for i in y], values1, height, label=label1)
    plt.barh([i + height/2 for i in y], values2, height, label=label2)

    plt.yticks(y, labels)
    plt.gca().invert_yaxis()
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    app_data, app_header = load_csv("data/RawData/AppleStore.csv")
    play_data, play_header = load_csv("data/RawData/googleplaystore.csv")

    app_cleaned = clean_app_store(app_data, app_header)
    play_cleaned = clean_play_store(play_data, play_header)

    play_genre_most = sort_dict(most_common_genres(play_cleaned))
    play_genre_avg = sort_dict(most_users_per_genre(play_cleaned))
    app_genre_most = sort_dict(most_common_genres(app_cleaned))
    app_genre_avg = sort_dict(most_users_per_genre(app_cleaned))

    #compare_barh(play_genre_most, play_genre_avg, "Supply", "Demand", "Google Play Store Supply vs Demand")
    #compare_barh(app_genre_most, app_genre_avg, "Supply", "Demand", "Apple Store Supply vs Demand")
    compare_barh(play_genre_most, app_genre_most, "Google Play Store", "Apple Store", "Supply Comparison")