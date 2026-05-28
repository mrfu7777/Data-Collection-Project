# Reflection: Social Media API Data Collection

## Overview
This reflection document outlines the process, technical challenges, and ethical considerations encountered during the data collection of public content related to "Artificial Intelligence" from YouTube.

## Reflection Questions

**1. Which API did you use and why?**
I utilized the **YouTube Data API v3**. I chose this API because it is a stable, officially maintained interface provided by Google. Unlike many other social media platforms that require complex, time-consuming corporate approvals, the YouTube API is highly accessible for educational and academic purposes, making it an ideal choice for this assignment.

**2. What credentials or authentication steps were required?**
I obtained an API Key via the Google Cloud Console. This process involved creating a new project, enabling the YouTube Data API v3 service, and generating a secure developer credential. The Python script authenticates by passing this API Key within the request header to ensure authorized access.

**3. Which keyword, hashtag, or brand did you search for?**
I performed a search for the topic: "Artificial Intelligence".

**4. How many records did you collect?**
I successfully collected 100 records.

**5. What limitations did you face?**
The primary technical limitation was the API's pagination constraint; the `maxResults` parameter is capped at 50 per request. To overcome this and reach the 100-record threshold, I implemented a loop that utilized the `nextPageToken` provided in the API response to fetch subsequent data pages. Additionally, I had to manage daily API quota usage to ensure efficient operation.

**6. What ethical issues should be considered?**
Ethical data collection is paramount. I adhered to the platform's policies by collecting only publicly available metadata (titles and descriptions). I ensured that no private user information was harvested, and I have treated the content solely as public discourse, maintaining data privacy by avoiding the collection of any sensitive personal identifiers.

**7. Which text field would be most useful for future sentiment analysis?**
The `text_content` (description) field is the most useful for future sentiment analysis, as it provides detailed context regarding the content creator’s perspective, professional opinion, and arguments concerning the development of Artificial Intelligence.