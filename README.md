<h1 align="center">🚀 Levogat 国内 AI API 中转站 | GPT-6/Claude Opus 5/Gemini 3.8/DeepSeek V4/Grok 4.6 免翻墙直连</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/500%2B-Models-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-China%20加速-3b82f6?style=flat" alt="CDN"/>
  <img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat" alt="OpenAI Compatible"/>
</p>

<div align="center">

· 低延迟 · 366 个模型 · OpenAI 兼容 · Claude Code

[🌐 官网](https://api.levogat.com) · [📋 定价](https://api.levogat.com/pricing) · [📖 API 文档](https://levogat.apifox.cn/) · [💬 联系](https://api.levogat.com)

</div>

> 最后更新：2026-09-19 23:44 (UTC+8) | [English](./README_EN.md) | [한국어](./README_KO.md) | [日本語](./README_JA.md) | [Español](./README_ES.md) | [Deutsch](./README_DE.md) | 中文

---

## 📋 目录

- [🖥️ 产品预览](#-产品预览)
- [🔍 中转站选购指南](#-中转站选购指南)
- [💰 实时模型价格](#-实时模型价格)
- [🛠️ 接入教程](#-接入教程)
- [📊 竞品对比](#-竞品对比)
- [❓ FAQ](#-faq)
- [📖 深入教程](#-深入教程)
- [🤝 贡献](#-贡献)

---

## 🖥️ 产品预览

![levogat AI 首页 - 366 个 AI 模型 API 中转平台](https://raw.githubusercontent.com/jiaqing77cn/levogat-ai-api/main/assets/homepage.jpg)

![levogat AI 控制台 - 创建 API Key、查看用量、充值](https://raw.githubusercontent.com/jiaqing77cn/levogat-ai-api/main/assets/console.jpg)

---

## 🔍 中转站选购指南

选择 AI API 中转站，看这 6 个维度：

| 维度 | 说明 | 警惕信号 |
|------|------|---------|
| **稳定性** | 是否经常宕机、延迟高 | 频繁断线、无公告 |
| **速度** | 响应延迟是否可接受 | >5s 首 token 延迟 |
| **模型覆盖** | 是否支持最新模型 | 上新慢、缺热门模型 |
| **价格透明** | 计费是否清晰、可查账单 | 无调用记录、不透明 |
| **掺水风险** | 是否用低价模型冒充高价模型 | 价格异常低、效果差 |
| **跑路风险** | 是否公司运营、有售后 | 个人运营、无客服 |

### ⚠️ 避坑清单

1. **缓存价格陷阱**：正常缓存价格应为 10%，部分站收 15%-30%
2. **掺水检测**：用相同 prompt 对比官方和中转站输出，质量差异大 = 掺水
3. **Token 计数造假**：发送已知 token 数请求，检查计费是否虚高
4. **低价陷阱**：价格远低于市场价，大概率用 GLM 冒充 GPT
5. **充值跑路**：不要大额充值！用多少充多少

### 🔬 如何检测中转站是否掺水

```python
# 方法1：能力测试 - 用需要推理的 prompt
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claude 正确答案: 9
# 低端模型经常答错: 8

# 方法2：长上下文测试
# 发送 50K+ token 的长文本，问结尾的细节
# 低端模型会丢失上下文

# 方法3：代码能力测试
prompt = "用 Python 实现一个 LRU 缓存，带 TTL 过期"
# 对比官方和中转站的代码质量
```

---

## 💰 实时模型价格

> 以下价格由 GitHub Actions 自动从 [Levogat API](https://api.levogat.com/api/pricing) 拉取，每小时更新。
> 
> 价格单位：USD / 百万 Token | 出入倍率 = 输出价格 / 输入价格

### OpenAI GPT 系列

<!-- GPT_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 推荐分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
| `gpt-6-astra` | Codex-Gpt-1 | 0.07x | $0.74 | $3.68 | Azure-Gpt-6 | 1.8x | $18.00 | $90.00 | 5x |
| `gpt-5.6-sol` | Codex-Gpt-1 | 0.07x | $0.37 | $2.21 | Azure-Gpt-6 | 1.8x | $9.00 | $54.00 | 6x |
| `gpt-5.6-luna` | Azure-Gpt-2 | 0.2x | $0.04 | $0.24 | Azure-Gpt-6 | 1.8x | $0.36 | $2.16 | 6x |
| `gpt-5.6-terra` | Codex-Gpt-1 | 0.07x | $0.15 | $0.88 | Azure-Gpt-6 | 1.8x | $3.60 | $21.60 | 6x |
| `gpt-5.5` | Codex-Gpt-1 | 0.07x | $0.37 | $2.21 | Azure-Gpt-6 | 1.8x | $9.00 | $54.00 | 6x |
| `gpt-5.5-pro` | Openai-Gpt-1 | 1.18x | $35.29 | $211.77 | Azure-Gpt-6 | 1.8x | $54.00 | $324.00 | 6x |
| `gpt-5.4-pro` | Azure-Gpt-1 | 0.09x | $2.64 | $15.84 | Azure-Gpt-6 | 1.8x | $54.00 | $324.00 | 6x |
| `gpt-5.4-pro-2026-03-05` | Azure-Gpt-2 | 0.2x | $6.00 | $36.00 | Openai-Gpt-2 | 1.47x | $44.12 | $264.71 | 6x |
| `gpt-5.4-mini` | Azure-Gpt-1 | 0.09x | $0.07 | $0.40 | Azure-Gpt-6 | 1.8x | $1.35 | $8.10 | 6x |
| `gpt-5.4-mini-2026-03-17` | Azure-Gpt-1 | 0.09x | $0.07 | $0.40 | Openai-Gpt-2 | 1.47x | $1.10 | $6.62 | 6x |
| `gpt-5.4-nano` | Azure-Gpt-1 | 0.09x | $0.02 | $0.11 | Azure-Gpt-6 | 1.8x | $0.36 | $2.25 | 6.25x |
| `gpt-5.4-nano-2026-03-17` | Azure-Gpt-1 | 0.09x | $0.02 | $0.11 | Openai-Gpt-2 | 1.47x | $0.29 | $1.84 | 6.25x |
| `gpt-5.3-codex` | Azure-Gpt-2 | 0.2x | $0.35 | $2.80 | Openai-Gpt-2 | 1.47x | $2.57 | $20.59 | 8x |
| `gpt-5.2-codex` | Azure-Gpt-2 | 0.2x | $0.35 | $2.80 | Openai-Gpt-2 | 1.47x | $2.57 | $20.59 | 8x |
| `gpt-5.2-chat-latest` | Azure-Gpt-1 | 0.09x | $0.15 | $1.23 | Openai-Gpt-2 | 1.47x | $2.57 | $20.59 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Anthropic Claude 系列

<!-- CLAUDE_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 推荐分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
| `claude-fable-5` | Kiro-Claude-… | 0.18x | $1.76 | $8.82 | AWS-Claude-3 | 2.2x | $22.00 | $110.00 | 5x |
| `claude-fable-5-1` | Kiro-Claude-… | 0.18x | $1.76 | $8.82 | AWS-Claude-3 | 2.2x | $22.00 | $110.00 | 5x |
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

### Google Gemini 系列

<!-- GEMINI_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 推荐分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
| `gemini-3.8-flash` | Anti-Gemini-… | 0.15x | $0.11 | $0.55 | Aistudio-Gem… | 1.91x | $1.43 | $7.17 | 5x |
| `gemini-3.7-flash` | Anti-Gemini-… | 0.15x | $0.11 | $0.55 | Aistudio-Gem… | 1.91x | $1.43 | $7.17 | 5x |
| `gemini-3.6-flash` | Anti-Gemini-… | 0.15x | $0.11 | $0.55 | Aistudio-Gem… | 1.91x | $1.43 | $7.17 | 5x |
| `gemini-3.5-flash` | Anti-Gemini-… | 0.15x | $0.22 | $1.32 | Aistudio-Gem… | 1.91x | $2.87 | $17.21 | 6x |
| `gemini-3.5-flash-lite` | Anti-Gemini-… | 0.15x | $0.04 | $0.37 | Aistudio-Gem… | 1.91x | $0.57 | $4.78 | 8.33x |
| `gemini-3-pro-image` | Aistudio-Gem… | 0.35x | $0.00 | $0.00 | Aistudio-Gem… | 1.91x | $0.00 | $0.00 | 0x |
| `gemini-3-pro-image-preview` | Aistudio-Gem… | 0.35x | $0.00 | $0.00 | Aistudio-Gem… | 1.91x | $0.00 | $0.00 | 0x |
| `gemini-3-pro-preview` | Anti-Gemini-… | 0.15x | $0.29 | $1.76 | Aistudio-Gem… | 1.91x | $3.82 | $22.94 | 6x |

<!-- GEMINI_PRICE_TABLE_END -->

### DeepSeek 系列

<!-- DEEPSEEK_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 推荐分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
| `deepseek-v4.1-flash` | Self-Deploye… | 1x | $0.30 | $1.20 | Self-Deploye… | 1.5x | $0.45 | $1.80 | 4x |
| `deepseek-v4-pro` | Self-Deploye… | 1x | $1.32 | $3.96 | deepseek-1 | 2.2x | $2.90 | $8.71 | 3x |
| `deepseek-v4-pro-0813` | Self-Deploye… | 1x | $1.32 | $3.96 | deepseek-1 | 2.2x | $2.90 | $8.71 | 3x |
| `deepseek-v4-flash` | Self-Deploye… | 1x | $0.44 | $1.32 | deepseek-1 | 2.2x | $0.97 | $2.90 | 3x |
| `deepseek-v4-flash-0731` | Self-Deploye… | 1x | $0.44 | $1.32 | deepseek-1 | 2.2x | $0.97 | $2.90 | 3x |
| `deepseek-v3.2` | Alibaba-1 | 1x | $0.29 | $0.43 | Alibaba-3 | 2.2x | $0.64 | $0.96 | 1.5x |
| `deepseek-v3.2-exp` | Alibaba-1 | 1x | $0.29 | $0.43 | Alibaba-3 | 2.2x | $0.64 | $0.96 | 1.5x |
| `deepseek-v3.1` | Self-Deploye… | 0.6x | $0.35 | $1.04 | Alibaba-3 | 2.2x | $1.28 | $3.83 | 3x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### xAI Grok 系列

<!-- GROK_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 推荐分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
| `grok-4.6` | Cli-Grok-1 | 0.15x | $0.29 | $0.88 | Xai-Grok-1 | 0.88x | $1.76 | $5.29 | 3x |
| `grok-4.5` | Cli-Grok-1 | 0.15x | $0.29 | $0.88 | Xai-Grok-1 | 0.88x | $1.76 | $5.29 | 3x |
| `grok-4.3` | Azure-Grok-1 | 0.15x | $0.18 | $0.37 | Xai-Grok-1 | 0.88x | $1.10 | $2.21 | 2x |
| `grok-4-20-non-reasoning` | Cli-Grok-1 | 0.15x | $0.18 | $0.37 | Xai-Grok-1 | 0.88x | $1.10 | $2.21 | 2x |
| `grok-4-20-reasoning` | Cli-Grok-1 | 0.15x | $0.18 | $0.37 | Xai-Grok-1 | 0.88x | $1.10 | $2.21 | 2x |
| `grok-4` | Azure-Grok-1 | 0.15x | $0.44 | $2.21 | Azure-Grok-2 | 0.22x | $0.66 | $3.31 | 5x |

<!-- GROK_PRICE_TABLE_END -->

### 国产模型（通义/豆包/智谱/Kimi/MiniMax）

<!-- CN_MODEL_PRICE_TABLE_START -->
| 模型 | 最低价分组 | 倍率 | 输入($/M) | 输出($/M) | 推荐分组 | 倍率 | 输入($/M) | 输出($/M) | 出入比 |
|------|-----------|------|-----------|-----------|---------|------|-----------|-----------|--------|
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

> 💡 完整价格请前往 [Levogat AI 定价页面](https://api.levogat.com/pricing) 查看，支持 81 个分组、366 个模型、数千种价格组合。

### 分组说明

| 分组类型 | 倍率范围 | 适合场景 |
|---------|---------|---------|
| 限时特价 | 0.6x | 测试、低成本场景 |
| Codex 专属 | 0.8x | GPT 编程、日常使用 |
| default | 1.0x | 标准质量、平衡选择 |
| anti/kiro | 1.2x | 性价比 Claude |
| Claude Code 专属 | 2.4x | Claude Code 编程 |
| Azure 渠道 | 3.0x | 稳定 GPT |
| AWS 企业级 | 4.0x | 企业级 Claude |
| Vertex/官方直连 | 6.0x | 最高质量 |
| 正价官转 | 16.0x | 完全官方品质 |

---

## 🛠️ 接入教程

### 快速开始

1. 前往 [Levogat AI](https://api.levogat.com) -> 注册 -> 控制台创建 Key
2. 充值（最低 1 元起充）
   - 支付宝支付 / 微信支付 / 加密货币支付 / 信用卡 / Stripe
3. 选择代码示例接入：

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
    messages=[{"role": "user", "content": "用Python写一个快速排序"}]
)

# Claude Sonnet 5
resp = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": "解释量子计算"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# DeepSeek V4
resp = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "用Python实现一个web服务器"}]
)
```

### Node.js / curl

```bash
curl https://api.levogat.com/v1/chat/completions \
  -H "Authorization: Bearer 你的API Key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

完整示例见 [examples/](./examples/) 目录（含 [Python](examples/quickstart.py) / [Node.js](examples/quickstart.js) / [Shell](examples/quickstart.sh)）。

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="你的API Key"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

📖 详细教程见 [Claude Code 接入教程](docs/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex

export OPENAI_API_KEY="你的API Key"
export OPENAI_API_BASE="https://api.levogat.com/v1"
```

📖 详细教程见 [Codex 接入教程](docs/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli

export GEMINI_API_KEY="你的API Key"
export GEMINI_API_BASE="https://api.levogat.com/v1"
```

📖 详细教程见 [Cursor IDE 配置教程](docs/cursor-setup.md)（同样适用于 Gemini CLI 配置）

### 工具集成

| 工具 | 配置方式 |
|------|---------|
| Dify / FastGPT | API 设置填入 Key + Base URL: `https://api.levogat.com/v1` |
| n8n | HTTP Request -> URL: `https://api.levogat.com/v1/chat/completions` |
| LangChain | `ChatOpenAI(openai_api_key="Key", openai_api_base="https://api.levogat.com/v1")` |
| NextChat | 设置 -> 自定义 API -> URL: `https://api.levogat.com/v1` |
| OpenClaw | `openai_api_key: Key` + `openai_api_base: https://api.levogat.com/v1` |

### 使用场景

- **AI 编程** - Claude Code / Codex 配置后，直接用 Claude Opus 5 / GPT-5.6 做代码重构、Bug 修复
- **长文本处理** - 10 万字文档分析、合同审核、论文总结
- **自动化 Agent** - 一个 Key 调度所有模型，支持多 Agent 并行
- **RAG 知识库** - DeepSeek / GPT 对接向量数据库，企业知识库问答
- **自动化工作流** - n8n / FastGPT / Dify 接入，全流程自动化

---

## 📊 2026 年竞品对比评测

> 数据基于 2026-07-29 公开信息整理，仅供参考。

| 维度 | levogat AI | OpenRouter | 硅基流动 | 神马中转 | 自建代理 |
|------|------------|-----------|---------|---------|---------|
| 模型数量 | **366** | ~400 | ~200 | ~100 | 需手动维护 |
| 分组选择 | **81 个分组** | 无（按供应商定价） | 无分组 | 1-3 个 | - |
| 国内 CDN 加速 | ✅ 多节点 | ❌ 无国内节点 | ✅ 单节点 | ✅ | ❌ |
| 最低充值 | **¥1** | ~¥35 | ¥50 | ¥20 | - |
| 按量计费 | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code 兼容 | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI 格式 | ✅ | ✅ | ✅ | ✅ | 需适配 |
| 价格透明 | ✅ 33 分组可选 | 按供应商，可选少 | 单一价格 | 单一价格 | - |
| GitHub 开源 | ✅ 价格自动更新 | ❌ | ❌ | ❌ | - |

---

## ❓ FAQ

**响应内容和官方一致吗？**

高度一致。levogat AI 仅做请求转发，底层调用官方模型，响应内容与官方 API 保持一致。

**会被封号吗？**

不会。你使用的是 levogat AI 的 Key，不走官方账号体系，不涉及你的官方账号封禁风险。

**不同分组有什么区别？**

不同分组对应不同的后端渠道（Azure/AWS/Vertex/官方直连等），质量和价格不同。低价分组性价比高，高价分组质量最稳定。建议先用 default 分组测试，再根据需求调整。

**支持 streaming 吗？**

支持，所有模型均支持流式输出，延迟低，实时性好。

**国内访问速度如何？**

采用国内 CDN 节点加速，延迟通常在 40-200ms，远低于直连官方的数百毫秒。

**有免费额度吗？**

新用户注册赠送体验额度，可先试用再决定是否充值。



**如何选择分组？**

- 省钱：限时特价(0.6x) / Codex专属(0.8x)
- 平衡：default(1.0x)
- 高质量：Claude Code专属(2.4x) / Azure(3.0x)
- 最高质量：Vertex(6.0x) / 正价官转(16.0x)

---

## 📖 深入教程

| 教程 | 内容 |
|------|------|
| [Claude Code 接入教程](docs/claude-code-guide.md) | 国内使用 Claude Code 的完整配置方案 |
| [Claude Desktop 接入教程](docs/claude-desktop-guide.md) | Claude Desktop 桌面应用配置 levogat AI |
| [Codex 接入教程](docs/codex-setup.md) | OpenAI Codex CLI 国内配置方法 |
| [Gemini CLI 接入教程](docs/gemini-cli-guide.md) | Gemini CLI 配置 levogat AI 调用 Gemini 模型 |
| [Cursor IDE 配置教程](docs/cursor-setup.md) | Cursor 中接入 GPT-5.6 / Claude Opus 5 / Gemini |
| [Grok Build 接入教程](docs/grok-build-guide.md) | xAI Grok Build 配置自定义模型接入 levogat AI |
| [OpenCode 接入教程](docs/opencode-guide.md) | OpenCode 开源编程助手配置 levogat AI |
| [OpenClaw 接入教程](docs/openclaw-guide.md) | OpenClaw Agent 运行时配置 levogat AI |
| [CC Switch 接入教程](docs/cc-switch-guide.md) | 统一管理多个 AI 工具的 levogat AI 配置 |
| [Dify 接入教程](docs/dify-integration.md) | Dify 对接 levogat AI 完整流程 |
| [模型选择指南](docs/model-selection-guide.md) | 366 个模型怎么选？按场景/预算推荐 |
| [中转站掺水检测指南](docs/fraud-detection-guide.md) | 5 种方法检测中转站是否用低端模型冒充 |
| [成本计算器使用指南](docs/cost-calculator-guide.md) | 估算 API 调用成本，优化开支 |

---

## 🤝 贡献

- 🐛 发现 Bug -> 提交 [Issue](https://github.com/jiaqing77cn/levogat-ai-api/issues)
- 📝 优化文档 -> 直接提交 PR
- 💡 新功能建议 -> 发起 [Discussion](https://github.com/jiaqing77cn/levogat-ai-api/discussions)
- 📄 贡献指南 -> 见 [CONTRIBUTING.md](./CONTRIBUTING.md)
- 📋 更新日志 -> 见 [CHANGELOG.md](./CHANGELOG.md)

---

## License

MIT License · Copyright (c) 2026 [Levogat AI](https://api.levogat.com)

## 📢 商标声明

GPT、OpenAI 是 OpenAI 的商标。Claude 是 Anthropic PBC 的商标。Gemini 是 Google LLC 的商标。DeepSeek 是 DeepSeek 的商标。本仓库仅描述兼容性，不暗示与上述公司的官方关联或背书。
