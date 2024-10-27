import argparse
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from .get_embedding_function import get_embedding_function
from .constants import MODELNAME, CHROMA_PATH
from .prompt_templates import create_template

PROMPT_TEMPLATE = """
Following context is provided to help you answer the question:

{context}

---

Some of the context might be irrelevant. Use only the context that is relevant to the question. Now, answer the question using the relevant context only: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(
        collection_name="example_collection",
        persist_directory=CHROMA_PATH, 
        embedding_function=embedding_function,
        collection_metadata={"hnsw:space": "cosine"} 
    )

    # Search the DB
    results = db.similarity_search_with_score(query=query_text, k=5)
    prompt = create_template(search_results=results, query_text=query_text)
    print(f"\n\n{prompt}\n\n")

    model = Ollama(model=MODELNAME)
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text


if __name__ == "__main__":
    main()