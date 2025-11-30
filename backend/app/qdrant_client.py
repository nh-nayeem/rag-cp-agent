from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from typing import List, Dict, Any, Optional
from .config import settings

class QdrantClientWrapper:
    def __init__(self):
        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
        self.collection_name = settings.QDRANT_COLLECTION_NAME
        self.vector_size = 3072
    
    def ensure_collection_exists(self):
        """Create vector collection if not exists."""
        try:
            collections = self.client.get_collections().collections
            exists = any(c.name == self.collection_name for c in collections)
            
            if not exists:
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(
                        size=self.vector_size,
                        distance=Distance.COSINE
                    )
                )
                print(f"Created collection: {self.collection_name}")
        except Exception as e:
            print(f"Error ensuring collection exists: {str(e)}")
    
    def search_embeddings(self, embedding: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        """Search for similar embeddings in Qdrant."""
        try:
            self.ensure_collection_exists()
            
            # Check if collection has any points
            collection_info = self.client.get_collection(self.collection_name)
            if collection_info.points_count == 0:
                return []
            
            search_result = self.client.search(
                collection_name=self.collection_name,
                query_vector=embedding,
                limit=limit,
                with_payload=True
            )
            
            # Convert to list of dicts with payload and score
            results = []
            for hit in search_result:
                results.append({
                    "payload": hit.payload,
                    "score": hit.score
                })
            
            return results
            
        except Exception as e:
            print(f"Error searching embeddings: {str(e)}")
            return []
    
    def upsert_vector(self, id: str, vector: List[float], payload: dict):
        """Upsert a vector with payload to Qdrant."""
        try:
            self.ensure_collection_exists()
            
            point = PointStruct(
                id=id,
                vector=vector,
                payload=payload
            )
            
            self.client.upsert(
                collection_name=self.collection_name,
                points=[point]
            )
            
        except Exception as e:
            raise Exception(f"Failed to upsert vector: {str(e)}")

qdrant_client = QdrantClientWrapper()