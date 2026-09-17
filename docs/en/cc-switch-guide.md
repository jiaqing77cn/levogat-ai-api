# CC Switch Guide: Switch Claude Code API Providers in One Click

> Use CC Switch to centrally manage Levogat AI configurations for Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw, and other tools.

> 👉 **Get your API Key**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=cc-switch-guide&utm_campaign=docs-funnel) (free trial credits — Alipay/WeChat/crypto accepted)

## What is CC Switch

CC Switch is a cross-platform desktop tool for managing API configurations across multiple AI coding tools. It supports Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build, OpenCode, OpenClaw, and Hermes — letting you switch API providers with one click, no manual config file editing required.

## Installation

### macOS

```bash
# Homebrew
brew install --cask cc-switch
```

### Windows

Download the installer from [ccswitch.io](https://ccswitch.io).

### Linux

Download the AppImage from [GitHub Releases](https://github.com/farion1231/cc-switch/releases).

## Configuring Levogat AI

### 1. Add Provider

Open CC Switch -> click "Add Provider" -> select "Custom":

| Setting | Value |
|---------|-------|
| Name | Levogat AI |
| API Key | your Levogat API Key |
| Base URL | `https://api.levogat.com/v1` |
| Format | OpenAI Compatible |

### 2. Configure Each Tool

CC Switch automatically generates configurations for each tool:

**Claude Code:**
```bash
export ANTHROPIC_AUTH_TOKEN="your-key"
export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"
```

**Codex:**
```bash
export OPENAI_API_KEY="your-key"
export OPENAI_API_BASE="https://api.levogat.com/v1"
```

**Gemini CLI:**
```bash
export GEMINI_API_KEY="your-key"
export GEMINI_API_BASE="https://api.levogat.com/v1"
```

**OpenCode:**
```json
{
  "provider": {
    "levogat": {
      "api_key": "your-key",
      "base_url": "https://api.levogat.com/v1"
    }
  }
}
```

### 3. One-Click Switching

Select the target tool in the CC Switch interface -> select "Levogat AI" -> click "Apply". CC Switch will automatically modify the corresponding tool's configuration file.

## Recommended Configuration

| Tool | Recommended Model | Group |
|------|------------------|-------|
| Claude Code | `claude-sonnet-4-6` | Default (1.0x) |
| Codex | `gpt-5.6-sol` | Codex Exclusive (0.8x) |
| Gemini CLI | `gemini-2.5-pro` | gemini-cli (1.0x) |
| OpenCode | `gpt-5.6-luna` | Codex Exclusive (0.8x) |
| OpenClaw | `claude-opus-4-8` | Default (1.0x) |

## Multi-Provider Management

CC Switch supports configuring multiple providers simultaneously, making it easy to compare and test:

1. Add "Levogat AI - Limited-time discount" (0.6x)
2. Add "Levogat AI - Default" (1.0x)
3. Add "Levogat AI - CC Exclusive" (2.4x)

Switch between them with one click in the interface — no need to modify code or environment variables.

## FAQ

### Q: The tool doesn't pick up changes after CC Switch modifies the config

Make sure the target tool has been fully quit and restarted. Claude Code requires re-sourcing environment variables.

### Q: Can I configure different providers for different tools at the same time?

Yes. CC Switch can independently configure providers and models for each tool.

### Q: Is CC Switch free?

CC Switch is an open-source tool and is free to use.

## Related Links

- [Levogat AI Official Site](https://api.levogat.com)
- [CC Switch Official Site](https://ccswitch.io)
- [CC Switch GitHub](https://github.com/farion1231/cc-switch)
- [API Documentation](https://levogat.apifox.cn/)
