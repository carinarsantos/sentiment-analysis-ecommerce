# src/preprocessor.py

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# Tenta carregar as stopwords. Em caso de falha, usa um conjunto vazio.
try:
    path_to_stopwords = r'C:\Users\55119\AppData\Roaming\nltk_data\corpora\stopwords\portuguese' # Adapte se o seu caminho for diferente
    with open(path_to_stopwords, 'r', encoding='utf-8') as f:
        stop_words = set(f.read().splitlines())
    print("Módulo Preprocessor: Stopwords carregadas com sucesso!")
except Exception:
    print("Módulo Preprocessor: Aviso - Stopwords não encontradas. Continuando sem elas.")
    stop_words = set()

def clean_text(text):
    """
    Função de limpeza final que usa RegexpTokenizer.
    """
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    clean_text = ' '.join(filtered_tokens)
    
    return clean_text