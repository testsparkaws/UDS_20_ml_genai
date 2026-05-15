from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pandas as pd
import time

SCOPES = ["https://www.googleapis.com/auth/youtube"]

# Authenticate
flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json",
    SCOPES
)

credentials = flow.run_local_server(port=0)

youtube = build("youtube", "v3", credentials=credentials)

print("Authentication successful\n")

# Read CSV
df = pd.read_csv("subscriptions.csv")

print(f"Total subscriptions found: {len(df)}\n")

# Delete subscriptions
for index, row in df.iterrows():

    channel_name = row["title"]
    subscription_id = row["subscription_id"]

    try:
        youtube.subscriptions().delete(
            id=subscription_id
        ).execute()

        print(f"Unsubscribed: {channel_name}")

        # small delay to avoid API throttling
        time.sleep(1)

    except Exception as e:
        print(f"Failed: {channel_name}")
        print(e)

print("\nCompleted")