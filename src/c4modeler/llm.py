# src/llm.py
from __future__ import annotations

from typing import Literal
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from langchain_xai import ChatXAI

MODEL_PROVIDER_MAP = {
    "gemini-1.5-flash-latest": ChatGoogleGenerativeAI,
    "gemini-1.5-pro-latest": ChatGoogleGenerativeAI,
    "gemini-2.5-flash-preview-05-20": ChatGoogleGenerativeAI,
    "gemini-2.5-pro-preview-05-20": ChatGoogleGenerativeAI,
    "gemini-2.5-pro-preview-06-05": ChatGoogleGenerativeAI,
    "gpt-4o": ChatOpenAI,
    "gpt-4o-mini": ChatOpenAI,
    "deepseek-chat": ChatDeepSeek,
    "grok-beta": ChatXAI,
    "grok-3-latest": ChatXAI,
}

ModelName = Literal[
    "gemini-1.5-flash-latest", "gemini-1.5-pro-latest",
    "gemini-2.5-flash-preview-05-20", "gemini-2.5-pro-preview-05-20", "gemini-2.5-pro-preview-06-05",
    "gpt-4o", "gpt-4o-mini",
    "deepseek-chat",
    "grok-beta", "grok-3-latest"
]

def get_llm(model_name: ModelName, temperature: float = 0.0) -> BaseChatModel:
    """
    Instantiates and returns a language model based on a direct mapping.
    """
    print(f"--- ⚙️  Instantiating model: {model_name} ---")
    model_class = MODEL_PROVIDER_MAP.get(model_name)
    if model_class is None:
        raise ImportError(
            f"Model '{model_name}' is not available. "
            f"Check if its provider library (e.g., langchain_xai) is installed."
        )
    return model_class(model=model_name, temperature=temperature)
