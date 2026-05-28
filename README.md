# Social Media API Data Collection: Artificial Intelligence

## Overview
This project focuses on the systematic collection of public social media data related to the topic of **Artificial Intelligence**. The objective is to gather raw data suitable for future sentiment analysis, ensuring adherence to data collection best practices using official platform APIs.

## Technical Specifications
* **Platform:** YouTube
* **API:** YouTube Data API v3 (Official Google API)
* **Search Query:** "Artificial Intelligence"
* **Date Range:** Recent public data
* **Number of Records Collected:** 100 records

## Dataset Fields
The dataset is stored in `youtube_data.json` and includes the following fields:
* `post_id`: Unique identifier for the video.
* `title`: The title of the YouTube video.
* `text_content`: The description of the video.
* `author`: The name of the channel.
* `timestamp`: The date and time of publication.
* `platform`: The source platform (YouTube).
* `url`: Direct link to the video.
* `search_keyword`: The term used for discovery.

## Ethics and Compliance
This data collection process adheres to the YouTube Responsible Builder Policy. Only publicly available metadata was collected, and no private user information was harvested.

## Usage
1. Ensure you have the `google-api-python-client` library installed:
   `pip install google-api-python-client`
2. Replace the `api_key` in the `data_collection.py` script with your valid Google API key.
3. Run the script:
   `python data_collection.py`