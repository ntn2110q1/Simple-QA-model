# Simple-Q&A-model
Build a simple question-answering application based on a `Large Language Model (LLM)`. The application uses `LangChain` and the `Retrieval-Augmented Generation (RAG)` technique to retrieve relevant information from documents and generate answers. It also deploys an API using `LangServe` and `FastAPI`.

## Download PDF File data
run `data_source.download.py`. 

Here we have some scientific papers about Transformer structure, BERT, LLM model like Llama, DeepSeek, ...

## Flows
<p align="center">
    <br>
    <a href="[https://github.com/safe](https://github.com/ntn2110q1/Simple-QA-model)">
        <img src="https://github.com/ntn2110q1/Simple-QA-model/blob/main/Flows.png" width="1000"/>
    </a>
    <br>
<p>

## Giao diện FastAPI
In [Google Collab](https://colab.research.google.com/), we need the `ngrok` library to use `FastAPI`.
<p align="center">
    <br>
    <a href="[https://github.com/safe](https://github.com/safe](https://github.com/ntn2110q1/Simple-QA-model)">
        <img src="https://github.com/ntn2110q1/Simple-QA-model/blob/main/FastAPI Interface/FastAPI.png" width="1000"/>
    </a>
    <br>
<p>

To enter a question, go to `Chat.Try it out`
<p align="left">
    <br>
    <a href="[https://github.com/safe](https://github.com/safe](https://github.com/ntn2110q1/Simple-QA-model)">
        <img src="https://github.com/ntn2110q1/Simple-QA-model/blob/main/FastAPI Interface/Input.png" width="500"/>
    </a>
    <br>
<p>

Questions and answers are saved in the `history` folder in `.JSON` format.
<p align="center">
    <br>
    <a href="[https://github.com/safe](https://github.com/safe](https://github.com/ntn2110q1/Simple-QA-model)">
        <img src="https://github.com/ntn2110q1/Simple-QA-model/blob/main/FastAPI Interface/Output.png" width="1000"/>
    </a>
    <br>
<p>
