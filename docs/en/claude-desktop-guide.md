# Claude Desktop Third-Party API Setup Guide

> Use Levogat AI with the Claude Desktop app to access Claude models directly without a VPN.

> 👉 **Get your API Key**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=claude-desktop-guide&utm_campaign=docs-funnel) (free trial credits — Alipay/WeChat/crypto accepted)

## What is Claude Desktop

Claude Desktop is Anthropic's official desktop client, available for macOS and Windows. By configuring environment variables, you can route Claude Desktop through Levogat AI to access Claude models.

## Configuration Steps

### 1. Set Environment Variables

**macOS:**

```bash
# Add to ~/.zshrc or ~/.bash_profile
export ANTHROPIC_API_KEY="your Levogat API Key"
export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"

# Apply changes
source ~/.zshrc
```

**Windows:**

```powershell
# PowerShell permanent setting
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "your-key", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://api.levogat.com/v1", "User")
```

### 2. Restart Claude Desktop

Fully quit Claude Desktop (not minimize), then relaunch it. The app will read the new environment variables.

### 3. Verify Connection

Send a message in Claude Desktop. If you receive a normal response, the connection through Levogat AI is successful.

## MCP Server Configuration

Claude Desktop supports MCP (Model Context Protocol) for integrating additional tools:

Edit the configuration file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "levogat": {
      "command": "curl",
      "args": ["https://api.levogat.com/v1/chat/completions"]
    }
  }
}
```

## Recommended Models

| Use Case | Model | Group Suggestion |
|----------|-------|-----------------|
| Daily chat | `claude-sonnet-4-6` | Default (1.0x) |
| Complex tasks | `claude-opus-4-8` | Default (1.0x) |
| Lightweight tasks | `claude-haiku-4-5` | Default (1.0x) |

## FAQ

### Q: Claude Desktop doesn't read environment variables after launch?

Make sure you fully quit the app (right-click the tray icon -> Quit), then launch it from the terminal:

```bash
open -a "Claude"
```

### Q: Getting a "connection error"?

Check that your API Key is correct and the Base URL ends with `/v1`.

### Q: Does it support Claude Opus 4.8?

Yes. Type `/model claude-opus-4-8` in the chat to switch models.

## Related Links

- [Levogat AI Official Site](https://api.levogat.com)
- [Claude Desktop Official Download](https://claude.ai/download)
- [API Documentation](https://levogat.apifox.cn/)
