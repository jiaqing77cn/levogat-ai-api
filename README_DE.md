<h1 align="center">🚀 KI-API-Proxy in China | Claude/GPT/Gemini/DeepSeek ohne VPN | Levogat AI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/500%2B-Models-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-China%20Accel-3b82f6?style=flat" alt="CDN"/>
  <img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat" alt="OpenAI Compatible"/>
</p>

<div align="center">

**Kein VPN · Geringe Latenz · 366 Modelle · OpenAI Compatible · Claude Code Ready**

[🌐 Website](https://api.levogat.com) · [📋 Preise](https://api.levogat.com/pricing) · [📖 API-Dokumentation](https://levogat.apifox.cn/) · [💬 Kontakt](https://api.levogat.com)

</div>

> Last updated: 2026-09-21 04:37 (UTC+8)| [中文](./README.md) | [English](./README_EN.md) | [한국어](./README_KO.md) | [日本語](./README_JA.md) | [Español](./README_ES.md) | Deutsch

---

## 📋 Inhaltsverzeichnis

- [🖥️ Produktvorschau](#-produktvorschau)
- [🔍 Wie wählt man einen API-Proxy aus](#-wie-wählt-man-einen-api-proxy-aus)
- [💰 Live-Modellpreise](#-live-modellpreise)
- [🛠️ Integrationsleitfaden](#-integrationsleitfaden)
- [📊 Vergleich](#-vergleich)
- [❓ FAQ](#-faq)
- [📖 Ausführliche Leitfäden](#-ausführliche-leitfäden)
- [🤝 Mitwirken](#-mitwirken)

---

## 🖥️ Produktvorschau

![Levogat AI homepage - 366 AI model API proxy dashboard](https://raw.githubusercontent.com/jiaqing77cn/levogat-ai-api/main/assets/homepage.jpg)

![Levogat AI dashboard - create API keys, view usage, top up account](https://raw.githubusercontent.com/jiaqing77cn/levogat-ai-api/main/assets/console.jpg)

---

## 🔍 Wie wählt man einen API-Proxy aus

Sechs Dimensionen zur Bewertung bei der Auswahl eines KI-API-Proxys:

| Dimension | Was prüfen | Warnsignale |
|-----------|-----------|-------------|
| **Stabilität** | Häufige Ausfälle? Hohe Latenz? | Verbindungsabbrüche, keine Ankündigungen |
| **Geschwindigkeit** | Ist die Antwortlatenz akzeptabel? | >5s Verzögerung bis zum ersten Token |
| **Modellabdeckung** | Neueste Modelle verfügbar? | Langsame Ergänzung neuer Modelle |
| **Preistransparenz** | Klare Abrechnung? Nutzungsprotokolle? | Keine Aufrufprotokolle, intransparent |
| **Modellaustausch** | Günstige Modelle als Premium getarnt? | Auffällig niedrige Preise, schlechte Qualität |
| **Ausfallrisiko** | Unternehmensgeführt? Support vorhanden? | Einzelperson, kein Kundenservice |

### ⚠️ Kontrollliste für Fallstricke

1. **Cache-Preisfalle**: Normaler Cache-Preis liegt bei 10%, einige verlangen 15%-30%
2. **Modellaustausch erkennen**: Outputs zwischen offizieller API und Proxy mit denselben Prompts vergleichen
3. **Token-Zähl-Betrug**: Anfragen mit bekannter Token-Anzahl senden, prüfen ob Abrechnung aufgebläht wird
4. **Niedrigpreis-Falle**: Preise weit unter Marktniveau bedeuten oft GLM, der sich als GPT ausgibt
5. **Ausfallrisiko (Exit Scam)**: Keine großen Guthaben einzahlen! Pay-as-you-go nutzen

### 🔬 Modellaustausch erkennen

```python
# Methode 1: Fähigkeitstest - Reasoning-Prompts verwenden
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claude richtige Antwort: 9
# Low-End-Modelle liegen oft falsch: 8

# Methode 2: Long-Context-Test
# 50K+ Token langen Text senden, nach Details am Ende fragen
# Low-End-Modelle verlieren den Kontext

# Methode 3: Code-Fähigkeitstest
prompt = "Implement an LRU cache with TTL expiration in Python"
# Code-Qualität zwischen offizieller API und Proxy vergleichen
```

---

## 💰 Live-Modellpreise

> Preise werden automatisch von der [Levogat API](https://api.levogat.com/api/pricing) über GitHub Actions abgerufen, stündlich aktualisiert.
>
> Einheit: USD / Million Tokens | Output/Input-Verhältnis = Output-Preis ÷ Input-Preis

### OpenAI GPT Serie

<!-- GPT_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gpt-6-astra` | Codex-Gpt-1 | 0.07x | $0.74 | $3.68 | Azure-Gpt-6 | 1.8x | $18.00 | $90.00 | 5x |
| `gpt-5.6-sol` | Codex-Gpt-1 | 0.07x | $0.37 | $2.21 | Azure-Gpt-6 | 1.8x | $9.00 | $54.00 | 6x |
| `gpt-5.6-luna` | Azure-Gpt-2 | 0.2x | $0.04 | $0.24 | Azure-Gpt-6 | 1.8x | $0.36 | $2.16 | 6x |
| `gpt-5.6-terra` | Codex-Gpt-1 | 0.07x | $0.15 | $0.88 | Azure-Gpt-6 | 1.8x | $3.60 | $21.60 | 6x |
| `gpt-5.5` | Codex-Gpt-1 | 0.07x | $0.37 | $2.21 | Azure-Gpt-6 | 1.8x | $9.00 | $54.00 | 6x |
| `gpt-5.5-pro` | Openai-Gpt-1 | 1.18x | $35.29 | $211.77 | Azure-Gpt-6 | 1.8x | $54.00 | $324.00 | 6x |
| `gpt-5.4-pro` | Azure-Gpt-1 | 0.09x | $2.64 | $15.84 | Azure-Gpt-6 | 1.8x | $54.00 | $324.00 | 6x |
| `gpt-5.4-pro-2026-03-05` | Azure-Gpt-2 | 0.2x | $6.00 | $36.00 | Openai-Gpt-2 | 1.47x | $44.12 | $264.71 | 6x |
| `gpt-5.4-mini` | Azure-Gpt-1 | 0.09x | $0.07 | $0.40 | Azure-Gpt-6 | 1.8x | $1.35 | $8.10 | 6x |
| `gpt-5.4-mini-2026-03-17` | Azure-Gpt-1 | 0.09x | $0.07 | $0.40 | Openai-Gpt-2 | 1.47x | $1.10 | $6.62 | 6x |
| `gpt-5.4-nano` | Azure-Gpt-1 | 0.09x | $0.02 | $0.11 | Azure-Gpt-6 | 1.8x | $0.36 | $2.25 | 6.25x |
| `gpt-5.4-nano-2026-03-17` | Azure-Gpt-1 | 0.09x | $0.02 | $0.11 | Openai-Gpt-2 | 1.47x | $0.29 | $1.84 | 6.25x |
| `gpt-5.3-codex` | Azure-Gpt-2 | 0.2x | $0.35 | $2.80 | Openai-Gpt-2 | 1.47x | $2.57 | $20.59 | 8x |
| `gpt-5.2-codex` | Azure-Gpt-2 | 0.2x | $0.35 | $2.80 | Openai-Gpt-2 | 1.47x | $2.57 | $20.59 | 8x |
| `gpt-5.2-chat-latest` | Azure-Gpt-1 | 0.09x | $0.15 | $1.23 | Openai-Gpt-2 | 1.47x | $2.57 | $20.59 | 8x |

<!-- GPT_PRICE_TABLE_END -->

### Anthropic Claude Serie

<!-- CLAUDE_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `claude-fable-5` | Kiro-Claude-… | 0.18x | $1.76 | $8.82 | AWS-Claude-3 | 2.2x | $22.00 | $110.00 | 5x |
| `claude-fable-5-1` | Kiro-Claude-… | 0.18x | $1.76 | $8.82 | AWS-Claude-3 | 2.2x | $22.00 | $110.00 | 5x |
| `claude-haiku-4-5-20251001` | Kiro-Claude-… | 0.18x | $0.18 | $0.88 | AWS-Claude-3 | 2.2x | $2.20 | $11.00 | 5x |
| `claude-opus-4-1-20250805` | Azure-Claude… | 0.88x | $13.24 | $66.18 | AWS-Claude-3 | 2.2x | $33.00 | $165.00 | 5x |
| `claude-opus-4-5-20251101` | Kiro-Claude-… | 0.18x | $0.88 | $4.41 | AWS-Claude-3 | 2.2x | $11.00 | $55.00 | 5x |
| `claude-opus-4-6` | Kiro-Claude-… | 0.18x | $0.88 | $4.41 | AWS-Claude-3 | 2.2x | $11.00 | $55.00 | 5x |
| `claude-opus-4-7` | Kiro-Claude-… | 0.18x | $0.88 | $4.41 | AWS-Claude-3 | 2.2x | $11.00 | $55.00 | 5x |
| `claude-opus-4-8` | Kiro-Claude-… | 0.18x | $0.88 | $4.41 | AWS-Claude-3 | 2.2x | $11.00 | $55.00 | 5x |
| `claude-opus-5` | Kiro-Claude-… | 0.18x | $0.88 | $4.41 | AWS-Claude-3 | 2.2x | $11.00 | $55.00 | 5x |
| `claude-sonnet-4-5-20250929` | Kiro-Claude-… | 0.18x | $0.53 | $2.65 | AWS-Claude-3 | 2.2x | $6.60 | $33.00 | 5x |
| `claude-sonnet-4-6` | Kiro-Claude-… | 0.18x | $0.53 | $2.65 | AWS-Claude-3 | 2.2x | $6.60 | $33.00 | 5x |
| `claude-sonnet-5` | Kiro-Claude-… | 0.18x | $0.35 | $1.76 | AWS-Claude-3 | 2.2x | $4.40 | $22.00 | 5x |

<!-- CLAUDE_PRICE_TABLE_END -->

### Google Gemini Serie

<!-- GEMINI_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `gemini-3.8-flash` | Anti-Gemini-… | 0.15x | $0.11 | $0.55 | Aistudio-Gem… | 1.91x | $1.43 | $7.17 | 5x |
| `gemini-3.7-flash` | Anti-Gemini-… | 0.15x | $0.11 | $0.55 | Aistudio-Gem… | 1.91x | $1.43 | $7.17 | 5x |
| `gemini-3.6-flash` | Anti-Gemini-… | 0.15x | $0.11 | $0.55 | Aistudio-Gem… | 1.91x | $1.43 | $7.17 | 5x |
| `gemini-3.5-flash` | Anti-Gemini-… | 0.15x | $0.22 | $1.32 | Aistudio-Gem… | 1.91x | $2.87 | $17.21 | 6x |
| `gemini-3.5-flash-lite` | Anti-Gemini-… | 0.15x | $0.04 | $0.37 | Aistudio-Gem… | 1.91x | $0.57 | $4.78 | 8.33x |
| `gemini-3-pro-image` | Aistudio-Gem… | 0.35x | $0.00 | $0.00 | Aistudio-Gem… | 1.91x | $0.00 | $0.00 | 0x |
| `gemini-3-pro-image-preview` | Aistudio-Gem… | 0.35x | $0.00 | $0.00 | Aistudio-Gem… | 1.91x | $0.00 | $0.00 | 0x |
| `gemini-3-pro-preview` | Anti-Gemini-… | 0.15x | $0.29 | $1.76 | Aistudio-Gem… | 1.91x | $3.82 | $22.94 | 6x |

<!-- GEMINI_PRICE_TABLE_END -->

### DeepSeek Serie

<!-- DEEPSEEK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `deepseek-v4.1-flash` | Self-Deploye… | 0.6x | $0.18 | $0.72 | Self-Deploye… | 1.5x | $0.45 | $1.80 | 4x |
| `deepseek-v4-pro` | Self-Deploye… | 1x | $1.32 | $3.96 | deepseek-1 | 2.2x | $2.90 | $8.71 | 3x |
| `deepseek-v4-pro-0813` | Self-Deploye… | 0.6x | $0.79 | $2.38 | deepseek-1 | 2.2x | $2.90 | $8.71 | 3x |
| `deepseek-v4-flash` | Self-Deploye… | 1x | $0.44 | $1.32 | deepseek-1 | 2.2x | $0.97 | $2.90 | 3x |
| `deepseek-v4-flash-0731` | Self-Deploye… | 0.6x | $0.26 | $0.79 | deepseek-1 | 2.2x | $0.97 | $2.90 | 3x |
| `deepseek-v3.2` | Alibaba-1 | 1x | $0.29 | $0.43 | Alibaba-3 | 2.2x | $0.64 | $0.96 | 1.5x |
| `deepseek-v3.2-exp` | Alibaba-1 | 1x | $0.29 | $0.43 | Alibaba-3 | 2.2x | $0.64 | $0.96 | 1.5x |
| `deepseek-v3.1` | Self-Deploye… | 0.6x | $0.35 | $1.04 | Alibaba-3 | 2.2x | $1.28 | $3.83 | 3x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### xAI Grok Serie

<!-- GROK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `grok-4.6` | Cli-Grok-1 | 0.15x | $0.29 | $0.88 | Xai-Grok-1 | 0.88x | $1.76 | $5.29 | 3x |
| `grok-4.5` | Cli-Grok-1 | 0.15x | $0.29 | $0.88 | Xai-Grok-1 | 0.88x | $1.76 | $5.29 | 3x |
| `grok-4.3` | Azure-Grok-1 | 0.15x | $0.18 | $0.37 | Xai-Grok-1 | 0.88x | $1.10 | $2.21 | 2x |
| `grok-4-20-non-reasoning` | Cli-Grok-1 | 0.15x | $0.18 | $0.37 | Xai-Grok-1 | 0.88x | $1.10 | $2.21 | 2x |
| `grok-4-20-reasoning` | Cli-Grok-1 | 0.15x | $0.18 | $0.37 | Xai-Grok-1 | 0.88x | $1.10 | $2.21 | 2x |
| `grok-4` | Azure-Grok-1 | 0.15x | $0.44 | $2.21 | Azure-Grok-2 | 0.22x | $0.66 | $3.31 | 5x |

<!-- GROK_PRICE_TABLE_END -->

### Chinesische Modelle (Qwen/Doubao/GLM/Kimi/MiniMax)

<!-- CN_MODEL_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `qwen3.8-max` | Self-Deploye… | 0.6x | $1.20 | $3.60 | Alibaba-3 | 2.2x | $4.40 | $13.20 | 3x |
| `qwen3-max` | Self-Deploye… | 0.6x | $0.72 | $3.60 | Alibaba-3 | 2.2x | $2.64 | $13.20 | 5x |
| `qwen3-coder-plus` | Self-Deploye… | 0.6x | $0.60 | $3.00 | Self-Deploye… | 1x | $1.00 | $5.00 | 5x |
| `glm-5.3` | Self-Deploye… | 1x | $1.40 | $4.40 | Alibaba-3 | 2.2x | $3.08 | $9.68 | 3.14x |
| `glm-5.3-flash` | Self-Deploye… | 1x | $0.15 | $0.50 | Self-Deploye… | 1.5x | $0.22 | $0.75 | 3.33x |
| `glm-5.2` | Self-Deploye… | 1x | $1.40 | $4.40 | Alibaba-3 | 2.2x | $3.08 | $9.68 | 3.14x |
| `kimi-k3` | Self-Deploye… | 1x | $3.00 | $15.00 | Self-Deploye… | 1.5x | $4.50 | $22.50 | 5x |
| `kimi-k2.7-code` | Self-Deploye… | 1x | $0.95 | $3.95 | Kimi-2 | 2.2x | $2.09 | $8.68 | 4.15x |
| `kimi-k2.5` | Alibaba-1 | 1x | $0.60 | $3.15 | Alibaba-3 | 2.2x | $1.32 | $6.93 | 5.25x |
| `doubao-seed-2-1-pro-260628` | Doubao-2 | 1.5x | $1.35 | $6.75 | Doubao-3 | 2.2x | $1.98 | $9.90 | 5x |
| `doubao-seed-1-6-250615` | Doubao-2 | 1.5x | $0.18 | $1.80 | Doubao-3 | 2.2x | $0.26 | $2.64 | 10x |
| `MiniMax-M3` | Self-Deploye… | 1x | $0.30 | $1.20 | Hailuo-3 | 2.2x | $0.66 | $2.64 | 4x |
| `MiniMax-M2.7` | Self-Deploye… | 1.5x | $0.45 | $1.80 | Hailuo-3 | 2.2x | $0.66 | $2.64 | 4x |
| `qwen3.8-flash` | Alibaba-2 | 1.5x | $0.22 | $0.70 | Alibaba-3 | 2.2x | $0.33 | $1.03 | 3.13x |

<!-- CN_MODEL_PRICE_TABLE_END -->

> 💡 Vollständige Preisliste mit allen 81 Gruppen und 366 Modellen unter [Levogat AI Pricing](https://api.levogat.com/pricing)

### Gruppen-Stufen

| Gruppentyp | Verhältnis | Optimal für |
|------------|-----------|-------------|
| Flash Sale | 0.6x | Tests, kostengünstige Nutzung |
| Codex Exclusive | 0.8x | GPT-Codierung, tägliche Nutzung |
| Default | 1.0x | Standardqualität, ausgewogen |
| anti/kiro | 1.2x | Budget Claude |
| Claude Code Exclusive | 2.4x | Claude Code Programmierung |
| Azure Channel | 3.0x | Stabiles GPT |
| AWS Enterprise | 4.0x | Enterprise-Claude |
| Vertex/Direct | 6.0x | Höchste Qualität |
| Official Premium | 16.0x | Volle offizielle Qualität |

---

## 🛠️ Integrationsleitfaden

### Schnellstart

1. [Levogat AI](https://api.levogat.com) besuchen -> Registrieren -> Konsole -> Key erstellen
2. Guthaben aufladen (mind. 1 Yuan)
   - Alipay / WeChat Pay / Crypto Pay / Kreditkarte / Stripe
3. Integrationsmethode wählen:

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="***",
    base_url="https://api.levogat.com/v1"
)

# GPT-5.6 Sol
resp = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Write a Python quicksort"}]
)

# Claude Sonnet 5
resp = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
    extra_body={"anthropic_version": "vertex-2023-10-01"}
)

# DeepSeek V4
resp = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "Implement a web server in Python"}]
)
```

### Node.js / curl

```bash
curl https://api.levogat.com/v1/chat/completions \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

Vollständige Beispiele im Verzeichnis [`examples/`](./examples/) (inkl. [Python](examples/quickstart.py) / [Node.js](examples/quickstart.js) / [Shell](examples/quickstart.sh)).

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="***"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

📖 Vollständiger Leitfaden: [Claude Code Setup](docs/de/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://api.levogat.com/v1"
```

📖 Vollständiger Leitfaden: [Codex Setup](docs/de/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://api.levogat.com/v1"
```

📖 Vollständiger Leitfaden: [Cursor IDE Setup](docs/de/cursor-setup.md) (gilt auch für Gemini CLI)

### Tool-Integrationen

| Tool | Setup |
|------|-------|
| **Dify / FastGPT** | API Key + Base URL: `https://api.levogat.com/v1` |
| **n8n** | HTTP Request -> URL: `https://api.levogat.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://api.levogat.com/v1")` |
| **NextChat** | Settings -> Custom API -> URL: `https://api.levogat.com/v1` |
| **Cursor IDE** | Settings -> Env Vars -> `ANTHROPIC_BASE_URL=https://api.levogat.com/v1` |
| **OpenClaw** | `openai_api_key: key` + `openai_api_base: https://api.levogat.com/v1` |

### Anwendungsfälle

- **AI-Codierung** - Claude Code / Codex mit Claude Opus 5 / GPT-5.6 für Refactoring, Bug-Fixes
- **Lange Dokumente verarbeiten** - 100K+ Wort-Analyse, Vertragsprüfung, Papier-Zusammenfassung
- **KI-Agenten** - Ein Key für alle Modelle, Multi-Agent-Parallelaufgaben
- **RAG-Wissensbasen** - DeepSeek / GPT mit Vektordatenbanken für Enterprise-Q&A
- **Automatisierte Workflows** - n8n / FastGPT / Dify-Integration für vollständige Automatisierung

---

## 📊 Vergleich & Review 2026

> Basierend auf öffentlich verfügbaren Informationen vom 2026-07-29. Nur als Referenz.

| | [Levogat AI](https://api.levogat.com) | OpenRouter | SiliconFlow | Andere Proxys | Selbstgebaut |
|--|-------------|-----------|-------------|---------------|------------|
| Modellanzahl | **366** | ~400 | ~200 | ~100 | Manuell |
| Gruppen-Optionen | **81 Gruppen** | Keine (pro Anbieter) | Keine | 1-3 | - |
| China CDN | ✅ Multi-Node | ❌ Keine China-Knoten | ✅ Einzel | ✅ | ❌ |
| Mindestaufladung | **¥1** | ~¥35 | ¥50 | ¥20 | - |
| Pay-as-you-go | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code ready | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI compatible | ✅ | ✅ | ✅ | ✅ | Adapter nötig |
| Preistransparenz | ✅ 81 Gruppen | Pro Modell, eingeschränkte Wahl | Einzelpreis | Einzelpreis | - |
| GitHub Open Source | ✅ Auto-Pricing | ❌ | ❌ | ❌ | - |

---

## ❓ FAQ

**Sind die Antworten identisch mit der offiziellen API?**

Ja. Levogat AI leitet Anfragen nur an offizielle Modelle weiter - die Antworten sind mit der offiziellen API konsistent.

**Kann mein Account gesperrt werden?**

Nein. Sie verwenden den Key von Levogat AI, nicht das offizielle Account-System - Ihr offizieller Account ist nicht gefährdet.

**Was ist der Unterschied zwischen den Gruppen?**

Verschiedene Gruppen entsprechen verschiedenen Backend-Kanälen (Azure/AWS/Vertex/Official Direct usw.) mit unterschiedlicher Qualität und Preis. Kosten günstigere Gruppen bieten besseres Preis-Leistungs-Verhältnis; teurere Gruppen bieten maximale Stabilität. Mit der Default-Gruppe starten und bei Bedarf anpassen.

**Wird streaming unterstützt?**

Ja, alle Modelle unterstützen `stream: true` mit geringer Latenz.

**Wie schnell ist es aus China?**

China CDN-Knoten, Latenz typischerweise 40-200ms - deutlich schneller als direkte Verbindung zu offiziellen APIs.

**Gibt es eine kostenlose Stufe?**

Neue Nutzer erhalten Testguthaben. Kostenlos starten, bei Bedarf aufladen.

**Welche Gruppe soll ich wählen?**

- Budget: Flash Sale (0.6x) / Codex Exclusive (0.8x)
- Ausgewogen: Default (1.0x)
- Hohe Qualität: Claude Code Exclusive (2.4x) / Azure (3.0x)
- Maximale Qualität: Vertex (6.0x) / Official Premium (16.0x)

---

## 📖 Ausführliche Leitfäden

| Leitfaden | Inhalt |
|-----------|--------|
| [Claude Code Anleitung](docs/de/claude-code-guide.md) | Vollständige Claude-Code-Konfiguration für China |
| [Claude Desktop Anleitung](docs/de/claude-desktop-guide.md) | Claude Desktop mit Levogat AI konfigurieren |
| [Codex Anleitung](docs/de/codex-setup.md) | OpenAI Codex CLI-Konfiguration für China |
| [Gemini CLI Anleitung](docs/de/gemini-cli-guide.md) | Gemini CLI mit Levogat AI für Gemini-Modelle |
| [Cursor IDE Anleitung](docs/de/cursor-setup.md) | GPT-5.6 / Claude Opus 5 / Gemini in Cursor verwenden |
| [Grok Build Anleitung](docs/de/grok-build-guide.md) | xAI Grok Build mit Levogat AI Custom-Modellen |
| [OpenCode Anleitung](docs/de/opencode-guide.md) | OpenCode Open-Source-Agent mit Levogat AI |
| [OpenClaw Anleitung](docs/de/openclaw-guide.md) | OpenClaw Agent-Runtime mit Levogat AI |
| [CC Switch Anleitung](docs/de/cc-switch-guide.md) | Unified Konfigurationsmanagement für mehrere AI-Tools |
| [Dify Integrationsleitfaden](docs/de/dify-integration.md) | Dify mit Levogat AI verbinden |
| [Modell-Auswahlleitfaden](docs/de/model-selection-guide.md) | Welches der 366 Modelle wählen? Nach Anwendungsfall & Budget |
| [Fraud Detection Leitfaden](docs/de/fraud-detection-guide.md) | 5 Methoden zur Erkennung von Modellaustausch bei API-Proxys |
| [Kostenrechner-Anleitung](docs/de/cost-calculator-guide.md) | API-Kosten schätzen und Ausgaben optimieren |

---

## 🤝 Mitwirken

- 🐛 Fehler melden -> [Issue eröffnen](https://github.com/jiaqing77cn/levogat-ai-api/issues)
- 📝 Dokumentation verbessern -> PR einreichen
- 💡 Feature wünschen -> [Diskussion starten](https://github.com/jiaqing77cn/levogat-ai-api/discussions)
- 📄 Mitwirkungsleitfaden -> Siehe [CONTRIBUTING.md](./CONTRIBUTING.md)
- 📋 Changelog -> Siehe [CHANGELOG.md](./CHANGELOG.md)

---

## 📜 Lizenz

MIT License · Copyright (c) 2026 [Levogat AI](https://api.levogat.com)

## 📢 Markenrechtlicher Hinweis

GPT und OpenAI sind Marken von OpenAI. Claude ist eine Marke von Anthropic PBC. Gemini ist eine Marke von Google LLC. DeepSeek ist eine Marke von DeepSeek. Dieses Repository beschreibt lediglich Kompatibilität und impliziert keine offizielle Verbindung mit oder Unterstützung durch diese Unternehmen.
