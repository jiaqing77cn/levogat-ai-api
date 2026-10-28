# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased] - 2026-10-28

### Added
- New models: `gpt-6-luna`, `gpt-6-sol`, `gpt-6.1-sol`, `gpt-6.1-terra`
- New models: `claude-opus-5-5`, `claude-haiku-5-5`, `claude-fable-5-1`
- New models: `gemini-3.8-flash-tts`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`
- New models: `grok-4.7` (Grok pricing table updated)
- New models: `qwen3.8-27b`, `qwen3.8-max-0902`, `MiniMax-M3.1-Flash`, `MiniMax-H3`
- New models: `doubao-seed-2-1-pro-260915`, `doubao-seed-2-1-turbo-260628`

### Changed
- Model count: 366 → 336 (pricing sync with upstream)
- Group count: 81 → 89
- Pricing tables fully refreshed (GPT/Claude/Gemini/DeepSeek/Grok/CN)
- Title bump: GPT-6 → GPT-6.1, Claude Opus 5 → Opus 5.5, DeepSeek V4 → V4.1, Grok 4.6 → 4.7

### Removed
- Dropped stale models: `gpt-5.3-codex`, `gpt-5.2-codex`, `gpt-5.2-chat-latest`, `gpt-5.4-nano-2026-03-17`
- Dropped stale models: `claude-sonnet-5`, `gemini-3-pro-preview`
- Dropped stale models: `deepseek-v3.2`, `deepseek-v3.2-exp`, `deepseek-v3.1` (renamed `deepseek-v3-1`)
- Dropped stale models: `qwen3-max`, `qwen3-coder-plus`

### Fixed
- `scripts/gen_pricing.py`: Grok keyword list now includes `grok-4.7`, table limit raised 6→7

## [1.0.0] - 2026-07-05

### Added
- Initial release
- 500+ AI models via one OpenAI-compatible API
- Support for Claude (Opus 4.7, Sonnet 4.6, Haiku 4.6)
- Support for GPT (GPT-5, GPT-4o, GPT-4o-mini, GPT-4)
- Support for Gemini (2.5 Pro, 2.0 Flash, 1.5 Pro)
- Support for DeepSeek (V4, Coder, R1)
- Support for Chinese models (Qwen3, Doubao, Zhipu GLM, Kimi, MiniMax)
- Support for media generation (Midjourney, Suno, Sora, Flux, Veo 3)
- Claude Code / Cursor / Codex / Gemini CLI integration
- Dify / FastGPT / n8n / LangChain / NextChat workflow support
- China CDN acceleration (40-200ms latency)
- Streaming support for all models
- Python, Node.js, and curl code examples
- Bilingual documentation (Chinese + English)

### Documentation
- README.md (Chinese) with SEO optimization
- README_EN.md (English) with SEO optimization
- CONTRIBUTING.md
- API docs at https://levogat.apifox.cn/

---

[1.0.0]: https://github.com/jiaqing77cn/levogat-ai-api/releases/tag/v1.0.0
