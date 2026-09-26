import pandas as pd
import spacy
import unicodedata

class NLPService:
    def __init__(self):
        try:
            self.nlp = spacy.load("pt_core_news_sm")
        except OSError:
            import os
            os.system("python -m spacy download pt_core_news_sm")
            self.nlp = spacy.load("pt_core_news_sm")
            
        self.df_keywords = pd.read_csv("data/palavras_chave.csv")

    def normalizar_texto(self, texto):
        texto = texto.lower()
        nfkd = unicodedata.normalize('NFKD', texto)
        sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
        return texto, sem_acento

    def classificar(self, texto_usuario):
        if not texto_usuario or not texto_usuario.strip():
            return "OUTROS", "nenhuma"

        texto_original_min, texto_normalizado = self.normalizar_texto(texto_usuario)
        doc = self.nlp(texto_original_min)
        
        for _, row in self.df_keywords.iterrows():
            palavra_chave = str(row['palavra_chave']).lower()
            _, kw_normalizada = self.normalizar_texto(palavra_chave)
            
            if palavra_chave in texto_original_min or kw_normalizada in texto_normalizado:
                return row['categoria'], palavra_chave

        return "OUTROS", "nenhuma"