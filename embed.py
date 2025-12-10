import numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from src.utils.logger import get_logger
from src.utils.helpers import load_config
from src.utils.exceptions import RAGError

logger = get_logger(__name__)

class Embedder:
    def __init__(self):
        config = load_config()
        self.provider = config["llm"]["provider"]
        self.embedding_model = config["llm"]["embedding_model"]
        self.client = None

        if self.provider == "openai":
            self.client = OpenAI()
            logger.info(f"Using OpenAI embeddings: {self.embedding_model}")
        else:
            logger.info(f"Using local embeddings: {self.embedding_model}")
            self.model = SentenceTransformer(self.embedding_model)

    def embed(self, texts):
        """Embed a list of texts and return a matrix."""
        try:
            if self.provider == "openai":
                response = self.client.embeddings.create(
                    model=self.embedding_model,
                    input=texts
                )
                vectors = [d.embedding for d in response.data]
                return np.array(vectors)

            else:
                return self.model.encode(texts, convert_to_numpy=True)

        except Exception as e:
            raise RAGError(f"Embedding failed: {e}")
