#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json
import requests

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCUl1iOsWP78X8dBLGmuTa0fRQMK_c4Vgc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  url = "https://www.googleapis.com/youtube/v3/activities"

  params = {'key' : DEVELOPER_KEY, 'channelId': 'UC3pS3Hzis3Ovydmy7ip5SWQ','part' : 'id,snippet'}
  

  response = requests.get(url, params=params, headers={"Authorization": DEVELOPER_KEY})

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  json = response.json()
  print(json) 



  # for search_result in search_response.get("items", []):
  #   print(json.dumps(search_result))
  #   if search_result["id"]["kind"] == "youtube#video":
  #     videos.append("%s (%s)" % (search_result["snippet"]["title"],
  #                                search_result["id"]["videoId"]))
  #   elif search_result["id"]["kind"] == "youtube#channel":
  #     channels.append("%s (%s)" % (search_result["snippet"]["title"],
  #                                  search_result["id"]["channelId"]))
  #   elif search_result["id"]["kind"] == "youtube#playlist":
  #     playlists.append("%s (%s)" % (search_result["snippet"]["title"],
  #                                   search_result["id"]["playlistId"]))


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except HttpError as e:
    print (e.resp.status, e.content)
