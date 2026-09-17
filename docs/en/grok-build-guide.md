# Grok Build Setup Guide: Grok API Relay Configuration

> Use Levogat AI with Grok Build to access GPT/Claude/Gemini and other models.

## What is Grok Build

Grok Build is xAI's terminal AI coding assistant, supporting interactive TUI, headless mode, and the ACP protocol. With custom model configuration, Grok Build can call any model available on Levogat AI.

## Configuration Steps

### 1. Install Grok Build

**macOS / Linux:**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash

> ⚠️ Consider reviewing the script before installation: curl -fsSL https://x.ai/cli/install.sh | less
```

**Windows (PowerShell):**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. Configure Custom Models

Edit `~/.grok/config.toml` (Windows: `%USERPROFILE%\.grok\config.toml`):

```toml
# Use Levogat AI as the backend
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

### 3. Set API Key

```bash
export LEVOGAT_API_KEY="your Levogat API Key"
```

### 4. Start Using

```bash
cd your-project
grok
```

Use `/model` in the TUI to switch models:

```
/model levogat-claude
```

## Recommended Model Configuration

| Use Case | Model | Group Suggestion |
|----------|-------|-----------------|
| Daily coding | `gpt-5.6-luna` | Codex Exclusive (0.8x) |
| Complex coding | `gpt-5.6-sol` | Codex Exclusive (0.8x) |
| Deep reasoning | `claude-opus-4-8` | Default (1.0x) |
| Long context | `gemini-2.5-pro` | gemini-cli (1.0x) |

## Headless Mode

```bash
# Execute a task using a Levogat model
grok -p "Explain this codebase" -m levogat-claude

# Output JSON
grok -p "Analyze architecture" -m levogat-gpt --output-format streaming-json
```

## FAQ

### Q: Grok Build shows "model not found" on startup

Run `grok inspect` to check if the configuration is loaded correctly:

```bash
grok inspect
```

### Q: Can I use both Grok models and Levogat models at the same time?

Add both xAI official models and Levogat models in `config.toml`, then switch between them using the `/model` command.

### Q: Does it support streaming output?

Yes. All models on Levogat AI support streaming output.

## Related Links

- [Levogat AI Official Site](https://api.levogat.com)
- [Grok Build Official Documentation](https://docs.x.ai/build/overview)
- [Grok Build GitHub](https://github.com/xai-org/grok-build)
- [API Documentation](https://levogat.apifox.cn/)
