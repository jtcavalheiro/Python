#   
#   Interact with YouTube API
#   https://developers.google.com/youtube/v3
#
#   Function ytchannel returns "channel" data
#
#   Function ytvideos returns 5 videos from "channel" with chosen "order" (date of publication or view count)
#   
#



import requests, json


def ytchannel(channel):

    params = {
        'part': 'topicDetails,id,snippet,contentDetails,statistics',
        'id': channel,
        'key': 'your google API key'
    }

    api_result = requests.get('https://youtube.googleapis.com/youtube/v3/channels', params)
    api_response = api_result.json()

    return api_response


def ytvideos(channel, order):
# Order options: date, viewCount

    params = {
        'part': 'snippet',
        'channelId': channel,
        'order' : order,
        'key': 'AIzaSyArRcAIHTRS6wUkpALur6n2K3FnXfAvZcI'
    }

    api_result = requests.get('https://www.googleapis.com/youtube/v3/search', params)
    api_response = api_result.json()

    return api_response

