import urllib.request
import json
from pprint import pprint

url = "https://raw.githubusercontent.com/DataGrazr/RedditPosts/main/data/latest/core_data.json"

print(f"Retrieving data from {url}")
with urllib.request.urlopen(url) as url_data:
    data = json.load(url_data)
    print(f"Got {len(data)} records back, printing the first 10...")
    pprint(data[0:10])
