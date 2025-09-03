import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from langserve import add_routes

from source_code.base.llm import get_hf_llm
from source_code.rag.main import build_rag_chain, InputQA, OutputQA
from source_code.chat.main import build_chat_chain

llm = get_hf_llm(temperature=0.9)

genai_docs = "/content/drive/MyDrive/LangChain/data_source"

# ----------Chains----------

genai_chain = build_rag_chain(llm, data_dir=genai_docs, data_type="pdf")

chat_chain = build_chat_chain(llm, history_folder="./chat_histories", max_history_length=6)

#-----------App - FastAPI-----------

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# -----------Routers - FastAPI-----------
@app.get("/check")
async def check():
    return {"status": "ok"}

@app.post("/generative_ai", response_model=OutputQA)
async def generative_ai(inputs: InputQA):
    answer = genai_chain.invoke(inputs.question)
    return {"answer": answer}

# Thêm route thủ công cho /chat (thay vì add_routes để tránh lỗi LangServe)
@app.post("/chat")
async def chat(inputs: InputChat):
    response = chat_chain.invoke({"human_input": inputs.human_input}, config={"configurable": {"session_id": "default_session"}})
    return {"response": response}