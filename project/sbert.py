from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer(
    'sentence-transformers/distiluse-base-multilingual-cased-v2')

emb1 = model.encode("Энэ бол улаан малгайтай муур юм.")
emb2 = model.encode("Энэ бол миний улаан малгайтай нохой.")

cos_sim = util.cos_sim(emb1, emb2)
print("Cosine-Similarity:", cos_sim)
