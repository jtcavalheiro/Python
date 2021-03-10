#
#   Google API to find social media links
#   
#   Get your programmable search engine at:
#   https://programmablesearchengine.google.com/about/
#
#   Get your custom search API key at:
#   https://developers.google.com/custom-search/v1/introduction
#
#

import requests, json

def twitter_url(brand):

    query = brand + ' twitter'

    params = {
        'q': query,
        'num': '1',
        'cx': 'your programmable search engine',
        'key': 'your API key'
    }

    api_result = requests.get('https://customsearch.googleapis.com/customsearch/v1', params)
    api_response = api_result.json()
    result = api_response['items'][0]['formattedUrl']

    return result


def youtube_url(brand):

    query = brand + ' youtube channel'

    params = {
        'q': query,
        'num': '1',
        'cx': 'your programmable search engine',
        'key': 'your API key'
    }

    api_result = requests.get('https://customsearch.googleapis.com/customsearch/v1', params)
    api_response = api_result.json()
    result = api_response['items'][0]['pagemap']['hcard'][0]['url']

    return result