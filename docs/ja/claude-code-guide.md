# Claude Code サードパーティAPI設定チュートリアル（国内直結）

> 中国国内でClaude CodeにサードパーティAPIキーを設定する完全ガイド：VPN不要、低遅延、Claude Opus 5 / Sonnet 5対応。5分で完了。

## Claude Code とは

Claude Code は Anthropic が公式提供する AI プログラミングアシスタントです。ターミナルで直接使用でき、コード生成、リファクタリング、バグ修正、テスト作成などをサポートしています。

## 設定手順

### 1. Claude Code のインストール

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. 環境変数の設定

```bash
# ~/.bash_profile または ~/.zshrc に追加
export ANTHROPIC_AUTH_TOKEN="あなたの Levogat API Key"
export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"

# 反映
source ~/.bash_profile
```

### 3. 使い始める

```bash
cd your-project
claude
```

## 推奨グループ

| グループ | 倍率 | 適したシーン |
|------|------|---------|
| デフォルト(Azure+MJ) | 1.0x | 日常使用、コスパ良好 |
| CC 専用 | 2.4x | Claude Code 専用最適化、最も安定 |
| anti/kiro | 1.2x | コスパ重視 |

## よくある質問

### Q: Claude Code で "authentication failed" エラーが出る

環境変数が正しく設定されているか確認してください：
```bash
echo $ANTHROPIC_AUTH_TOKEN
echo $ANTHROPIC_BASE_URL
```

### Q: レスポンスが遅い

グループの切り替えを試してください。CC 専用グループは Claude Code 向けに最適化されており、より高速です。

### Q: Claude Opus 4.8 に対応していますか

対応しています。Claude Code で `/model` と入力すればモデルを切り替えられます。

## 関連リンク

- [Levogat AI 公式サイト](https://api.levogat.com)
- [Claude Code 公式ドキュメント](https://docs.anthropic.com/en/docs/claude-code)
- [API ドキュメント](https://levogat.apifox.cn/)
