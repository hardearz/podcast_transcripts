import json
import os

from dotenv import load_dotenv
import requests

load_dotenv()

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

corpora = [
    {
        "custom_dimensions": {},
        "metadata_filter": "",
        "lexical_interpolation": 0.025,
        "semantics": "default",
        "corpus_key": os.environ["VECTARA_CORPUS_KEY"]
    }
]

search = {
    "custom_dimensions": {},
    "metadata_filter": "",
    "lexical_interpolation": 0.025,
    "semantics": "default",
    "offset": 0,
    "limit": 5,
    "context_configuration": {
        "sentences_before": 0,
        "sentences_after": 0,
        "start_tag": "<em>",
        "end_tag": "</em>"
    },
    "reranker": {
        "type": "mmr",
        "diversity_bias": 0.5
    }

}

chat_search = {
    "corpora": corpora,
    "offset": 0,
    "limit": 5,
    "context_configuration": {
        "sentences_before": 2,
        "sentences_after": 2,
        "start_tag": "<em>",
        "end_tag": "</em>"
    },
    "reranker": {
        "type": "mmr",
        "diversity_bias": 0.5
    }
}

generation = {
    "generation_preset_name": "mockingbird-1.0-2024-07-16",
    "max_used_search_results": 5,
    "response_language": "eng",
    "citations": {
        "style": "numeric"
    },
    "enable_factual_consistency_score": True
}

def post(url: str, json: dict, headers: dict) -> dict:
    response = requests.post(url, json=json, headers=headers)
    return response.json()

def post_vectara(url: str, json: dict, headers: dict) -> dict:
    headers = headers.copy()
    headers.update({"x-api-key": os.environ["VECTARA_API_KEY"]})
    #print(headers)
    response = post(url, json, headers)
    return response

def query_vectara(query: str) -> dict:
    corpus_key = os.environ["VECTARA_CORPUS_KEY"]
    url = f"https://api.vectara.io/v2/corpora/{corpus_key}/query"
    request = {
        "query": query,
        "search": search,
        "generation": generation,
        "stream_response": False,

    }

    response = post_vectara(url=url, json=request, headers=headers)

    return response


def create_chat_vectara(query: str):
    url = f"https://api.vectara.io/v2/chats"
    request = {
        "query": query,
        "search": chat_search,
        "generation": generation,
        "chat": {
            "store": True
        },
        "stream_response": False
    }
    response = post_vectara(url=url, json=request, headers=headers)

    return response

def chat_vectara(query: str, chat_id: str):
    url = f"https://api.vectara.io/v2/chats/{chat_id}/turns"
    request = {
        "query": query,
        "search": chat_search,
        "generation": generation,
        "chat": {
            "store": True
        },
        "stream_response": False
    }

    response = post_vectara(url=url, json=request, headers=headers)

    return response