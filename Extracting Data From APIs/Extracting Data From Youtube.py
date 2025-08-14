from googleapiclient.discovery import build
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()

# Replace with your API key
API_KEY = os.getenv("YOUTUBE_DATA_API_KEY")
VIDEO_ID = "ueCc-AYUMRs"  # Example: "dQw4w9WgXcQ"

# Build YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_comments(video_id, max_comments=50):
    comments = []
    next_page_token = None

    while len(comments) < max_comments:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                "author": comment['authorDisplayName'],
                "text": comment['textDisplay'],
                "likes": comment['likeCount'],
                "published_at": comment['publishedAt']
            })

            if len(comments) >= max_comments:
                break

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return pd.DataFrame(comments)

# Collect comments
df = get_comments(VIDEO_ID, max_comments=50)

# Save to CSV for later sentiment analysis
df.to_csv("Youtube comments datasets/youtube_comments.csv", index=False)
print(f"Collected {len(df)} comments.")
print(df.head())
