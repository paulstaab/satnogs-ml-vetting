import datetime
import satnogs_api_client
import os

obs_good = satnogs_api_client.fetch_observation_data_from_id(41789, datetime.datetime(2000, 1, 1, 0, 0), datetime.datetime.now(), 'good')

for o in obs_good:
    if o["waterfall"]:
        os.system('cd ../data/good; wget ' + o["waterfall"])



obs_bad = satnogs_api_client.fetch_observation_data_from_id(41789, datetime.datetime(2000, 1, 1, 0, 0), datetime.datetime.now(), 'bad')

for o in obs_bad:
    if o["waterfall"]:
        os.system('cd ../data/bad; wget ' + o["waterfall"])
