import os
import json
from dotenv import load_dotenv
from googleapiclient.discovery import build

# 获取当前脚本所在的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
# 拼接出 .env 的完整路径
dotenv_path = os.path.join(basedir, '.env')

# 加载该路径下的 .env
load_dotenv(dotenv_path)

api_key = os.getenv('YOUTUBE_API_KEY')

# 调试：确认是否读到
if not api_key:
    print(f"错误：未在 {dotenv_path} 中找到 YOUTUBE_API_KEY")
else:
    print("API Key 已成功加载")
youtube = build('youtube', 'v3', developerKey=api_key)

query = 'Artificial Intelligence'
all_videos = []
next_page_token = None

# 分页循环获取数据
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

# 保存数据
with open('youtube_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_videos, f, indent=4, ensure_ascii=False)

print(f"成功收集了 {len(all_videos)} 条记录，已保存至 youtube_data.json")