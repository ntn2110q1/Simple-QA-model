import os
import wget

file_links = [
    {
        "title": "Attention is All you Need",
        "url": "https://arxiv.org/pdf/1706.03762"
    },
    {
        "title": "BERT- Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "url": "https://arxiv.org/pdf/1810.04805"
    },
    {
        "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
        "url": "https://arxiv.org/pdf/2201.11903"
    },
    {
        "title": "Instruction Tuning for Large Language Models- A Survey",
        "url": "https://arxiv.org/pdf/2308.10792"
    },
    {
        "title": "Llama 2- Open Foundation and Fine-Tuned Chat Models",
        "url": "https://arxiv.org/pdf/2307.09288"
    },
    {
        "title": "DeepSeek LLM Scaling Open-Source Language Models with Longtermism",
        "url": "https://arxiv.org/pdf/2401.02954"
    },
    {
        "title": r"DeepSeek-V2",
        "url": "https://arxiv.org/pdf/2405.04434"
    },
    {
        "title": "DeepSeek-V3 Technical Report",
        "url": "https://arxiv.org/pdf/2412.19437"
    },
    {
        "title": r"DeepSeek-R1",
        "url": "https://arxiv.org/pdf/2501.12948?"
    },
]

folder = r"C:\AI\AIO2024\Module10\data_source"

def is_exist(file_link):
    return os.path.exists(os.path.join(folder, f"{file_link['title']}.pdf"))

if not os.path.exists(folder):
    os.makedirs(folder)

for file_link in file_links:
    if not is_exist(file_link):
        wget.download(file_link["url"], out=os.path.join(folder, f"{file_link['title']}.pdf"))