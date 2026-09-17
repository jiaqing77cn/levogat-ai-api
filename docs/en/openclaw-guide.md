# OpenClaw Setup Guide: Configure AI API in China

> Use Levogat AI as the backend model provider for OpenClaw.

> 👉 **Get your API Key**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=openclaw-guide&utm_campaign=docs-funnel) (free trial credits — Alipay/WeChat/crypto accepted)

## What is OpenClaw

OpenClaw is an open-source AI Agent runtime that supports multi-model scheduling, a skill system, scheduled tasks, a memory system, and more. By configuring an OpenAI-compatible API endpoint, you can connect it to Levogat AI.

## Configuration Steps

### 1. Install OpenClaw

```bash
# Install via npm
npm install -g openclaw

# Or using Docker
docker run -d openclaw/openclaw
```

### 2. Configure Gateway

Edit OpenClaw's Gateway configuration file (typically at `~/.openclaw/config.yaml` or `config.yaml` in the project directory):

```yaml
# Model configuration
model:
  # Default model
  default: volces/glm-5.2

  # OpenAI-compatible provider
  providers:
    - name: levogat
      api_key: "your Levogat API Key"
      base_url: "https://api.levogat.com/v1"
      models:
        - gpt-5.6-sol
        - gpt-5.6-luna
        - claude-sonnet-4-6
        - claude-opus-4-8
        - gemini-2.5-pro
        - deepseek-reasoner
```

### 3. Or Configure via Environment Variables

```bash
# Add to ~/.bash_profile or ~/.zshrc
export OPENAI_API_KEY="your Levogat API Key"
export OPENAI_API_BASE="https://api.levogat.com/v1"

source ~/.bash_profile
```

### 4. Start OpenClaw

```bash
openclaw gateway start

# Check status
openclaw status
```

## Recommended Model Configuration

| Use Case | Model | Group Suggestion |
|----------|-------|-----------------|
| Agent daily tasks | `gpt-5.6-luna` | Codex Exclusive (0.8x) |
| Complex reasoning | `claude-opus-4-8` | Default (1.0x) |
| Coding tasks | `claude-sonnet-4-6` | Default (1.0x) |
| Long context processing | `gemini-2.5-pro` | gemini-cli (1.0x) |
| Best value | `deepseek-reasoner` | Limited-time discount (0.6x) |

## Session Model Switching

OpenClaw supports specifying different models for different sessions:

```bash
# Switch model in a session
/model claude-opus-4-8

# View current model
/status
```

## Multi-Model Scheduling

OpenClaw supports scheduling multiple models simultaneously, ideal for Agent parallel tasks:

```yaml
# Configure multiple providers to use simultaneously
model:
  providers:
    - name: levogat-gpt
      api_key: "your-key"
      base_url: "https://api.levogat.com/v1"
    - name: levogat-claude
      api_key: "your-key"
      base_url: "https://api.levogat.com/v1"
```

## FAQ

### Q: OpenClaw reports "model not available"

Check that the Gateway is running and the model name is correct:

```bash
openclaw status
openclaw models list
```

### Q: How do I set the default model?

Set `model.default` in the configuration file, or use the `/model` command in a session.

### Q: Does it support streaming output?

Yes. OpenClaw uses streaming output by default.

### Q: How do I control costs?

1. Use the limited-time discount group (0.6x rate)
2. Choose appropriate models for different tasks
3. Set token limits in the configuration

## Related Links

- [Levogat AI Official Site](https://api.levogat.com)
- [OpenClaw Official Documentation](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [API Documentation](https://levogat.apifox.cn/)
- [Model Selection Guide](./model-selection-guide.md)
