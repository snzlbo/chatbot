from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

sen_model = SentenceTransformer('sentence-transformers/msmarco-distilbert-multilingual-en-de-v2-tmp-lng-aligned')
embeddings = sen_model.encode(sentences)
print(embeddings)