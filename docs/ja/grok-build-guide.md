# Grok Build接続チュートリアル：Grok API中継設定

> Grok Build で Levogat AI 経由で GPT/Claude/Gemini などのモデルを呼び出します。

> 👉 **API Keyを取得**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=grok-build-guide&utm_campaign=docs-funnel) (登録で無料トライアルクレジット、Alipay/WeChatでチャージ可)

## Grok Build とは

Grok Build は xAI が提供するターミナル AI プログラミングアシスタントで、インタラクティブ TUI、ヘッドレスモード、ACP プロトコルをサポートしています。カスタムモデル設定により、Grok Build から Levogat AI 上の任意のモデルを呼び出すことができます。

## 設定手順

### 1. Grok Build のインストール

**macOS / Linux：**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash

> ⚠️ インストール前にスクリプト内容を確認することを推奨: curl -fsSL https://x.ai/cli/install.sh | less
```

**Windows (PowerShell)：**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. カスタムモデルの設定

`~/.grok/config.toml` を編集（Windows: `%USERPROFILE%\.grok\config.toml`）：

```toml
# Levogat AI をバックエンドとして使用
[model.levogat-gpt]
model = "gpt-5.6-sol"
base_url = "https://api.levogat.com/v1"
name = "GPT-5.6 Sol (Levogat)"
env_key = "LEVOGAT_API_KEY"

[model.levogat-claude]
model = "claude-sonnet-4-6"
base_url = "https://api.levogat.com/v1"
name = "Claude Sonnet 4.6 (Levogat)"
env_key = "LEVOGAT_API_KEY"

[model.levogat-gemini]
model = "gemini-2.5-pro"
base_url = "https://api.levogat.com/v1"
name = "Gemini 2.5 Pro (Levogat)"
env_key = "LEVOGAT_API_KEY"

[models]
default = "levogat-gpt"
```

### 3. API Key の設定

```bash
export LEVOGAT_API_KEY="あなたの Levogat API Key"
```

### 4. 使い方

```bash
cd your-project
grok
```

TUI で `/model` を使用してモデルを切り替え：

```
/model levogat-claude
```

## 推奨モデル設定

| 用途 | モデル | グループ推奨 |
|------|------|---------|
| 日常プログラミング | `gpt-5.6-luna` | Codex 専用 (0.8x) |
| 複雑なプログラミング | `gpt-5.6-sol` | Codex 専用 (0.8x) |
| 高度な推論 | `claude-opus-4-8` | デフォルト (1.0x) |
| 長文 | `gemini-2.5-pro` | gemini-cli (1.0x) |

## ヘッドレスモード

```bash
# Levogat モデルを使用してタスクを実行
grok -p "Explain this codebase" -m levogat-claude

# JSON 出力
grok -p "Analyze architecture" -m levogat-gpt --output-format streaming-json
```

## よくある質問

### Q: Grok Build 起動時に "model not found" と表示される

`grok inspect` を実行して設定が正しく読み込まれているか確認してください：

```bash
grok inspect
```

### Q: Grok モデルと Levogat モデルを同時に使用できますか？

`config.toml` に xAI 公式モデルと Levogat モデルの両方を追加し、`/model` コマンドで切り替えることができます。

### Q: ストリーミング出力に対応していますか

対応しています。Levogat AI のすべてのモデルがストリーミング出力に対応しています。

## 関連リンク

- [Levogat AI 公式サイト](https://api.levogat.com)
- [Grok Build 公式ドキュメント](https://docs.x.ai/build/overview)
- [Grok Build GitHub](https://github.com/xai-org/grok-build)
- [API ドキュメント](https://levogat.apifox.cn/)
