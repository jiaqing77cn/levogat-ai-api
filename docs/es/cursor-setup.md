# Guía de configuración de API en Cursor (API puente para Claude/GPT)

> Guía completa para configurar una API puente en Cursor: compatible con Claude Opus 5, GPT-6, DeepSeek V4. Acceso directo en China.

> 👉 **Obtén tu API Key**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=cursor-setup&utm_campaign=docs-funnel) (créditos de prueba gratis — recarga con Alipay/WeChat/crypto)

## Pasos de Configuración

### 1. Abrir la Configuración de Cursor

`Cmd/Ctrl + ,` -> Buscar "OpenAI" -> Encontrar "OpenAI API Key"

### 2. Ingresar la Configuración

- **API Key**: Tu Levogat API Key
- **Base URL**: `https://api.levogat.com/v1`

### 3. Modificar ~/.cursor/settings.json

```json
{
  "openai.apiKey": "Tu Levogat API Key",
  "openai.baseUrl": "https://api.levogat.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. Usar Modelos Claude

En el selector de modelos de Cursor, introduce el nombre del modelo personalizado:
- `claude-sonnet-4-6` - Programación diaria
- `claude-opus-4-8` - Tareas complejas
- `gpt-5.6-sol` - Programación con GPT

## Configuración Recomendada

| Uso | Modelo | Grupo |
|-----|--------|-------|
| Autocompletado de código | gpt-5.6-luna | Codex exclusivo (0.8x) |
| Conversación | claude-sonnet-4-6 | Por defecto (1.0x) |
| Refactorización compleja | claude-opus-4-8 | CC exclusivo (2.4x) |
