import configparser
import twitter
import pandas as pd
from model.TwitterClassification import TwitterClassification

# load .env config
config = configparser.ConfigParser()
config.read('.env')

# Initialized Twitter API
twitterApi = twitter.Api(consumer_key=config["twitter"]["twitter_api_key"],
                  consumer_secret=config["twitter"]["twitter_api_private_key"],
                  access_token_key=config["twitter"]["twitter_access_token"],
                  access_token_secret=config["twitter"]["twitter_access_token_secret"])

# load accounts from csv file
accounts = pd.read_csv(config['data']['accounts'])

# Creating an training model
model = TwitterClassification(twitterApi)
model.train(accounts)



