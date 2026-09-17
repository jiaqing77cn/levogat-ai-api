# API 中转站大全（2026 实测版）

> 数据来源：2026-09-17 对各站公开接口（`/api/pricing`、`/api/status`）实测，仅收录**当前在线**的中转站。
> 模型数/分组数为接口实时返回值，价格请以各站定价页为准。本列表仅供参考，不构成推荐。

市面上流传的中转站列表（如 awesome-ai-proxy）大多年久失修，约三分之一站点已关停。本列表只收录实测在线的站点，并持续更新。

## 站点列表（按可探测模型数排序）

| 中转站 | 模型数（实测） | 分组数 | 备注 |
|---|---|---|---|
| **[Levogat](https://api.levogat.com)**（本仓库） | **366** | **81** | 支付宝/微信/加密货币，价格表每6小时自动更新 |
| [KFCV50API](https://kfcv50.link) | 1494 | 109 | - |
| [bltcy](https://api.bltcy.ai) | 1073 | 26 | - |
| [ggwk1](https://www.ggwk1.online) | 599 | 29 | - |
| [v3](https://api.v3.cm) | 568 | 14 | - |
| [sbgpt](https://go.sbgpt.site) | 477 | 24 | - |
| [yunwu](https://yunwu.ai) | 389 | 36 | - |
| [MaynorAPI](https://apipro.maynor1024.live) | 389 | 36 | - |
| [openaiLabs](https://www.openai-labs.com) | 335 | 30 | - |
| [35-aigcbest](https://35.aigcbest.top) | 251 | 4 | - |
| [kksj](https://cnapi.kksj.org) | 231 | 9 | - |
| [GalaxyAPI](https://api.openai-ch.top) | 222 | 10 | - |
| [nekoapi](https://api.nekoapi.com) | 157 | 14 | - |
| [gptgod](https://gptgod.cloud) | - | - | 模型数较少或非 new-api 架构 |
| [zhtec](https://api1.zhtec.xyz) | - | - | 模型数较少或非 new-api 架构 |
| [xjai-new](https://new.xjai.cc) | - | - | 接口未开放模型数据 |
| [xeduapi](https://xeduapi.com) | - | - | 模型数较少或非 new-api 架构 |
| [ephone](https://api.ephone.ai) | - | - | 模型数较少或非 new-api 架构 |
| [chatfire](https://api.chatfire.cn) | - | - | 模型数较少或非 new-api 架构 |
| [aabao](https://api.aabao.top) | - | - | 接口未开放模型数据 |
| [YuegleAPI](https://api.yuegle.com) | - | - | 接口未开放模型数据 |
| [OneChats](https://chatapi.onechats.top) | - | - | 接口未开放模型数据 |
| [azapi](https://azapi.com.cn) | - | - | 模型数较少或非 new-api 架构 |
| [mnapi](https://www.mnapi.com) | - | - | 模型数较少或非 new-api 架构 |

## 收录标准

- 当前在线，提供公开的 AI API 中转服务
- 支持 OpenAI 兼容格式优先
- 无诈骗/跑路记录

## 提交收录 / 修正

欢迎通过 [Issue](https://github.com/jiaqing77cn/levogat-ai-api/issues/new?template=station-submission.md) 提交你的中转站或修正信息，请包含：

1. 站点名称与官网地址
2. 支持的模型范围（OpenAI/Claude/Gemini/国产模型等）
3. 支付方式
4. （可选）公开定价接口地址

## 免责声明

- 模型数、分组数为检测当日接口返回值，可能随时间变化
- 部分站点未开放公开定价接口，无法获取模型数，不代表其服务质量
- 列表排序仅依据可探测模型数，不代表推荐顺序
