# OpenClaw接続チュートリアル：中国国内AI APIの設定

> OpenClaw で Levogat AI をバックエンドモデルプロバイダーとして使用します。

> 👉 **API Keyを取得**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=openclaw-guide&utm_campaign=docs-funnel) (登録で無料トライアルクレジット、Alipay/WeChatでチャージ可)

## OpenClaw とは

OpenClaw はオープンソースの AI Agent ランタイムで、マルチモデルスケジューリング、スキルシステム、定期タスク、メモリシステムなどをサポートしています。OpenAI 互換の API エンドポイントを設定することで、Levogat AI を連携できます。

## 設定手順

### 1. OpenClaw のインストール

```bash
# npm でインストール
npm install -g openclaw

# または Docker を使用
docker run -d openclaw/openclaw
```

### 2. Gateway の設定

OpenClaw の Gateway 設定ファイル（通常は `~/.openclaw/config.yaml` またはプロジェクトディレクトリの `config.yaml`）を編集：

```yaml
# モデル設定
model:
  # デフォルトモデル
  default: volces/glm-5.2

  # OpenAI 互換プロバイダー
  providers:
    - name: levogat
      api_key: "あなたの Levogat API Key"
      base_url: "https://api.levogat.com/v1"
      models:
        - gpt-5.6-sol
        - gpt-5.6-luna
        - claude-sonnet-4-6
        - claude-opus-4-8
        - gemini-2.5-pro
        - deepseek-reasoner
```

### 3. または環境変数で設定

```bash
# ~/.bash_profile または ~/.zshrc に追加
export OPENAI_API_KEY="あなたの Levogat API Key"
export OPENAI_API_BASE="https://api.levogat.com/v1"

source ~/.bash_profile
```

### 4. OpenClaw の起動

```bash
openclaw gateway start

# 状態確認
openclaw status
```

## 推奨モデル設定

| 用途 | モデル | グループ推奨 |
|------|------|---------|
| Agent 日常タスク | `gpt-5.6-luna` | Codex 専用 (0.8x) |
| 複雑な推論 | `claude-opus-4-8` | デフォルト (1.0x) |
| プログラミングタスク | `claude-sonnet-4-6` | デフォルト (1.0x) |
| 長文処理 | `gemini-2.5-pro` | gemini-cli (1.0x) |
| コストパフォーマンス | `deepseek-reasoner` | 期間限定特価 (0.6x) |

## セッションモデルの切り替え

OpenClaw はセッションごとに異なるモデルを指定できます：

```bash
# セッション内でモデルを切り替え
/model claude-opus-4-8

# 現在のモデルを確認
/status
```

## マルチモデルスケジューリング

OpenClaw は複数モデルの同時スケジューリングに対応しており、Agent の並列タスクに最適です：

```yaml
# 複数の provider を同時に使用する設定
model:
  providers:
    - name: levogat-gpt
      api_key: "あなたのKey"
      base_url: "https://api.levogat.com/v1"
    - name: levogat-claude
      api_key: "あなたのKey"
      base_url: "https://api.levogat.com/v1"
```

## よくある質問

### Q: OpenClaw で "model not available" エラーが出る

Gateway が起動しているか、モデル名が正しいか確認してください：

```bash
openclaw status
openclaw models list
```

### Q: デフォルトモデルの設定方法

設定ファイルで `model.default` を設定するか、セッション内で `/model` コマンドを使用してください。

### Q: ストリーミング出力に対応していますか

対応しています。OpenClaw はデフォルトでストリーミング出力を使用します。

### Q: コストを抑える方法

1. 期間限定特価グループ（0.6x 倍率）を使用
2. タスクに適したモデルを選択
3. 設定でトークン制限を設定

## 関連リンク

- [Levogat AI 公式サイト](https://api.levogat.com)
- [OpenClaw 公式ドキュメント](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [API ドキュメント](https://levogat.apifox.cn/)
- [モデル選択ガイド](./model-selection-guide.md)
