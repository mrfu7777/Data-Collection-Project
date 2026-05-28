import os
import json
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Get the absolute path of the current script
basedir = os.path.abspath(os.path.dirname(__file__))
# Construct the full path to the .env file
dotenv_path = os.path.join(basedir, '.env')

# Load the .env file
load_dotenv(dotenv_path)

api_key = os.getenv('YOUTUBE_API_KEY')

# Debugging: Confirm if the key is loaded
if not api_key:
    print(f"Error: YOUTUBE_API_KEY not found in {dotenv_path}")
else:
    print("API Key loaded successfully.")

youtube = build('youtube', 'v3', developerKey=api_key)

query = 'Artificial Intelligence'
all_videos = []
next_page_token = None

# Paginated loop to collect data
while len(all_videos) < 100:
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=50,
        pageToken=next_page_token
    )
    response = request.execute()

    for item in response.get('items', []):
        all_videos.append({
            'post_id': item['id']['videoId'],
            'title': item['snippet']['title'],
            'text_content': item['snippet']['description'],
            'author': item['snippet']['channelTitle'],
            'timestamp': item['snippet']['publishedAt'],
            'platform': 'YouTube',
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            'search_keyword': query
        })

    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

# Save the raw data to a JSON file
with open('youtube_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_videos, f, indent=4, ensure_ascii=False)

print(f"Successfully collected {len(all_videos)} records. Saved to youtube_data.json.")