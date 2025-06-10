from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def analyze_sentiment(text):
    key = "<YOUR_LANGUAGE_API_KEY>"
    endpoint = "<YOUR_LANGUAGE_API_ENDPOINT>"
    
    # Configuração do cliente de análise de linguagem
    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    
    # Análise de sentimento
    response = client.analyze_sentiment([text])[0]
    
    return response.sentiment

def extract_key_phrases(text):
    key = "<YOUR_LANGUAGE_API_KEY>"
    endpoint = "<YOUR_LANGUAGE_API_ENDPOINT>"
    
    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    
    # Extração de frases-chave
    response = client.extract_key_phrases([text])[0]
    
    return response.key_phrases
