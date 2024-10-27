from langchain.prompts import ChatPromptTemplate
from typing import List, Tuple
from langchain.schema.document import Document

PROMPT_TEMPLATE = """
Following context is provided to help you answer the question:

{context}

---

Some of the context might be irrelevant. Use only the context that is relevant to the question. Now, answer the question using the relevant context only: {question}
"""

CONTEXT_PROMPT_TEMPLATE = """
We have search for additional context base on the user question. Review each chuck of context, check whether it is relevant to the question and answer the question below. Here is the context:

{context}

---

From the context above, use only parts that is relevant to the question and answer the question: {question}
"""

def create_template(search_results:List[Tuple[Document, float]], query_text:str):
    def _create_context_string(doc:Document, i_context:int):
        return f"<CONTEXT {i_context} STARTS>\nMETADATA={doc.metadata}\nDATA={doc.page_content}\n<CONTEXT {i_context} ENDS>"
    context_text = "\n\n\n\n".join([_create_context_string(doc, i) for i,(doc, _score) in enumerate(search_results)])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    return prompt_template.format(context=context_text, question=query_text)