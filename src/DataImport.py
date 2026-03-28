import kagglehub


path_playstore = kagglehub.dataset_download("lava18/google-play-store-apps")
path_apple = kagglehub.dataset_download("ramamet4/app-store-apple-data-set-10k-apps")

print("Path to Google Play Store data:", path_playstore)
print("Path to Apple Store data:", path_apple)

