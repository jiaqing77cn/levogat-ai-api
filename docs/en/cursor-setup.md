# Cursor API Setup Guide: Configure Third-Party API in China

> Complete guide to configuring a relay API in Cursor — supports Claude Opus 5, GPT-6, DeepSeek V4. Direct access in China.

> 👉 **Get your API Key**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=cursor-setup&utm_campaign=docs-funnel) (free trial credits — Alipay/WeChat/crypto accepted)

## Configuration Steps

### 1. Open Cursor Settings

`Cmd/Ctrl + ,` -> Search for "OpenAI" -> Find "OpenAI API Key"

### 2. Fill in Configuration

- **API Key**: Your Levogat API Key
- **Base URL**: `https://api.levogat.com/v1`

### 3. Modify ~/.cursor/settings.json

```json
{
  "openai.apiKey": "your Levogat API Key",
  "openai.baseUrl": "https://api.levogat.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. Using Claude Models

Enter a custom model name in Cursor's model selector:
- `claude-sonnet-4-6` - Daily coding
- `claude-opus-4-8` - Complex tasks
- `gpt-5.6-sol` - GPT coding

## Recommended Configuration

| Use Case | Model | Group |
|----------|-------|-------|
| Code completion | gpt-5.6-luna | Codex Dedicated (0.8x) |
| Chat | claude-sonnet-4-6 | Default (1.0x) |
| Complex refactoring | claude-opus-4-8 | CC Dedicated (2.4x) |
