# Dify-Integrationsguide: OpenAI-kompatible API konfigurieren

> Verbinde Dify mit Levogat AI – ein Key für 500+ KI-Modelle.

## Was ist Dify

Dify ist eine Open-Source-LLM-Anwendungsentwicklungsplattform, die Wissensbankverwaltung, Agent-Orchestrierung und Workflow-Automatisierung unterstützt. Durch die Anbindung an Levogat AI kann Dify auf alle Modelle wie GPT-5.6, Claude 4.8, Gemini, DeepSeek und weitere zugreifen.

## Konfigurationsschritte

### 1. Levogat API Key abrufen

Gehe zu [Levogat AI](https://api.levogat.com) -> Registrieren -> Konsole -> Key erstellen

### 2. Modellanbieter in Dify konfigurieren

Gehe zu Dify -> Einstellungen -> Modellanbieter -> Wähle **OpenAI API kompatibel**:

| Konfiguration | Wert |
|--------|-----|
| API Key | Dein Levogat API Key |
| API endpoint | `https://api.levogat.com/v1` |
| Modellname | `gpt-5.6-sol` / `claude-sonnet-4-6` / `deepseek-reasoner` etc. |

### 3. Mehrere Modelle hinzufügen

Füge auf der Dify-Modellseite nacheinander die benötigten Modelle hinzu:

**Empfohlene Konfiguration:**

| Verwendung | Modell | Gruppenempfehlung |
|------|------|---------|
| Konversationsassistent | `claude-sonnet-4-6` | Standard (1.0x) |
| Programmierassistent | `gpt-5.6-sol` | Codex Exklusiv (0.8x) |
| Lange Texte verarbeiten | `gemini-2.5-pro` | Gemini-CLI Gemischt (1.0x) |
| Reasoning-Aufgaben | `deepseek-reasoner` | Zeitlich begrenztes Angebot (0.6x) |
| Tägliche Konversation | `gpt-5.6-luna` | Codex Exklusiv (0.8x) |

### 4. In der App verwenden

Beim Erstellen einer App einfach das hinzugefügte Modell aus dem Dropdown-Menü „Modell" auswählen.

## RAG-Wissensbank-Konfiguration

Nutzung der Dify-Wissensbankfunktion mit Levogat AI:

1. **Embedding-Modell**: Verwende `text-embedding-3-large` (von Levogat unterstützt)
2. **Rerank-Modell**: Derzeit nicht unterstützt, Rerank kann deaktiviert werden
3. **Konversationsmodell**: Empfohlen `claude-sonnet-4-6` oder `gpt-5.6-sol`

### Kostenabschätzung für Wissensbank

| Dokumentanzahl | Embedding-Kosten | Konversationskosten/Anfrage |
|--------|---------------|----------|
| 100 | ~$0.02 | ~$0.01 |
| 1000 | ~$0.20 | ~$0.01 |
| 10000 | ~$2.00 | ~$0.02 |

## Agent-Workflow-Konfiguration

Typischer Workflow für Dify Agent + Levogat AI:

```
Benutzereingabe -> Claude Sonnet 4.6 (Intent-Erkennung)
                -> DeepSeek R1 (Reasoning-Analyse)
                -> GPT-5.6 Sol (Antwortgenerierung)
```

Ein einziger API Key genügt, um alle Modelle zu steuern – keine mehreren Accounts nötig.

## Dify mit Docker

Wenn du Dify über Docker bereitstellst, setze die Umgebungsvariablen in der `docker-compose.yml`:

```yaml
services:
  api:
    environment:
      - OPENAI_API_KEY=Dein Levogat Key
      - OPENAI_API_BASE=https://api.levogat.com/v1
```

## Häufige Fragen

### F: Dify meldet "model not found"

Stelle sicher, dass der Modellname exakt übereinstimmt. Die Liste der von Levogat unterstützten Modelle findest du in der [README-Preistabelle](../../README_DE.md#-live-modellpreise).

### F: Streaming-Ausgabe funktioniert nicht

Aktiviere die Option „Streaming-Ausgabe" in den Dify-Modelleinstellungen. Alle Levogat-Modelle unterstützen streaming.

### F: Wie kann man die Kosten kontrollieren?

1. Verwende die Gruppe mit zeitlich begrenztem Angebot (0.6x Multiplikator)
2. Für lange Texte Gemini 2.5 Flash verwenden ($0.30/M Eingabe)
3. Für tägliche Konversationen GPT-5.6 Luna verwenden ($0.80/M Eingabe)
4. Token-Limits in Dify festlegen

## Verwandte Links

- [Levogat AI Webseite](https://api.levogat.com)
- [Dify offizielle Dokumentation](https://docs.dify.ai)
- [API Dokumentation](https://levogat.apifox.cn/)
- [Modell-Auswahlleitfaden](./model-selection-guide.md)
- [Kostenrechner](./cost-calculator-guide.md)
