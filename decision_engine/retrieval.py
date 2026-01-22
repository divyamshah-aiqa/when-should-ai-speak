from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class RetrievalConfidence:
    def __init__(self, knowledge_base):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.knowledge_base = knowledge_base
        self.kb_embeddings = self.model.encode(knowledge_base)

    def estimate(self, query: str) -> float:
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.kb_embeddings)
        return float(similarities.max())
