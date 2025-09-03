import re
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class Str_OutputParser(StrOutputParser):  # Merge 2 class duplicate
    def __init__(self) -> None:
        super().__init__()

    def parse(self, text: str) -> str:
        return self.extract_answer(text)

    def extract_answer(self,
                       text_response: str,
                       patterns: List[str] = [r'Answer:\s*(.*)', r'Assistant:(.*)', r'\nAI:(.*)'],
                       default="Sorry, I am not sure how to help with that."
                       ) -> str:
        input_text = text_response
        default_answer = default
        for pattern in patterns:
            output_text = recursive_extract(input_text, pattern, default_answer)
            if output_text != default_answer:
                input_text = output_text
                default_answer = output_text
        return output_text

class Offline_RAG:

  def __init__(self, llm) -> None:
    self.llm = llm
    self.prompt = hub.pull("rlm/rag-prompt")
    self.str_parser = Str_OutputParser()

  def get_chain(self, retriever):
    input_data = {
        "context": retriever | self.format_docs,
        "question": RunnablePassthrough()
    }
    rag_chain = (
        input_data | self.prompt | self.llm | self.str_parser
    )
    return rag_chain

  def format_docs(self, docs):
    return "\n\n".join(doc.page_content for doc in docs)