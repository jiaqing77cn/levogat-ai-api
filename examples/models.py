"""
Levogat AI - Supported Models List
====================================
Complete list of 500+ AI models available through the Levogat AI API proxy.

Usage:
    from models import SUPPORTED_MODELS, get_models_by_provider
    print(get_models_by_provider("openai"))

Docs: https://levogat.apifox.cn/
"""

SUPPORTED_MODELS = {
    # OpenAI
    "openai": [
        "gpt-3.5-turbo", "gpt-3.5-turbo-0125", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-16k",
        "gpt-4", "gpt-4-1106-preview", "gpt-4-turbo", "gpt-4-turbo-2024-04-09",
        "gpt-4.1", "gpt-4.1-2025-04-14", "gpt-4.1-mini", "gpt-4.1-mini-2025-04-14",
        "gpt-4.1-nano", "gpt-4.1-nano-2025-04-14", "gpt-4o", "gpt-4o-2024-05-13",
        "gpt-4o-2024-08-06", "gpt-4o-2024-11-20", "gpt-4o-audio-preview-2024-12-17", "gpt-4o-mini",
        "gpt-4o-mini-2024-07-18", "gpt-4o-mini-transcribe", "gpt-4o-mini-tts", "gpt-4o-transcribe",
        "gpt-5", "gpt-5-2025-08-07", "gpt-5-chat-latest", "gpt-5-codex",
        "gpt-5-mini", "gpt-5-mini-2025-08-07", "gpt-5-nano", "gpt-5-nano-2025-08-07",
        "gpt-5-pro", "gpt-5-search-api", "gpt-5-search-api-2025-10-14", "gpt-5.1",
        "gpt-5.1-2025-11-13", "gpt-5.1-chat-latest", "gpt-5.1-codex", "gpt-5.1-codex-mini",
        "gpt-5.2", "gpt-5.2-chat-latest", "gpt-5.2-codex", "gpt-5.2-pro",
        "gpt-5.3-codex", "gpt-5.4", "gpt-5.4-mini", "gpt-5.4-mini-2026-03-17",
        "gpt-5.4-nano", "gpt-5.4-nano-2026-03-17", "gpt-5.4-pro", "gpt-5.4-pro-2026-03-05",
        "gpt-5.5", "gpt-5.5-pro", "gpt-5.6-luna", "gpt-5.6-sol",
        "gpt-5.6-terra", "gpt-6-astra", "gpt-audio-2025-08-28", "gpt-chat-latest",
        "gpt-image-1", "gpt-image-1-mini", "gpt-image-1.5", "gpt-image-2",
        "gpt-image-2-c", "gpt-image-2.5-flare", "gpt-image-2.5-flare-c", "gpt-image-2.5-sunburst",
        "gpt-image-2.5-sunburst-c", "gpt-oss-120b", "o1", "o1-2024-12-17",
        "o3", "o3-2025-04-16", "o3-mini", "o3-mini-2025-01-31",
        "o3-pro", "o3-pro-2025-06-10", "o4-mini", "o4-mini-2025-04-16",
        "text-embedding-3-large", "text-embedding-3-small", "text-embedding-ada-002", "tts-1",
        "tts-1-1106", "tts-1-hd", "tts-1-hd-1106", "whisper-1",
    ],
    # Anthropic
    "anthropic": [
        "claude-fable-5", "claude-fable-5-1", "claude-haiku-4-5-20251001", "claude-opus-4-1-20250805",
        "claude-opus-4-5-20251101", "claude-opus-4-6", "claude-opus-4-7", "claude-opus-4-8",
        "claude-opus-5", "claude-sonnet-4-5-20250929", "claude-sonnet-4-6", "claude-sonnet-5",
    ],
    # Google
    "google": [
        "gemini-2.5-flash", "gemini-2.5-flash-image", "gemini-2.5-flash-lite", "gemini-2.5-flash-preview-tts",
        "gemini-2.5-pro", "gemini-2.5-pro-preview-tts", "gemini-3-flash-preview", "gemini-3-pro-image",
        "gemini-3-pro-image-preview", "gemini-3-pro-preview", "gemini-3.1-flash-image", "gemini-3.1-flash-image-preview",
        "gemini-3.1-flash-lite", "gemini-3.1-flash-lite-image", "gemini-3.1-flash-lite-preview", "gemini-3.1-flash-tts-preview",
        "gemini-3.1-pro-preview", "gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-3.6-flash",
        "gemini-3.7-flash", "gemini-3.8-flash", "gemini-embedding-001", "gemini-embedding-2-preview",
        "gemini-flash-latest", "gemini-flash-lite-latest", "gemini-pro-latest",
    ],
    # DeepSeek
    "deepseek": [
        "deepseek-r1", "deepseek-r1-0528", "deepseek-v3", "deepseek-v3-1",
        "deepseek-v3.1", "deepseek-v3.2", "deepseek-v3.2-exp", "deepseek-v4-flash",
        "deepseek-v4-flash-0731", "deepseek-v4-pro", "deepseek-v4-pro-0813", "deepseek-v4.1-flash",
    ],
    # xAI
    "grok": [
        "grok-1.5-video", "grok-4", "grok-4-20-non-reasoning", "grok-4-20-reasoning",
        "grok-4.3", "grok-4.5", "grok-4.6", "grok-build-0.1",
        "grok-imagine-image", "grok-imagine-image-2.0", "grok-imagine-image-quality", "grok-imagine-video",
        "grok-imagine-video-1.5-preview",
    ],
    # Chinese Models
    "chinese": [
        "MiniMax-Hailuo-02", "MiniMax-Hailuo-2.3", "MiniMax-M2.5", "MiniMax-M2.7",
        "MiniMax-M3", "MiniMax-Voice-Design", "Qwen/Qwen3-Reranker-0.6B", "doubao-seed-1-6-250615",
        "doubao-seed-1-6-251015", "doubao-seed-1-6-flash-250828", "doubao-seed-1-6-thinking-250615", "doubao-seed-1-6-thinking-250715",
        "doubao-seed-1-6-vision-250815", "doubao-seed-1-8-251228", "doubao-seed-2-0-code-preview-260215", "doubao-seed-2-0-lite-260215",
        "doubao-seed-2-0-lite-260428", "doubao-seed-2-0-mini-260215", "doubao-seed-2-0-mini-260428", "doubao-seed-2-0-pro-260215",
        "doubao-seed-2-1-pro-260628", "glm-4", "glm-4-airx", "glm-4-flash",
        "glm-4-long", "glm-4.5", "glm-4.5-air", "glm-4.6",
        "glm-4.7", "glm-5", "glm-5.1", "glm-5.2",
        "glm-5.3", "glm-5.3-flash", "kimi-k2", "kimi-k2-0711-preview",
        "kimi-k2.5", "kimi-k2.6", "kimi-k2.7-code", "kimi-k3",
        "qwen-flash", "qwen-image-2.0-2026-03-03", "qwen-image-3.0", "qwen-image-3.0-pro",
        "qwen-image-edit-2509", "qwen-image-max", "qwen-image-max-2025-12-30", "qwen-max",
        "qwen-plus", "qwen-plus-2025-12-01", "qwen-plus-character", "qwen-plus-latest",
        "qwen-turbo", "qwen-vl-max", "qwen3-14b", "qwen3-235b-a22b",
        "qwen3-235b-a22b-instruct-2507", "qwen3-30b-a3b", "qwen3-30b-a3b-instruct-2507", "qwen3-30b-a3b-think",
        "qwen3-30b-a3b-thinking-2507", "qwen3-32b", "qwen3-8b", "qwen3-coder-30b-a3b-instruct",
        "qwen3-coder-480b-a35b-instruct", "qwen3-coder-flash", "qwen3-coder-plus", "qwen3-max",
        "qwen3-max-2026-01-23", "qwen3-max-preview", "qwen3-next-80b-a3b-instruct", "qwen3-next-80b-a3b-thinking",
        "qwen3-rerank", "qwen3-vl-235b-a22b-instruct", "qwen3-vl-235b-a22b-thinking", "qwen3-vl-30b-a3b-instruct",
        "qwen3-vl-30b-a3b-thinking", "qwen3-vl-32b-instruct", "qwen3-vl-32b-thinking", "qwen3-vl-8b-instruct",
        "qwen3-vl-8b-thinking", "qwen3-vl-flash", "qwen3-vl-plus", "qwen3.5-122b-a10b",
        "qwen3.5-27b", "qwen3.5-35b-a3b", "qwen3.5-397b-a17b", "qwen3.5-plus",
        "qwen3.5-plus-2026-02-15", "qwen3.6-27b", "qwen3.6-35b-a3b", "qwen3.6-max-preview",
        "qwen3.6-plus", "qwen3.6-plus-2026-04-02", "qwen3.7-max", "qwen3.7-plus",
        "qwen3.8-27b", "qwen3.8-flash", "qwen3.8-max", "qwen3.8-max-0902",
    ],
    # Media Generation
    "media": [
        "BAAI/bge-reranker-v2-m3", "Pro/BAAI/bge-reranker-v2-m3", "aigc-image-kling", "aigc-video-hailuo",
        "doubao-seedance-1-0-pro-250528", "doubao-seedance-1-0-pro-fast-251015", "doubao-seedance-1-5-pro-251215", "doubao-seedance-2-0-260128",
        "doubao-seedance-2-0-fast-260128", "doubao-seedance-2-5-260628", "doubao-seedream-3-0-t2i-250415", "doubao-seedream-4-0-250828",
        "doubao-seedream-4-5-251128", "doubao-seedream-5-0-260128", "doubao-seedream-5-0-pro-260628", "flux-1.1-pro",
        "flux.1-kontext-pro", "happyhorse-1.0-video-edit", "kling-3.0-turbo", "kling-advanced-custom-elements",
    ],
}


def get_models_by_provider(provider: str) -> list[str]:
    """Get all models for a given provider."""
    return SUPPORTED_MODELS.get(provider.lower(), [])


def get_all_models() -> list[str]:
    """Get all supported models across all providers."""
    all_models = []
    for models in SUPPORTED_MODELS.values():
        all_models.extend(models)
    return sorted(set(all_models))


if __name__ == "__main__":
    for provider, models in SUPPORTED_MODELS.items():
        print(f"{provider}: {len(models)} models")
        for m in models[:5]:
            print(f"  - {m}")
        if len(models) > 5:
            print(f"  ... and {len(models) - 5} more")
        print()
    print(f"Total: {len(get_all_models())} models")
