# Grok Build 接入教程

> 在 Grok Build 中使用 Levogat AI 中转调用 GPT/Claude/Gemini 等模型。

## 什么是 Grok Build

Grok Build 是 xAI 推出的终端 AI 编程助手，支持交互式 TUI、无头模式和 ACP 协议。通过自定义模型配置，可以让 Grok Build 调用 Levogat AI 上的任意模型。

## 配置步骤

### 1. 安装 Grok Build

**macOS / Linux：**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash

> ⚠️ 安装前建议先审查脚本内容：curl -fsSL https://x.ai/cli/install.sh | less
```

**Windows (PowerShell)：**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. 配置自定义模型

编辑 `~/.grok/config.toml`（Windows: `%USERPROFILE%\.grok\config.toml`）：

```toml
# 使用 Levogat AI 作为后端
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

### 3. 设置 API Key

```bash
export LEVOGAT_API_KEY="你的 Levogat API Key"
```

### 4. 开始使用

```bash
cd your-project
grok
```

在 TUI 中使用 `/model` 切换模型：

```
/model levogat-claude
```

## 推荐模型配置

| 用途 | 模型 | 分组建议 |
|------|------|---------|
| 日常编程 | `gpt-5.6-luna` | Codex 专属 (0.8x) |
| 复杂编程 | `gpt-5.6-sol` | Codex 专属 (0.8x) |
| 深度推理 | `claude-opus-4-8` | 默认 (1.0x) |
| 长文本 | `gemini-2.5-pro` | gemini-cli (1.0x) |

## 无头模式

```bash
# 使用 Levogat 模型执行任务
grok -p "Explain this codebase" -m levogat-claude

# 输出 JSON
grok -p "Analyze architecture" -m levogat-gpt --output-format streaming-json
```

## 常见问题

### Q: Grok Build 启动时提示 "model not found"

运行 `grok inspect` 检查配置是否正确加载：

```bash
grok inspect
```

### Q: 如何同时使用 Grok 模型和 Levogat 模型？

在 `config.toml` 中添加 xAI 官方模型和 Levogat 模型，通过 `/model` 命令切换。

### Q: 支持流式输出吗

支持。Levogat AI 所有模型均支持流式输出。

## 相关链接

- [Levogat AI 官网](https://api.levogat.com)
- [Grok Build 官方文档](https://docs.x.ai/build/overview)
- [Grok Build GitHub](https://github.com/xai-org/grok-build)
- [API 文档](https://levogat.apifox.cn/)
