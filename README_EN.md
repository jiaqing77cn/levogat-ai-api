<h1 align="center">🚀 AI API Proxy in China Without VPN | Claude/GPT/Gemini/DeepSeek | Levogat AI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/500%2B-Models-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-China%20Accel-3b82f6?style=flat" alt="CDN"/>
  <img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat" alt="OpenAI Compatible"/>
</p>

<div align="center">

**No VPN · Low Latency · 366 Models · OpenAI Compatible · Claude Code Ready**

[🌐 Website](https://api.levogat.com) · [📋 Pricing](https://api.levogat.com/pricing) · [📖 API Docs](https://levogat.apifox.cn/) · [💬 Contact](https://api.levogat.com)

</div>

> Last updated: 2026-09-17 18:15 (UTC+8)| [中文](./README.md) | [한국어](./README_KO.md) | [日本語](./README_JA.md) | [Español](./README_ES.md) | [Deutsch](./README_DE.md) | English

---

## 📋 Table of Contents

- [🖥️ Product Preview](#-product-preview)
- [🔍 How to Choose an API Proxy](#-how-to-choose-an-api-proxy)
- [💰 Live Model Pricing](#-live-model-pricing)
- [🛠️ Integration Guide](#-integration-guide)
- [📊 Comparison](#-comparison)
- [❓ FAQ](#-faq)
- [📖 In-Depth Guides](#-in-depth-guides)
- [🤝 Contributing](#-contributing)

---

## 🖥️ Product Preview

![Levogat AI homepage - 366 AI model API proxy dashboard](https://raw.githubusercontent.com/jiaqing77cn/levogat-ai-api/main/assets/homepage.jpg)

![Levogat AI dashboard - create API keys, view usage, top up account](https://raw.githubusercontent.com/jiaqing77cn/levogat-ai-api/main/assets/console.jpg)

---

## 🔍 How to Choose an API Proxy

Six dimensions to evaluate when choosing an AI API proxy:

| Dimension | What to Check | Red Flags |
|-----------|--------------|-----------|
| **Stability** | Frequent downtime? High latency? | Disconnections, no announcements |
| **Speed** | Is response latency acceptable? | >5s first token delay |
| **Model Coverage** | Latest models available? | Slow to add new models |
| **Price Transparency** | Clear billing? Usage logs? | No call records, opaque |
| **Model Swapping** | Using cheap models to impersonate premium? | Abnormally low prices, poor quality |
| **Exit Risk** | Company-operated? Has support? | Solo operator, no customer service |

### ⚠️ Pitfall Checklist

1. **Cache price trap**: Normal cache price is 10%, some charge 15%-30%
2. **Model swapping detection**: Compare outputs between official and proxy with same prompts
3. **Token count fraud**: Send requests with known token counts, check if billing is inflated
4. **Low price trap**: Prices far below market rate likely mean GLM impersonating GPT
5. **Exit scam risk**: Don't deposit large amounts! Pay as you go

### 🔬 How to Detect Model Swapping

```python
# Method 1: Capability test - use reasoning prompts
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claude correct answer: 9
# Low-end models often get it wrong: 8

# Method 2: Long context test
# Send 50K+ token long text, ask about details at the end
# Low-end models lose context

# Method 3: Code capability test
prompt = "Implement an LRU cache with TTL expiration in Python"
# Compare code quality between official and proxy
```

---

## 💰 Live Model Pricing

> Prices are automatically fetched from [Levogat API](https://api.levogat.com/api/pricing) by GitHub Actions, updated hourly.
>
> Unit: USD / Million Tokens | Output/Input ratio = output price ÷ input price

### OpenAI GPT Series

<!-- GPT_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gpt-6-astra` | Codex-Gpt-1 | 0.07x | $0.74 | $3.68 | Azure-Gpt-6 | 1.8x | $18.00 | $90.00 | 5x |
| `gpt-5.6-sol` | Codex-Gpt-1 | 0.07x | $0.37 | $2.21 | Azure-Gpt-6 | 1.8x | $9.00 | $54.00 | 6x |
| `gpt-5.6-luna` | Azure-Gpt-2 | 0.21x | $0.04 | $0.25 | Azure-Gpt-6 | 1.8x | $0.36 | $2.16 | 6x |
| `gpt-5.6-terra` | Codex-Gpt-1 | 0.07x | $0.15 | $0.88 | Azure-Gpt-6 | 1.8x | $3.60 | $21.60 | 6x |
| `gpt-5.5` | Codex-Gpt-1 | 0.07x | $0.37 | $2.21 | Azure-Gpt-6 | 1.8x | $9.00 | $54.00 | 6x |
| `gpt-5.5-pro` | Openai-Gpt-1 | 1.18x | $35.29 | $211.77 | Azure-Gpt-6 | 1.8x | $54.00 | $324.00 | 6x |
| `gpt-5.4-pro` | Azure-Gpt-1 | 0.09x | $2.65 | $15.88 | Azure-Gpt-6 | 1.8x | $54.00 | $324.00 | 6x |
| `gpt-5.4-pro-2026-03-05` | Azure-Gpt-2 | 0.21x | $6.18 | $37.06 | Openai-Gpt-2 | 1.47x | $44.12 | $264.71 | 6x |
| `gpt-5.4-mini` | Azure-Gpt-1 | 0.09x | $0.07 | $0.40 | Azure-Gpt-6 | 1.8x | $1.35 | $8.10 | 6x |
| `gpt-5.4-mini-2026-03-17` | Azure-Gpt-1 | 0.09x | $0.07 | $0.40 | Openai-Gpt-2 | 1.47x | $1.10 | $6.62 | 6x |
| `gpt-5.4-nano` | Azure-Gpt-1 | 0.09x | $0.02 | $0.11 | Azure-Gpt-6 | 1.8x | $0.36 | $2.25 | 6.25x |
| `gpt-5.4-nano-2026-03-17` | Azure-Gpt-1 | 0.09x | $0.02 | $0.11 | Openai-Gpt-2 | 1.47x | $0.29 | $1.84 | 6.25x |
| `gpt-5.3-codex` | Azure-Gpt-2 | 0.21x | $0.36 | $2.88 | Openai-Gpt-2 | 1.47x | $2.57 | $20.59 | 8x |
| `gpt-5.2-codex` | Azure-Gpt-2 | 0.21x | $0.36 | $2.88 | Openai-Gpt-2 | 1.47x | $2.57 | $20.59 | 8x |
| `gpt-5.2-chat-latest` | Azure-Gpt-1 | 0.09x | $0.15 | $1.24 | Openai-Gpt-2 | 1.47x | $2.57 | $20.59 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Anthropic Claude Series

<!-- CLAUDE_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `claude-fable-5` | Claude-Code-… | 0.35x | $3.53 | $17.65 | AWS-Claude-3 | 2.2x | $22.00 | $110.00 | 5x |
| `claude-fable-5-1` | Claude-Code-… | 0.35x | $3.53 | $17.65 | AWS-Claude-3 | 2.2x | $22.00 | $110.00 | 5x |
| `claude-haiku-4-5-20251001` | Kiro-Claude-… | 0.18x | $0.18 | $0.88 | AWS-Claude-3 | 2.2x | $2.20 | $11.00 | 5x |
| `claude-opus-4-1-20250805` | Azure-Claude… | 0.88x | $13.24 | $66.18 | AWS-Claude-3 | 2.2x | $33.00 | $165.00 | 5x |
| `claude-opus-4-5-20251101` | Kiro-Claude-… | 0.18x | $0.88 | $4.41 | AWS-Claude-3 | 2.2x | $11.00 | $55.00 | 5x |
| `claude-opus-4-6` | Kiro-Claude-… | 0.18x | $0.88 | $4.41 | AWS-Claude-3 | 2.2x | $11.00 | $55.00 | 5x |
| `claude-opus-4-7` | Kiro-Claude-… | 0.18x | $0.88 | $4.41 | AWS-Claude-3 | 2.2x | $11.00 | $55.00 | 5x |
| `claude-opus-4-8` | Kiro-Claude-… | 0.18x | $0.88 | $4.41 | AWS-Claude-3 | 2.2x | $11.00 | $55.00 | 5x |
| `claude-opus-5` | Kiro-Claude-… | 0.18x | $0.88 | $4.41 | AWS-Claude-3 | 2.2x | $11.00 | $55.00 | 5x |
| `claude-sonnet-4-5-20250929` | Kiro-Claude-… | 0.18x | $0.53 | $2.65 | AWS-Claude-3 | 2.2x | $6.60 | $33.00 | 5x |
| `claude-sonnet-4-6` | Kiro-Claude-… | 0.18x | $0.53 | $2.65 | AWS-Claude-3 | 2.2x | $6.60 | $33.00 | 5x |
| `claude-sonnet-5` | Kiro-Claude-… | 0.18x | $0.35 | $1.76 | AWS-Claude-3 | 2.2x | $4.40 | $22.00 | 5x |

<!-- CLAUDE_PRICE_TABLE_END -->

### Google Gemini Series

<!-- GEMINI_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gemini-3.8-flash` | Anti-Gemini-… | 0.15x | $0.11 | $0.55 | Aistudio-Gem… | 1.91x | $1.43 | $7.17 | 5x |
| `gemini-3.7-flash` | Anti-Gemini-… | 0.15x | $0.11 | $0.55 | Aistudio-Gem… | 1.91x | $1.43 | $7.17 | 5x |
| `gemini-3.6-flash` | Anti-Gemini-… | 0.15x | $0.11 | $0.55 | Aistudio-Gem… | 1.91x | $1.43 | $7.17 | 5x |
| `gemini-3.5-flash` | Anti-Gemini-… | 0.15x | $0.22 | $1.32 | Aistudio-Gem… | 1.91x | $2.87 | $17.21 | 6x |
| `gemini-3.5-flash-lite` | Anti-Gemini-… | 0.15x | $0.04 | $0.37 | Aistudio-Gem… | 1.91x | $0.57 | $4.78 | 8.33x |
| `gemini-3-pro-image` | Aistudio-Gem… | 0.35x | $0.00 | $0.00 | Aistudio-Gem… | 1.91x | $0.00 | $0.00 | 0x |
| `gemini-3-pro-image-preview` | Aistudio-Gem… | 0.35x | $0.00 | $0.00 | Aistudio-Gem… | 1.91x | $0.00 | $0.00 | 0x |
| `gemini-3-pro-preview` | Anti-Gemini-… | 0.15x | $0.29 | $1.76 | Aistudio-Gem… | 1.91x | $3.82 | $22.94 | 6x |

<!-- GEMINI_PRICE_TABLE_END -->

### DeepSeek Series

<!-- DEEPSEEK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `deepseek-v4.1-flash` | Self-Deploye… | 1x | $0.30 | $1.20 | Self-Deploye… | 1.5x | $0.45 | $1.80 | 4x |
| `deepseek-v4-pro` | Self-Deploye… | 1x | $1.32 | $3.96 | deepseek-1 | 2.2x | $2.90 | $8.71 | 3x |
| `deepseek-v4-pro-0813` | Self-Deploye… | 1x | $1.32 | $3.96 | deepseek-1 | 2.2x | $2.90 | $8.71 | 3x |
| `deepseek-v4-flash` | Self-Deploye… | 1x | $0.44 | $1.32 | deepseek-1 | 2.2x | $0.97 | $2.90 | 3x |
| `deepseek-v4-flash-0731` | Self-Deploye… | 1x | $0.44 | $1.32 | deepseek-1 | 2.2x | $0.97 | $2.90 | 3x |
| `deepseek-v3.2` | Alibaba-1 | 1x | $0.29 | $0.43 | Alibaba-3 | 2.2x | $0.64 | $0.96 | 1.5x |
| `deepseek-v3.2-exp` | Alibaba-1 | 1x | $0.29 | $0.43 | Alibaba-3 | 2.2x | $0.64 | $0.96 | 1.5x |
| `deepseek-v3.1` | Self-Deploye… | 0.6x | $0.35 | $1.04 | Alibaba-3 | 2.2x | $1.28 | $3.83 | 3x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### xAI Grok Series

<!-- GROK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `grok-4.6` | Cli-Grok-1 | 0.15x | $0.29 | $0.88 | Xai-Grok-1 | 0.88x | $1.76 | $5.29 | 3x |
| `grok-4.5` | Cli-Grok-1 | 0.15x | $0.29 | $0.88 | Xai-Grok-1 | 0.88x | $1.76 | $5.29 | 3x |
| `grok-4.3` | Azure-Grok-1 | 0.15x | $0.18 | $0.37 | Xai-Grok-1 | 0.88x | $1.10 | $2.21 | 2x |
| `grok-4-20-non-reasoning` | Cli-Grok-1 | 0.15x | $0.18 | $0.37 | Xai-Grok-1 | 0.88x | $1.10 | $2.21 | 2x |
| `grok-4-20-reasoning` | Cli-Grok-1 | 0.15x | $0.18 | $0.37 | Xai-Grok-1 | 0.88x | $1.10 | $2.21 | 2x |
| `grok-4` | Azure-Grok-1 | 0.15x | $0.44 | $2.21 | Azure-Grok-2 | 0.22x | $0.66 | $3.31 | 5x |

<!-- GROK_PRICE_TABLE_END -->

### Chinese Models (Qwen/Doubao/GLM/Kimi/MiniMax)

<!-- CN_MODEL_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `qwen3.8-max` | Self-Deploye… | 0.6x | $1.20 | $3.60 | Alibaba-3 | 2.2x | $4.40 | $13.20 | 3x |
| `qwen3-max` | Self-Deploye… | 0.6x | $0.72 | $3.60 | Alibaba-3 | 2.2x | $2.64 | $13.20 | 5x |
| `qwen3-coder-plus` | Self-Deploye… | 0.6x | $0.60 | $3.00 | Self-Deploye… | 1x | $1.00 | $5.00 | 5x |
| `glm-5.3` | Self-Deploye… | 1x | $1.40 | $4.40 | Alibaba-3 | 2.2x | $3.08 | $9.68 | 3.14x |
| `glm-5.3-flash` | Self-Deploye… | 1x | $0.15 | $0.50 | Self-Deploye… | 1.5x | $0.22 | $0.75 | 3.33x |
| `glm-5.2` | Self-Deploye… | 1x | $1.40 | $4.40 | Alibaba-3 | 2.2x | $3.08 | $9.68 | 3.14x |
| `kimi-k3` | Self-Deploye… | 1x | $3.00 | $15.00 | Self-Deploye… | 1.5x | $4.50 | $22.50 | 5x |
| `kimi-k2.7-code` | Self-Deploye… | 1x | $0.95 | $3.95 | Kimi-2 | 2.2x | $2.09 | $8.68 | 4.15x |
| `kimi-k2.5` | Alibaba-1 | 1x | $0.60 | $3.15 | Alibaba-3 | 2.2x | $1.32 | $6.93 | 5.25x |
| `doubao-seed-2-1-pro-260628` | Doubao-2 | 1.5x | $1.35 | $6.75 | Doubao-3 | 2.2x | $1.98 | $9.90 | 5x |
| `doubao-seed-1-6-250615` | Doubao-2 | 1.5x | $0.18 | $1.80 | Doubao-3 | 2.2x | $0.26 | $2.64 | 10x |
| `MiniMax-M3` | Self-Deploye… | 1x | $0.30 | $1.20 | Hailuo-3 | 2.2x | $0.66 | $2.64 | 4x |
| `MiniMax-M2.7` | Self-Deploye… | 1.5x | $0.45 | $1.80 | Hailuo-3 | 2.2x | $0.66 | $2.64 | 4x |
| `qwen3.8-flash` | Alibaba-2 | 1.5x | $0.22 | $0.70 | Alibaba-3 | 2.2x | $0.33 | $1.03 | 3.13x |

<!-- CN_MODEL_PRICE_TABLE_END -->

> 💡 Full pricing with all 81 groups and 366 models at [Levogat AI Pricing](https://api.levogat.com/pricing)

### Group Tiers

| Group Type | Ratio | Best For |
|------------|-------|----------|
| Flash Sale | 0.6x | Testing, low-cost use |
| Codex Exclusive | 0.8x | GPT coding, daily use |
| Default | 1.0x | Standard quality, balanced |
| anti/kiro | 1.2x | Budget Claude |
| Claude Code Exclusive | 2.4x | Claude Code programming |
| Azure Channel | 3.0x | Stable GPT |
| AWS Enterprise | 4.0x | Enterprise-grade Claude |
| Vertex/Direct | 6.0x | Highest quality |
| Official Premium | 16.0x | Full official quality |

---

## 🛠️ Integration Guide

### Quick Start

1. Visit [Levogat AI](https://api.levogat.com) -> Register -> Console -> Create Key
2. Top up (min 1 yuan)
   - Alipay / WeChat Pay / Crypto Pay / Credit Card / Stripe
3. Choose your integration method:

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="***",
    base_url="https://api.levogat.com/v1"
)

# GPT-5.6 Sol
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Write a Python quicksort"}]
)

# Claude Sonnet 5
resp = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# DeepSeek V4
resp = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "Implement a web server in Python"}]
)
```

### Node.js / curl

```bash
curl https://api.levogat.com/v1/chat/completions \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

Full examples in [`examples/`](./examples/) directory (incl. [Python](examples/quickstart.py) / [Node.js](examples/quickstart.js) / [Shell](examples/quickstart.sh)).

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="***"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

📖 Full guide: [Claude Code Setup](docs/en/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://api.levogat.com/v1"
```

📖 Full guide: [Codex Setup](docs/en/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://api.levogat.com/v1"
```

📖 Full guide: [Cursor IDE Setup](docs/en/cursor-setup.md) (also applies to Gemini CLI)

### Tool Integrations

| Tool | Setup |
|------|-------|
| **Dify / FastGPT** | API Key + Base URL: `https://api.levogat.com/v1` |
| **n8n** | HTTP Request -> URL: `https://api.levogat.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://api.levogat.com/v1")` |
| **NextChat** | Settings -> Custom API -> URL: `https://api.levogat.com/v1` |
| **Cursor IDE** | Settings -> Env Vars -> `ANTHROPIC_BASE_URL=https://api.levogat.com/v1` |
| **OpenClaw** | `openai_api_key: key` + `openai_api_base: https://api.levogat.com/v1` |

### Use Cases

- **AI Coding** - Claude Code / Codex with Claude Opus 5 / GPT-5.6 for refactoring, bug fixes
- **Long Document Processing** - 100K+ word analysis, contract review, paper summarization
- **AI Agents** - One key for all models, multi-agent parallel tasks
- **RAG Knowledge Bases** - DeepSeek / GPT with vector databases for enterprise Q&A
- **Automated Workflows** - n8n / FastGPT / Dify integration for full automation

---

## 📊 2026 Comparison & Review

> Based on publicly available information as of 2026-07-29. For reference only.

| | [Levogat AI](https://api.levogat.com) | OpenRouter | SiliconFlow | Other Proxies | Self-Built |
|--|-------------|-----------|-------------|---------------|------------|
| Model count | **366** | ~400 | ~200 | ~100 | Manual |
| Group options | **81 groups** | None (per-provider) | None | 1-3 | - |
| China CDN | ✅ Multi-node | ❌ No China nodes | ✅ Single | ✅ | ❌ |
| Min top-up | **¥1** | ~¥35 | ¥50 | ¥20 | - |
| Pay-as-you-go | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code ready | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI compatible | ✅ | ✅ | ✅ | ✅ | Needs adapter |
| Price transparency | ✅ 81 groups | Per-model, limited choice | Single price | Single price | - |
| GitHub open source | ✅ Auto-pricing | ❌ | ❌ | ❌ | - |

---

## ❓ FAQ

**Are responses identical to the official API?**

Yes. Levogat AI only forwards requests to official models - responses are consistent with the official API.

**Can my account get banned?**

No. You use Levogat AI's key, not the official account system - your official account is not at risk.

**What's the difference between groups?**

Different groups correspond to different backend channels (Azure/AWS/Vertex/Official Direct, etc.) with varying quality and price. Lower-cost groups offer better value; higher-priced groups offer maximum stability. Start with the default group, then adjust as needed.

**Is streaming supported?**

Yes, all models support `stream: true` with low latency.

**How fast is it from China?**

China CDN nodes, latency typically 40-200ms - much faster than connecting to official APIs directly.

**Is there a free tier?**

New users get trial credits. Start free, top up when ready.

**Which group should I choose?**

- Budget: Flash Sale (0.6x) / Codex Exclusive (0.8x)
- Balanced: Default (1.0x)
- High quality: Claude Code Exclusive (2.4x) / Azure (3.0x)
- Maximum quality: Vertex (6.0x) / Official Premium (16.0x)

---

## 📖 In-Depth Guides

| Guide | Content |
|-------|---------|
| [Claude Code Setup Guide](docs/en/claude-code-guide.md) | Complete Claude Code configuration for China |
| [Claude Desktop Guide](docs/en/claude-desktop-guide.md) | Configure Claude Desktop with Levogat AI |
| [Codex Setup Guide](docs/en/codex-setup.md) | OpenAI Codex CLI configuration for China |
| [Gemini CLI Guide](docs/en/gemini-cli-guide.md) | Gemini CLI with Levogat AI for Gemini models |
| [Cursor IDE Setup](docs/en/cursor-setup.md) | Use GPT-5.6 / Claude Opus 5 / Gemini in Cursor |
| [Grok Build Guide](docs/en/grok-build-guide.md) | xAI Grok Build with custom Levogat AI models |
| [OpenCode Guide](docs/en/opencode-guide.md) | OpenCode open-source agent with Levogat AI |
| [OpenClaw Guide](docs/en/openclaw-guide.md) | OpenClaw Agent runtime with Levogat AI |
| [CC Switch Guide](docs/en/cc-switch-guide.md) | Unified config management for multiple AI tools |
| [Dify Integration Guide](docs/en/dify-integration.md) | Connect Dify with Levogat AI |
| [Model Selection Guide](docs/en/model-selection-guide.md) | Which of 366 models to choose? By use case & budget |
| [API Relay Directory](docs/en/api-relay-list.md) | Verified-live relay stations 2026 — submit yours via Issue |
| [Fraud Detection Guide](docs/en/fraud-detection-guide.md) | 5 methods to detect model swapping in API proxies |
| [Cost Calculator Guide](docs/en/cost-calculator-guide.md) | Estimate API costs and optimize spending |

---

## 🤝 Contributing

- 🐛 Bug report -> [Open an Issue](https://github.com/jiaqing77cn/levogat-ai-api/issues)
- 📝 Improve docs -> Submit a PR
- 💡 Feature request -> [Start a Discussion](https://github.com/jiaqing77cn/levogat-ai-api/discussions)
- 📄 Contributing guide -> See [CONTRIBUTING.md](./CONTRIBUTING.md)
- 📋 Changelog -> See [CHANGELOG.md](./CHANGELOG.md)

---

## 📜 License

MIT License · Copyright (c) 2026 [Levogat AI](https://api.levogat.com)

## 📢 Trademark Notice

GPT and OpenAI are trademarks of OpenAI. Claude is a trademark of Anthropic PBC. Gemini is a trademark of Google LLC. DeepSeek is a trademark of DeepSeek. This repository describes compatibility only and does not imply official affiliation with or endorsement by these companies.
