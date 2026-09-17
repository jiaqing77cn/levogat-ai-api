# Cursor API-Einrichtungsguide (Relay-API für Claude/GPT)

> Komplette Anleitung zur Einrichtung einer Relay-API in Cursor — unterstützt Claude Opus 5, GPT-6, DeepSeek V4. Direktzugang in China.

> 👉 **API-Key holen**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=cursor-setup&utm_campaign=docs-funnel) (kostenlose Testguthaben — Alipay/WeChat/Crypto)

## Konfigurationsschritte

### 1. Cursor-Einstellungen öffnen

`Cmd/Ctrl + ,` -> Suche nach "OpenAI" -> Finde "OpenAI API Key"

### 2. Konfiguration eintragen

- **API Key**: Dein Levogat API Key
- **Base URL**: `https://api.levogat.com/v1`

### 3. ~/.cursor/settings.json anpassen

```json
{
  "openai.apiKey": "Dein Levogat API Key",
  "openai.baseUrl": "https://api.levogat.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. Claude-Modelle verwenden

Gib in Cursors Modellauswahl einen benutzerdefinierten Modellnamen ein:
- `claude-sonnet-4-6` - Tägliche Programmierung
- `claude-opus-4-8` - Komplexe Aufgaben
- `gpt-5.6-sol` - GPT-Programmierung

## Empfohlene Konfiguration

| Verwendung | Modell | Gruppe |
|------|------|------|
| Code-Vervollständigung | gpt-5.6-luna | Codex Exklusiv (0.8x) |
| Konversation | claude-sonnet-4-6 | Standard (1.0x) |
| Komplexes Refactoring | claude-opus-4-8 | CC Exklusiv (2.4x) |
