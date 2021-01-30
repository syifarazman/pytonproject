import re
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import itertools
import numpy as np
import nltk
import pickle
import joblib

class sentiment_analysis_code():

    lem = WordNetLemmatizer()

    def cleaning(self, text):
        txt = str(text)
        txt = re.sub(r"http\S+", "", txt)
        if len(txt) == 0:
            return 'no text'
        else:
            txt = txt.split()
            index = 0
            for j in range(len(txt)):
                if txt[j][0] == '@':
                    index = j
            txt = np.delete(txt, index)
            if len(txt) == 0:
                return 'no text'
            else:
                words = txt[0]
                for k in range(len(txt)-1):
                    words+= " " + txt[k+1]
                txt = words
                txt = re.sub(r'[^\w]', ' ', txt)
                if len(txt) == 0:
                    return 'no text'
                else:
                    txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
                    txt = txt.replace("'", "")
                    txt = nltk.tokenize.word_tokenize(txt)
                    #data.content[i] = [w for w in data.content[i] if not w in stopset]
                    for j in range(len(txt)):
                        txt[j] = self.lem.lemmatize(txt[j], "v")
                    if len(txt) == 0:
                        return 'no text'
                    else:
                        return txt

    def get_tweet_sentiment(self, tweet):
        #cleaning of tweet
            model_NB=joblib.load('sentiment1401.pkl')
            tweet = ' '.join(self.cleaning(tweet))
            analysis = model_NB.predict([tweet])
            if analysis==0:
                return 'Negative'
            else:
                return 'Positive'