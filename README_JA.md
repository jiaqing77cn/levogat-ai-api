<h1 align="center">🚀 中国AI APIプロキシ | VPN不要でClaude/GPT/Gemini/DeepSeekに直接接続 | Levogat AI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/500%2B-Models-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-China%20Accel-3b82f6?style=flat" alt="CDN"/>
  <img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat" alt="OpenAI Compatible"/>
</p>

<div align="center">

**VPN不要 · 低レイテンシ · 500以上のモデル · OpenAI Compatible · Claude Code対応**

[🌐 公式サイト](https://api.levogat.com) · [📋 料金](https://api.levogat.com/pricing) · [📖 APIドキュメント](https://levogat.apifox.cn/) · [💬 お問い合わせ](https://api.levogat.com)

</div>

> Last updated: 2026-09-18 05:11 (UTC+8)| [中文](./README.md) | [English](./README_EN.md) | [한국어](./README_KO.md) | 日本語 | [Español](./README_ES.md) | [Deutsch](./README_DE.md)

---

## 📋 目次

- [🖥️ プロダクトプレビュー](#-プロダクトプレビュー)
- [🔍 APIプロキシの選び方](#-apiプロキシの選び方)
- [💰 リアルタイムモデル料金](#-リアルタイムモデル料金)
- [🛠️ 統合ガイド](#-統合ガイド)
- [📊 比較](#-比較)
- [❓ FAQ](#-faq)
- [📖 詳細ガイド](#-詳細ガイド)
- [🤝 コントリビュート](#-コントリビュート)

---

## 🖥️ プロダクトプレビュー

![Levogat AI ホームページ - 500以上のAIモデルAPIプロキシダッシュボード](https://raw.githubusercontent.com/jiaqing77cn/levogat-ai-api/main/assets/homepage.jpg)

![Levogat AI コンソール - APIキー作成、使用量確認、アカウントチャージ](https://raw.githubusercontent.com/jiaqing77cn/levogat-ai-api/main/assets/console.jpg)

---

## 🔍 APIプロキシの選び方

AI APIプロキシを選ぶ際に評価すべき6つの評価軸：

| 評価軸 | 確認ポイント | 危険信号 |
|-----------|--------------|-----------|
| **安定性** | 頻繁にダウンする？レイテンシが高い？ | 切断、告知なし |
| **速度** | レスポンスレイテンシは許容範囲？ | 初回トークンまで5秒以上 |
| **モデルカバレッジ** | 最新モデルが利用可能？ | 新モデル追加が遅い |
| **価格透明性** | 課金が明確？使用ログあり？ | 呼出記録なし、不透明 |
| **モデルすり替え** | 安価なモデルを高級モデルとして偽装？ | 異常に安い、品質が低い |
| **退出リスク** | 企業運営？サポートあり？ | 個人運営、カスタマーサポートなし |

### ⚠️ 落とし穴チェックリスト

1. **キャッシュ価格の罠**：通常のキャッシュ価格は10%、一部は15%-30%を請求する
2. **モデルすり替え検出**：同じプロンプトで公式とプロキシの出力を比較する
3. **トークン数不正**：既知のトークン数でリクエストを送信し、課金が水増しされていないか確認する
4. **低価格の罠**：市場価格を大幅に下回る価格は、GLMがGPTを偽装している可能性が高い
5. **退出詐欺リスク**：大額入金しないこと！従量課金で利用する

### 🔬 モデルすり替えの検出方法

```python
# 方法1：能力テスト - 推論プロンプトを使用
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claudeの正解：9
# 低品質モデルは多くの場合間違える：8

# 方法2：長文コンテキストテスト
# 50K+トークンの長文を送信し、末尾の詳細について質問する
# 低品質モデルはコンテキストを見失う

# 方法3：コード能力テスト
prompt = "Implement an LRU cache with TTL expiration in Python"
# 公式とプロキシのコード品質を比較する
```

---

## 💰 リアルタイムモデル料金

> 価格はGitHub Actionsにより[Levogat API](https://api.levogat.com/api/pricing)から自動取得され、毎時更新されます。
>
> 単位：USD / Million Tokens | 出力/入力比 = 出力価格 ÷ 入力価格

### OpenAI GPTシリーズ

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

### Anthropic Claudeシリーズ

<!-- CLAUDE_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
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

### Google Geminiシリーズ

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

### DeepSeekシリーズ

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

### xAI Grokシリーズ

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

### 中国製モデル（Qwen/Doubao/GLM/Kimi/MiniMax）

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

> 💡 全81グループ・366モデルの完全な料金表は[Levogat AI 料金ページ](https://api.levogat.com/pricing)でご確認ください。

### グループティア

| グループタイプ | 倍率 | 最適な用途 |
|------------|-------|----------|
| フラッシュセール | 0.6x | テスト、低コスト利用 |
| Codex专属 | 0.8x | GPTコーディング、日常利用 |
| デフォルト | 1.0x | 標準品質、バランス型 |
| anti/kiro | 1.2x | コスト重視のClaude利用 |
| Claude Code専属 | 2.4x | Claude Codeプログラミング |
| Azureチャネル | 3.0x | 安定性重視のGPT |
| AWSエンタープライズ | 4.0x | エンタープライズ級Claude |
| Vertex/ダイレクト | 6.0x | 最高品質 |
| 公式プレミアム | 16.0x | 完全な公式品質 |

---

## 🛠️ 統合ガイド

### クイックスタート

1. [Levogat AI](https://api.levogat.com)にアクセス -> 新規登録 -> コンソール -> キー作成
2. チャージ（最低1元）
   - Alipay / WeChat Pay / Crypto Pay / クレジットカード / Stripe
3. 統合方法を選択：

### Python（OpenAI SDK）

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

完全なサンプルは[`examples/`](./examples/)ディレクトリをご覧ください（[Python](examples/quickstart.py) / [Node.js](examples/quickstart.js) / [Shell](examples/quickstart.sh)を含む）。

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="***"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

📖 完全ガイド：[Claude Code セットアップ](docs/ja/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://api.levogat.com/v1"
```

📖 完全ガイド：[Codex セットアップ](docs/ja/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://api.levogat.com/v1"
```

📖 完全ガイド：[Cursor IDE セットアップ](docs/ja/cursor-setup.md)（Gemini CLIにも適用）

### ツール統合

| ツール | 設定方法 |
|------|-------|
| **Dify / FastGPT** | API Key + Base URL: `https://api.levogat.com/v1` |
| **n8n** | HTTP Request -> URL: `https://api.levogat.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://api.levogat.com/v1")` |
| **NextChat** | 設定 -> カスタムAPI -> URL: `https://api.levogat.com/v1` |
| **Cursor IDE** | 設定 -> 環境変数 -> `ANTHROPIC_BASE_URL=https://api.levogat.com/v1` |
| **OpenClaw** | `openai_api_key: key` + `openai_api_base: https://api.levogat.com/v1` |

### ユースケース

- **AIコーディング** - Claude Code / CodexでClaude Opus 5 / GPT-5.6を使用し、リファクタリングやバグ修正
- **長文処理** - 10万字以上の文書分析、契約書レビュー、論文要約
- **AIエージェント** - 1つのキーで全モデルにアクセス、マルチエージェント並列タスク
- **RAGナレッジベース** - DeepSeek / GPTとベクトルデータベースでエンタープライズQ&A
- **自動化ワークフロー** - n8n / FastGPT / Dify統合でフルオートメーション

---

## 📊 2026年 比較・レビュー

> 2026-07-29時点の公開情報に基づきます。参考用です。

| | [Levogat AI](https://api.levogat.com) | OpenRouter | SiliconFlow | その他プロキシ | セルフビルド |
|--|-------------|-----------|-------------|---------------|------------|
| モデル数 | **366** | ~400 | 約200 | 約100 | 手動 |
| グループ選択肢 | **81グループ** | なし（プロバイダー別） | なし | 1-3 | - |
| 中国CDN | ✅ マルチノード | ❌ 中国ノードなし | ✅ 単一 | ✅ | ❌ |
| 最低チャージ | **¥1** | ~¥35 | ¥50 | ¥20 | - |
| 従量課金 | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code対応 | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI互換 | ✅ | ✅ | ✅ | ✅ | アダプター必要 |
| 価格透明性 | ✅ 81グループ | モデル別、選択制限 | 単一価格 | 単一価格 | - |
| GitHubオープンソース | ✅ 自動価格更新 | ❌ | ❌ | ❌ | - |

---

## ❓ FAQ

**公式APIと同じレスポンスですか？**

はい。Levogat AIは公式モデルへのリクエストを転送するだけです。レスポンスは公式APIと一致しています。

**アカウントがBANされるリスクはありますか？**

いいえ。Levogat AIのキーを使用するため、公式アカウントシステムには関与しません。公式アカウントが停止されるリスクはありません。

**グループ間の違いは何ですか？**

グループによってバックエンドチャネル（Azure/AWS/Vertex/公式ダイレクトなど）が異なり、品質と価格が異なります。低コストグループはコストパフォーマンスに優れ、高価格グループは最大の安定性を提供します。まずデフォルトグループから始め、必要に応じて調整してください。

**streamingに対応していますか？**

はい、全モデルで`stream: true`に対応しており、低レイテンシで利用できます。

**中国からの速度はどのくらいですか？**

中国CDNノードを使用し、レイテンシは通常40-200msです。公式APIに直接接続するよりはるかに高速です。

**無料枠はありますか？**

新規ユーザーにはトライアルクレジットが付与されます。無料で開始し、必要に応じてチャージしてください。

**どのグループを選ぶべきですか？**

- コスト重視：フラッシュセール（0.6x）/ Codex专属（0.8x）
- バランス型：デフォルト（1.0x）
- 高品質：Claude Code専属（2.4x）/ Azure（3.0x）
- 最高品質：Vertex（6.0x）/ 公式プレミアム（16.0x）

---

## 📖 詳細ガイド

| ガイド | 内容 |
|-------|---------|
| [Claude Code セットアップガイド](docs/ja/claude-code-guide.md) | 中国向けClaude Codeの完全設定 |
| [Claude Desktop ガイド](docs/ja/claude-desktop-guide.md) | Claude DesktopにLevogat AIを設定 |
| [Codex セットアップガイド](docs/ja/codex-setup.md) | 中国向けOpenAI Codex CLI設定 |
| [Gemini CLI ガイド](docs/ja/gemini-cli-guide.md) | Gemini CLIでLevogat AI経由でGeminiモデルを使用 |
| [Cursor IDE セットアップ](docs/ja/cursor-setup.md) | CursorでGPT-5.6 / Claude Opus 5 / Geminiを使用 |
| [Grok Build ガイド](docs/ja/grok-build-guide.md) | xAI Grok BuildにLevogat AIカスタムモデルを設定 |
| [OpenCode ガイド](docs/ja/opencode-guide.md) | OpenCodeオープンソースエージェントにLevogat AIを設定 |
| [OpenClaw ガイド](docs/ja/openclaw-guide.md) | OpenClaw AgentランタイムにLevogat AIを設定 |
| [CC Switch ガイド](docs/ja/cc-switch-guide.md) | 複数AIツールのLevogat AI設定を統合管理 |
| [Dify 統合ガイド](docs/ja/dify-integration.md) | DifyとLevogat AIの連携 |
| [モデル選択ガイド](docs/ja/model-selection-guide.md) | 366モデルからどれを選ぶ？用途と予算別 |
| [詐欺検出ガイド](docs/ja/fraud-detection-guide.md) | APIプロキシでモデルすり替えを検出する5つの方法 |
| [コスト計算ガイド](docs/ja/cost-calculator-guide.md) | APIコストの見積もりと最適化 |

---

## 🤝 コントリビュート

- 🐛 バグ報告 -> [Issueを開く](https://github.com/jiaqing77cn/levogat-ai-api/issues)
- 📝 ドキュメント改善 -> PRを提出
- 💡 機能要望 -> [Discussionを開始](https://github.com/jiaqing77cn/levogat-ai-api/discussions)
- 📄 コントリビュートガイド -> [CONTRIBUTING.md](./CONTRIBUTING.md)を参照
- 📋 変更履歴 -> [CHANGELOG.md](./CHANGELOG.md)を参照

---

## 📜 ライセンス

MIT License · Copyright (c) 2026 [Levogat AI](https://api.levogat.com)

## 📢 商標表示

GPTおよびOpenAIはOpenAIの商標です。ClaudeはAnthropic PBCの商標です。GeminiはGoogle LLCの商標です。DeepSeekはDeepSeekの商標です。このリポジトリは互換性の説明のみを目的としており、これらの企業との公式な提携や承認を意味するものではありません。
