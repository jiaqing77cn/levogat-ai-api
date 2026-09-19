<h1 align="center">🚀 Proxy de IA API en China | Claude/GPT/Gemini/DeepSeek sin VPN | Levogat AI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"/>
  <img src="https://img.shields.io/badge/500%2B-Models-34d399?style=flat" alt="Models"/>
  <img src="https://img.shields.io/badge/CDN-China%20Accel-3b82f6?style=flat" alt="CDN"/>
  <img src="https://img.shields.io/badge/OpenAI-Compatible-10a37f?style=flat" alt="OpenAI Compatible"/>
</p>

<div align="center">

**Sin VPN · Baja Latencia · 366 Modelos · OpenAI Compatible · Claude Code Ready**

[🌐 Sitio Web](https://api.levogat.com) · [📋 Precios](https://api.levogat.com/pricing) · [📖 Docs API](https://levogat.apifox.cn/) · [💬 Contacto](https://api.levogat.com)

</div>

> Last updated: 2026-09-19 18:41 (UTC+8)| [中文](./README.md) | [English](./README_EN.md) | [한국어](./README_KO.md) | [日本語](./README_JA.md) | Español | [Deutsch](./README_DE.md)

---

## 📋 Tabla de Contenidos

- [🖥️ Vista previa del producto](#-vista-previa-del-producto)
- [🔍 Cómo elegir un proxy de API](#-cómo-elegir-un-proxy-de-api)
- [💰 Precios de modelos en tiempo real](#-precios-de-modelos-en-tiempo-real)
- [🛠️ Guía de integración](#-guía-de-integración)
- [📊 Comparación](#-comparación)
- [❓ Preguntas frecuentes](#-preguntas-frecuentes)
- [📖 Guías detalladas](#-guías-detalladas)
- [🤝 Contribuir](#-contribuir)

---

## 🖥️ Vista previa del producto

![Página principal de Levogat AI - panel de proxy de API con 366 modelos de IA](https://raw.githubusercontent.com/jiaqing77cn/levogat-ai-api/main/assets/homepage.jpg)

![Panel de Levogat AI - crear claves API, ver uso, recargar cuenta](https://raw.githubusercontent.com/jiaqing77cn/levogat-ai-api/main/assets/console.jpg)

---

## 🔍 Cómo elegir un proxy de API

Seis dimensiones para evaluar al elegir un proxy de API de IA:

| Dimensión | Qué verificar | Señales de alerta |
|-----------|--------------|-----------|
| **Estabilidad** | ¿Caídas frecuentes? ¿Alta latencia? | Desconexiones, sin anuncios |
| **Velocidad** | ¿Es aceptable la latencia de respuesta? | >5s de retraso en el primer token |
| **Cobertura de modelos** | ¿Disponibles los modelos más recientes? | Lentitud para añadir nuevos modelos |
| **Transparencia de precios** | ¿Facturación clara? ¿Registros de uso? | Sin registros de llamadas, opaco |
| **Sustitución de modelos** | ¿Usa modelos baratos para hacerse pasar por premium? | Precios anormalmente bajos, mala calidad |
| **Riesgo de cierre** | ¿Operado por una empresa? ¿Tiene soporte? | Operador en solitario, sin servicio al cliente |

### ⚠️ Lista de trampas a evitar

1. **Trampa del precio de caché**: El precio normal de caché es 10%, algunos cobran 15%-30%
2. **Detección de sustitución de modelos**: Compara las respuestas entre el oficial y el proxy con los mismos prompts
3. **Fraude en conteo de tokens**: Envía solicitudes con cantidades de tokens conocidas, verifica si la facturación está inflada
4. **Trampa de precio bajo**: Precios muy por debajo del mercado probablemente significan GLM haciéndose pasar por GPT
5. **Riesgo de estafa de cierre**: ¡No recargues grandes cantidades! Paga sobre la marcha

### 🔬 Cómo detectar sustitución de modelos

```python
# Método 1: Prueba de capacidad - usa prompts de razonamiento
prompt = "A farmer has 17 sheep. All but 9 die. How many are left?"
# GPT/Claude respuesta correcta: 9
# Modelos de gama baja a menudo se equivocan: 8

# Método 2: Prueba de contexto largo
# Envía un texto largo de 50K+ tokens, pregunta sobre detalles al final
# Los modelos de gama baja pierden el contexto

# Método 3: Prueba de capacidad de código
prompt = "Implement an LRU cache with TTL expiration in Python"
# Compara la calidad del código entre el oficial y el proxy
```

---

## 💰 Precios de modelos en tiempo real

> Los precios se obtienen automáticamente desde [Levogat API](https://api.levogat.com/api/pricing) mediante GitHub Actions, actualizados cada hora.
>
> Unidad: USD / Millón de Tokens | Relación Salida/Entrada = precio de salida ÷ precio de entrada

### Serie OpenAI GPT

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

### Serie Anthropic Claude

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

### Serie Google Gemini

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

### Serie DeepSeek

<!-- DEEPSEEK_PRICE_TABLE_START -->
| Model | Cheapest Group | Ratio | Input($/M) | Output($/M) | Premium Group | Ratio | Input($/M) | Output($/M) | Out/In |
|-------|---------------|-------|-----------|------------|--------------|-------|-----------|------------|--------|
| `deepseek-v4.1-flash` | Self-Deploye… | 1x | $0.30 | $1.20 | Self-Deploye… | 1.5x | $0.45 | $1.80 | 4x |
| `deepseek-v4-pro` | Self-Deploye… | 1x | $1.32 | $3.96 | deepseek-1 | 2.2x | $2.90 | $8.71 | 3x |
| `deepseek-v4-pro-0813` | Self-Deploye… | 1x | $1.32 | $3.96 | deepseek-1 | 2.2x | $2.90 | $8.71 | 3x |
| `deepseek-v4-flash` | Self-Deploye… | 1x | $0.44 | $1.32 | deepseek-1 | 2.2x | $0.97 | $2.90 | 3x |
| `deepseek-v4-flash-0731` | Self-Deploye… | 1x | $0.44 | $1.32 | deepseek-1 | 2.2x | $0.97 | $2.90 | 3x |
| `deepseek-v3.2` | Alibaba-1 | 1x | $0.29 | $0.43 | Alibaba-3 | 2.2x | $0.64 | $0.96 | 1.5x |
| `deepseek-v3.2-exp` | Alibaba-1 | 1x | $0.29 | $0.43 | Alibaba-3 | 2.2x | $0.64 | $0.96 | 1.5x |
| `deepseek-v3.1` | Self-Deploye… | 0.6x | $0.35 | $1.04 | Alibaba-3 | 2.2x | $1.28 | $3.83 | 3x |

<!-- DEEPSEEK_PRICE_TABLE_END -->

### Serie xAI Grok

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

### Modelos chinos (Qwen/Doubao/GLM/Kimi/MiniMax)

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

> 💡 Precios completos con los 81 grupos y 366 modelos en [Levogat AI Pricing](https://api.levogat.com/pricing)

### Niveles de grupos

| Tipo de grupo | Ratio | Mejor para |
|------------|-------|----------|
| Oferta flash | 0.6x | Pruebas, uso de bajo costo |
| Codex Exclusive | 0.8x | Programación con GPT, uso diario |
| Default | 1.0x | Calidad estándar, equilibrado |
| anti/kiro | 1.2x | Claude económico |
| Claude Code Exclusive | 2.4x | Programación con Claude Code |
| Canal Azure | 3.0x | GPT estable |
| AWS Enterprise | 4.0x | Claude de nivel empresarial |
| Vertex/Direct | 6.0x | Máxima calidad |
| Official Premium | 16.0x | Calidad oficial completa |

---

## 🛠️ Guía de integración

### Inicio rápido

1. Visita [Levogat AI](https://api.levogat.com) -> Regístrate -> Consola -> Crear Key
2. Recarga (mínimo 1 yuan)
   - Alipay / WeChat Pay / Crypto Pay / Tarjeta de crédito / Stripe
3. Elige tu método de integración:

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

Ejemplos completos en el directorio [`examples/`](./examples/) (incluye [Python](examples/quickstart.py) / [Node.js](examples/quickstart.js) / [Shell](examples/quickstart.sh)).

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

echo 'export ANTHROPIC_AUTH_TOKEN="***"' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"' >> ~/.bash_profile
source ~/.bash_profile

cd your-project && claude
```

📖 Guía completa: [Configuración de Claude Code](docs/es/claude-code-guide.md)

### OpenAI Codex

```bash
npm install -g @openai/codex
export OPENAI_API_KEY="***"
export OPENAI_API_BASE="https://api.levogat.com/v1"
```

📖 Guía completa: [Configuración de Codex](docs/es/codex-setup.md)

### Gemini CLI

```bash
npm install -g @google/gemini-cli
export GEMINI_API_KEY="***"
export GEMINI_API_BASE="https://api.levogat.com/v1"
```

📖 Guía completa: [Configuración de Cursor IDE](docs/es/cursor-setup.md) (también aplica para Gemini CLI)

### Integraciones con herramientas

| Herramienta | Configuración |
|------|-------|
| **Dify / FastGPT** | API Key + Base URL: `https://api.levogat.com/v1` |
| **n8n** | HTTP Request -> URL: `https://api.levogat.com/v1/chat/completions` |
| **LangChain** | `ChatOpenAI(openai_api_key="key", openai_api_base="https://api.levogat.com/v1")` |
| **NextChat** | Ajustes -> API personalizada -> URL: `https://api.levogat.com/v1` |
| **Cursor IDE** | Ajustes -> Variables de entorno -> `ANTHROPIC_BASE_URL=https://api.levogat.com/v1` |
| **OpenClaw** | `openai_api_key: key` + `openai_api_base: https://api.levogat.com/v1` |

### Casos de uso

- **Programación con IA** - Claude Code / Codex con Claude Opus 5 / GPT-5.6 para refactoring, corrección de bugs
- **Procesamiento de documentos largos** - Análisis de 100K+ palabras, revisión de contratos, resumen de papers
- **Agentes de IA** - Una clave para todos los modelos, tareas multi-agente en paralelo
- **Bases de conocimiento RAG** - DeepSeek / GPT con bases de datos vectoriales para Q&A empresarial
- **Flujos de trabajo automatizados** - Integración con n8n / FastGPT / Dify para automatización completa

---

## 📊 Comparativa 2026

> Basado en información pública al 2026-07-29. Solo como referencia.

| | [Levogat AI](https://api.levogat.com) | OpenRouter | SiliconFlow | Otros proxies | Autoconstruido |
|--|-------------|-----------|-------------|---------------|------------|
| Número de modelos | **366** | ~400 | ~200 | ~100 | Manual |
| Opciones de grupos | **81 grupos** | Ninguna (por proveedor) | Ninguna | 1-3 | - |
| CDN en China | ✅ Multi-nodo | ❌ Sin nodos en China | ✅ Único | ✅ | ❌ |
| Recarga mínima | **¥1** | ~¥35 | ¥50 | ¥20 | - |
| Pago por uso | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Code ready | ✅ | ✅ | ✅ | ✅ | ❌ |
| OpenAI compatible | ✅ | ✅ | ✅ | ✅ | Necesita adaptador |
| Transparencia de precios | ✅ 81 grupos | Por modelo, elección limitada | Precio único | Precio único | - |
| Código abierto en GitHub | ✅ Precios automáticos | ❌ | ❌ | ❌ | - |

---

## ❓ Preguntas frecuentes

**¿Las respuestas son idénticas a las de la API oficial?**

Sí. Levogat AI solo reenvía las solicitudes a los modelos oficiales: las respuestas son consistentes con la API oficial.

**¿Mi cuenta puede ser baneada?**

No. Usas la clave de Levogat AI, no el sistema de cuentas oficial, tu cuenta oficial no está en riesgo.

**¿Cuál es la diferencia entre los grupos?**

Los diferentes grupos corresponden a diferentes canales de backend (Azure/AWS/Vertex/Official Direct, etc.) con calidad y precio variables. Los grupos más económicos ofrecen mejor relación calidad-precio; los grupos más caros ofrecen máxima estabilidad. Comienza con el grupo default y ajusta según sea necesario.

**¿Es compatible con streaming?**

Sí, todos los modelos soportan `stream: true` con baja latencia.

**¿Qué tan rápido es desde China?**

Nodos CDN en China, latencia típicamente de 40-200ms, mucho más rápido que conectarse directamente a las APIs oficiales.

**¿Hay una capa gratuita?**

Los nuevos usuarios reciben créditos de prueba. Empieza gratis, recarga cuando quieras.

**¿Qué grupo debería elegir?**

- Económico: Oferta flash (0.6x) / Codex Exclusive (0.8x)
- Equilibrado: Default (1.0x)
- Alta calidad: Claude Code Exclusive (2.4x) / Azure (3.0x)
- Máxima calidad: Vertex (6.0x) / Official Premium (16.0x)

---

## 📖 Guías detalladas

| Guía | Contenido |
|-------|---------|
| [Guía de Claude Code](docs/es/claude-code-guide.md) | Configuración completa de Claude Code para China |
| [Guía de Claude Desktop](docs/es/claude-desktop-guide.md) | Configurar Claude Desktop con Levogat AI |
| [Guía de Codex](docs/es/codex-setup.md) | Configuración de OpenAI Codex CLI para China |
| [Guía de Gemini CLI](docs/es/gemini-cli-guide.md) | Gemini CLI con Levogat AI para modelos Gemini |
| [Configuración de Cursor IDE](docs/es/cursor-setup.md) | Usar GPT-5.6 / Claude Opus 5 / Gemini en Cursor |
| [Guía de Grok Build](docs/es/grok-build-guide.md) | xAI Grok Build con modelos personalizados de Levogat AI |
| [Guía de OpenCode](docs/es/opencode-guide.md) | OpenCode agente open-source con Levogat AI |
| [Guía de OpenClaw](docs/es/openclaw-guide.md) | OpenClaw Agent runtime con Levogat AI |
| [Guía de CC Switch](docs/es/cc-switch-guide.md) | Gestión unificada de configuración para múltiples herramientas IA |
| [Guía de integración con Dify](docs/es/dify-integration.md) | Conectar Dify con Levogat AI |
| [Guía de selección de modelos](docs/es/model-selection-guide.md) | ¿Cuál de los 366 modelos elegir? Por caso de uso y presupuesto |
| [Guía de detección de fraude](docs/es/fraud-detection-guide.md) | 5 métodos para detectar sustitución de modelos en proxies de API |
| [Guía de calculadora de costos](docs/es/cost-calculator-guide.md) | Estima costos de API y optimiza el gasto |

---

## 🤝 Contribuir

- 🐛 Reportar bug -> [Abrir un Issue](https://github.com/jiaqing77cn/levogat-ai-api/issues)
- 📝 Mejorar docs -> Enviar un PR
- 💡 Solicitud de función -> [Iniciar una Discussion](https://github.com/jiaqing77cn/levogat-ai-api/discussions)
- 📄 Guía de contribución -> Ver [CONTRIBUTING.md](./CONTRIBUTING.md)
- 📋 Registro de cambios -> Ver [CHANGELOG.md](./CHANGELOG.md)

---

## 📜 Licencia

MIT License · Copyright (c) 2026 [Levogat AI](https://api.levogat.com)

## 📢 Aviso de Marcas Registradas

GPT y OpenAI son marcas registradas de OpenAI. Claude es una marca registrada de Anthropic PBC. Gemini es una marca registrada de Google LLC. DeepSeek es una marca registrada de DeepSeek. Este repositorio describe únicamente la compatibilidad y no implica afiliación oficial ni respaldo por parte de estas empresas.
