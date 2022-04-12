from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
 
analyzer = SentimentIntensityAnalyzer()
 
 
application = Flask(__name__)
 
def get_sentiment(my_text):
    vs = analyzer.polarity_scores(my_text)
 
    sentiment = ''
    if vs['compound'] >= 0.05:
        sentiment = 'Positive'
    elif vs['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
 
    return(sentiment)
 
 
 
@application.route("/endpoint", methods=['GET','POST'])
def sentiment_endpoint():
    if request.method == 'POST':
        json_dict = request.get_json()
        if 'my_text' in json_dict:
            result = get_sentiment(json_dict['my_text'])
            return jsonify({'output' : result})
        else:
            return jsonify({
                "status": "failed",
                "message": "parameter 'my_text' is required!"
            })
 
    if request.method == 'GET':
    
        my_text = request.args.get('my_text')
        result = get_sentiment(my_text)
        return jsonify({'output' : result})
 
 
 
 
 
if __name__=='__main__':
    application.run()
