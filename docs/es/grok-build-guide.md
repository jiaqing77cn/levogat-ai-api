# Guía de Integración con Grok Build

> Usa Levogat AI en Grok Build para invocar modelos como GPT/Claude/Gemini a través de intermediario.

## ¿Qué es Grok Build?

Grok Build es el asistente de programación con IA para terminal de xAI, que soporta TUI interactivo, modo headless y protocolo ACP. Mediante configuración personalizada de modelos, Grok Build puede invocar cualquier modelo disponible en Levogat AI.

## Pasos de Configuración

### 1. Instalar Grok Build

**macOS / Linux:**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash

> ⚠️ Se recomienda revisar el script antes de instalar: curl -fsSL https://x.ai/cli/install.sh | less
```

**Windows (PowerShell):**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. Configurar Modelos Personalizados

Edita `~/.grok/config.toml` (Windows: `%USERPROFILE%\.grok\config.toml`):

```toml
# Usar Levogat AI como backend
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

### 3. Configurar API Key

```bash
export LEVOGAT_API_KEY="tu Levogat API Key"
```

### 4. Comenzar a Usar

```bash
cd your-project
grok
```

Usa `/model` en el TUI para cambiar de modelo:

```
/model levogat-claude
```

## Configuración de Modelos Recomendados

| Uso | Modelo | Grupo Recomendado |
|------|------|---------|
| Programación diaria | `gpt-5.6-luna` | Codex exclusivo (0.8x) |
| Programación compleja | `gpt-5.6-sol` | Codex exclusivo (0.8x) |
| Razonamiento profundo | `claude-opus-4-8` | Por defecto (1.0x) |
| Textos largos | `gemini-2.5-pro` | gemini-cli (1.0x) |

## Modo Headless

```bash
# Usar modelo de Levogat para ejecutar tareas
grok -p "Explain this codebase" -m levogat-claude

# Salida en formato JSON
grok -p "Analyze architecture" -m levogat-gpt --output-format streaming-json
```

## Preguntas Frecuentes

### P: Grok Build muestra "model not found" al iniciar

Ejecuta `grok inspect` para verificar que la configuración se haya cargado correctamente:

```bash
grok inspect
```

### P: ¿Cómo usar simultáneamente modelos de Grok y Levogat?

Añade tanto los modelos oficiales de xAI como los de Levogat en `config.toml`, y cambia entre ellos con el comando `/model`.

### P: ¿Soporta salida en streaming?

Sí. Todos los modelos de Levogat AI soportan salida en streaming.

## Enlaces Relacionados

- [Levogat AI - Sitio Oficial](https://api.levogat.com)
- [Documentación Oficial de Grok Build](https://docs.x.ai/build/overview)
- [GitHub de Grok Build](https://github.com/xai-org/grok-build)
- [Documentación API](https://levogat.apifox.cn/)
