import configparser
import twitter

# load .env config
config = configparser.ConfigParser()
config.read('.env')

# load a tweet
api = twitter.Api(consumer_key=config["twitter"]["twitter_api_key"],
                  consumer_secret=config["twitter"]["twitter_api_private_key"],
                  access_token_key=config["twitter"]["twitter_access_token"],
                  access_token_secret=config["twitter"]["twitter_access_token_secret"])