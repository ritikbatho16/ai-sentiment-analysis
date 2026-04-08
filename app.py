from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    text = request.form.get("text")
    if not text:
        return render_template("index.html", result="Error: No text provided", sentiment="Neutral")
    
    analysis = TextBlob(text)
    
    if analysis.sentiment.polarity > 0:
        sentiment = "Positive"
    elif analysis.sentiment.polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    result_text = f"Text: {text} | Sentiment: {sentiment} | Polarity: {analysis.sentiment.polarity:.2f}"
    return render_template("index.html", result=result_text, sentiment=sentiment)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)