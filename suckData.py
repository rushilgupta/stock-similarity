import twitter

api = twitter.Api(consumer_key='yVJ1IbE5zN2qoXyurztCatY5v', consumer_secret='DdnOwQCcmsD1KBWXsEWi8bmhk2FsBhoXtZTF22iYbDzfjuzkmb',
  access_token_key='113862838-urs2yuzG8qdqZ7pJqpxqptN0iVI0bEKXjsXXW37r',access_token_secret='iX17wJcs4fkjpjRQd9duYdMQLIPxyESpAOBVl6a08XSbo')

#GetSearch(self, term=None, geocode=None, since_id=None, max_id=None, until=None, since=None, count=15, lang=None, locale=None, result_type="mixed", include_entities=None):
dataset = api.GetSearch("aapl", count=10)
for data in dataset:
    print data.text