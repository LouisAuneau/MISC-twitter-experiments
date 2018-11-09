from model.SupervisedModel import SupervisedModel
from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
import pandas

class TwitterClassification(SupervisedModel):

    def __init__(self, twitterApi):
        self.twitterApi = twitterApi

    def train(self, trainingData: pandas.DataFrame) -> None:
        # Generate TF-IDF Table which will act as classification features
        featureTable: pandas.DataFrame = pandas.DataFrame()
        featureTable['tweet_id'] = None
        twitterDescriptions = []

        for index, row in trainingData.iterrows():
            twitter_account = row["account"]

            # Getting each twitter account description
            twitterDescriptions.append(self.twitterApi.GetUser(screen_name=twitter_account).description)


        # TF-IDF on all description with normalization
        stopWords = get_stop_words('fr')
        vectorizer = TfidfVectorizer(stop_words=stopWords, strip_accents='unicode', norm='l2')
        table = vectorizer.fit_transform(twitterDescriptions)

        import ipdb; ipdb.set_trace()

    def run(self, entity):
        raise NotImplementedError()
