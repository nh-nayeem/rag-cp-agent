from typing import Dict, Any, List
from .gemini_client import gemini_client
from .qdrant_client import qdrant_client
from .schemas import SourceInfo

def rag_answer(query: str) -> Dict[str, Any]:
    """
    Generate RAG answer for the given query.
    
    Args:
        query: User query string
        
    Returns:
        Dict with 'answer' and 'sources' keys
    """
    try:
        # Step 1: Embed user query
        query_embedding = gemini_client.embed_text(query)
        
        # Step 2: Search Qdrant for relevant documents
        search_results = qdrant_client.search_embeddings(
            embedding=query_embedding,
            limit=5
        )
        
        # Step 3: Build prompt based on search results
        if search_results:
            # We have relevant documents - include them in prompt
            context = "\n\n".join([
                f"Document {i+1} (Score: {result['score']:.3f}):\n{result['payload'].get('text', '')}"
                for i, result in enumerate(search_results)
            ])
            
            prompt = f"""You are a competitive programming expert. Use the following context to answer the user's question. If the context doesn't contain enough information, say so and provide your best general answer.

Context:
{context}

User Question: {query}

Provide a helpful, accurate answer:"""
        else:
            # No relevant documents found - fallback to normal LLM
            prompt = f"""You are a competitive programming expert. Answer the following question to the best of your ability.

User Question: {query}

Provide a helpful, accurate answer:"""
        
        # Step 4: Generate answer using Gemini
        answer = gemini_client.generate_text(prompt)
        
        # Step 5: Convert search results to SourceInfo objects
        sources = [
            SourceInfo(
                payload=result['payload'],
                score=result['score']
            )
            for result in search_results
        ]
        
        return {
            "answer": answer,
            "sources": sources
        }
        
    except Exception as e:
        # Fallback in case of any error
        try:
            fallback_prompt = f"""You are a competitive programming expert. Answer the following question.

User Question: {query}

Provide a helpful, accurate answer:"""
            answer = gemini_client.generate_text(fallback_prompt)
            return {
                "answer": answer,
                "sources": []
            }
        except Exception as fallback_error:
            return {
                "answer": f"Sorry, I encountered an error: {str(e)}",
                "sources": []
            }