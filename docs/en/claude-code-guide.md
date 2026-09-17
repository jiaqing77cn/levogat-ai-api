# Claude Code Third-Party API Setup Guide (China)

> The complete guide to configuring Claude Code with a third-party API key in China — no VPN, low latency, supports Claude Opus 5 / Sonnet 5. Done in 5 minutes.

> 👉 **Get your API Key**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=claude-code-guide&utm_campaign=docs-funnel) (free trial credits — Alipay/WeChat/crypto accepted)

## What is Claude Code

Claude Code is an official AI programming assistant from Anthropic. It runs directly in the terminal and supports code generation, refactoring, bug fixing, test writing, and more.

## Configuration Steps

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Configure Environment Variables

```bash
# Add to ~/.bash_profile or ~/.zshrc
export ANTHROPIC_AUTH_TOKEN="your Levogat API Key"
export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"

# Apply changes
source ~/.bash_profile
```

### 3. Start Using

```bash
cd your-project
claude
```

## Recommended Groups

| Group | Multiplier | Best For |
|-------|-----------|----------|
| Default (Azure+MJ) | 1.0x | Daily use, great value |
| CC Dedicated | 2.4x | Optimized for Claude Code, best stability |
| anti/kiro | 1.2x | Best value option |

## FAQ

### Q: Claude Code reports "authentication failed"

Check that your environment variables are set correctly:
```bash
echo $ANTHROPIC_AUTH_TOKEN
echo $ANTHROPIC_BASE_URL
```

### Q: Slow response times

Try switching groups. The CC Dedicated group is optimized for Claude Code and offers faster speeds.

### Q: Does it support Claude Opus 4.8?

Yes. Type `/model` in Claude Code to switch models.

## Related Links

- [Levogat AI Website](https://api.levogat.com)
- [Claude Code Official Docs](https://docs.anthropic.com/en/docs/claude-code)
- [API Documentation](https://levogat.apifox.cn/)
