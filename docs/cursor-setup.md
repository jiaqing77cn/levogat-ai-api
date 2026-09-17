# Cursor 配置 API 教程（中转 API 接入 Claude/GPT）

> Cursor 配置中转 API 的完整教程：支持 Claude Opus 5、GPT-6、DeepSeek V4，国内直连，一键配置 API Key。

> 👉 **获取 API Key**：[api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=cursor-setup&utm_campaign=docs-funnel)（注册即送体验额度，支付宝/微信可充值）

## 配置步骤

### 1. 打开 Cursor 设置

`Cmd/Ctrl + ,` -> 搜索 "OpenAI" -> 找到 "OpenAI API Key"

### 2. 填入配置

- **API Key**: 你的 Levogat API Key
- **Base URL**: `https://api.levogat.com/v1`

### 3. 修改 ~/.cursor/settings.json

```json
{
  "openai.apiKey": "你的 Levogat API Key",
  "openai.baseUrl": "https://api.levogat.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. 使用 Claude 模型

在 Cursor 的模型选择中输入自定义模型名：
- `claude-sonnet-4-6` - 日常编程
- `claude-opus-4-8` - 复杂任务
- `gpt-5.6-sol` - GPT 编程

## 推荐配置

| 用途 | 模型 | 分组 |
|------|------|------|
| 代码补全 | gpt-5.6-luna | Codex 专属 (0.8x) |
| 对话 | claude-sonnet-4-6 | 默认 (1.0x) |
| 复杂重构 | claude-opus-4-8 | CC 专属 (2.4x) |
