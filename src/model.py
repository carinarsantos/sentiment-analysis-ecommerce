# src/model.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator

# Inicializa as ferramentas uma vez quando o módulo é importado
analyzer = SentimentIntensityAnalyzer()
translator = Translator()

def get_sentiment_scores(text_portuguese):
    """
    Traduz um texto para o inglês e retorna os scores de sentimento do VADER.
    """
    if not isinstance(text_portuguese, str) or not text_portuguese.strip():
        return {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
    try:
        text_english = translator.translate(text_portuguese, src='pt', dest='en').text
        sentiment_scores = analyzer.polarity_scores(text_english)
        return sentiment_scores
    except Exception as e:
        return {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

def classify_sentiment(compound_score):
    """
    Classifica o sentimento em 'Positivo', 'Neutro' ou 'Negativo'.
    """
    if compound_score >= 0.05:
        return 'Positivo'
    elif compound_score <= -0.05:
        return 'Negativo'
    else:
        return 'Neutro'