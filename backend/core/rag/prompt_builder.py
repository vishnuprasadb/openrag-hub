from typing import List, Dict


def build_prompt(
    query: str,
    documents: List[Dict],
) -> str:
    """
    Build a prompt using retrieved documents as context.
    """

    context_blocks = []

    for doc in documents:
        snippet = doc.get("metadata", {}).get("text", "")
        doc_id = doc.get("id", "unknown")

        context_blocks.append(
            f"[Source: {doc_id}]\n{snippet}"
        )

    context = "\n\n".join(context_blocks)

    prompt = f"""
You are an assistant answering questions using the provided context.

Context:
{context}

Question:
{query}

Instructions:
- Answer concisely
- Use only the provided context
- If the answer is not in the context, say "I don't know"
"""

    return prompt.strip()
