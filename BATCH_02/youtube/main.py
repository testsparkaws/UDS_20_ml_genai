from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pandas as pd

SCOPES = ["https://www.googleapis.com/auth/youtube"]

# OAuth Login
flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json",
    SCOPES
)

credentials = flow.run_local_server(port=0)

# Build YouTube client
youtube = build("youtube", "v3", credentials=credentials)

print("Authentication successful")

# Fetch subscriptions
subscriptions = []

request = youtube.subscriptions().list(
    part="snippet",
    mine=True,
    maxResults=50
)

while request:
    response = request.execute()

    for item in response["items"]:
        subscriptions.append({
            "title": item["snippet"]["title"],
            "subscription_id": item["id"],
            "channel_id": item["snippet"]["resourceId"]["channelId"]
        })

    request = youtube.subscriptions().list_next(request, response)

# Print results
print(f"\nTotal subscriptions: {len(subscriptions)}\n")

for sub in subscriptions:
    print(sub)

# Export CSV
df = pd.DataFrame(subscriptions)

df.to_csv("subscriptions.csv", index=False)

print("\nCSV exported successfully")