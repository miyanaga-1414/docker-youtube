import json
import requests

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBIA8k4TYG7F6BFNJcutwtTfKZcWkJc96c"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def search_video(query):
    url = "https://www.googleapis.com/youtube/v3/search"

    #params = {'key' : DEVELOPER_KEY, 'part' : 'id,snippet', 'q' : query}
    params = {'key' : DEVELOPER_KEY, 'part' : 'id', 'q' : query}


    response = requests.get(url, params=params)

    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    json = response.json()
    status = response.status_code

    return {
                "status": status,
                "body": json
            }
