# Grok Build Integrationsanleitung

> Verwenden Sie Levogat AI als Proxy in Grok Build, um Modelle wie GPT/Claude/Gemini aufzurufen.

## Was ist Grok Build?

Grok Build ist der von xAI entwickelte Terminal-AI-Programmierassistent und unterstützt interaktives TUI, Headless-Modus und das ACP-Protokoll. Durch benutzerdefinierte Modellkonfiguration kann Grok Build beliebige Modelle von Levogat AI aufrufen.

## Konfigurationsschritte

### 1. Grok Build installieren

**macOS / Linux:**

```bash
curl -fsSL https://x.ai/cli/install.sh | bash

> ⚠️ Skript vor der Installation überprüfen: curl -fsSL https://x.ai/cli/install.sh | less
```

**Windows (PowerShell):**

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

### 2. Benutzerdefinierte Modelle konfigurieren

Bearbeiten Sie `~/.grok/config.toml` (Windows: `%USERPROFILE%\.grok\config.toml`):

```toml
# Levogat AI als Backend verwenden
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

### 3. API Key festlegen

```bash
export LEVOGAT_API_KEY="Ihr Levogat API Key"
```

### 4. Verwendung starten

```bash
cd your-project
grok
```

Im TUI mit `/model` das Modell wechseln:

```
/model levogat-claude
```

## Empfohlene Modellkonfiguration

| Verwendungszweck | Modell | Gruppenempfehlung |
|------|------|---------|
| Tägliche Programmierung | `gpt-5.6-luna` | Codex exklusiv (0.8x) |
| Komplexe Programmierung | `gpt-5.6-sol` | Codex exklusiv (0.8x) |
| Tiefgreifendes Reasoning | `claude-opus-4-8` | Standard (1.0x) |
| Lange Texte | `gemini-2.5-pro` | gemini-cli (1.0x) |

## Headless-Modus

```bash
# Aufgabe mit Levogat-Modell ausführen
grok -p "Explain this codebase" -m levogat-claude

# JSON-Ausgabe
grok -p "Analyze architecture" -m levogat-gpt --output-format streaming-json
```

## Häufig gestellte Fragen

### F: Grok Build meldet beim Start "model not found"

Führen Sie `grok inspect` aus, um zu überprüfen, ob die Konfiguration korrekt geladen wurde:

```bash
grok inspect
```

### F: Wie kann ich gleichzeitig Grok-Modelle und Levogat-Modelle verwenden?

Fügen Sie in `config.toml` sowohl die offiziellen xAI-Modelle als auch die Levogat-Modelle hinzu und wechseln Sie mit dem Befehl `/model`.

### F: Wird Streaming-Ausgabe unterstützt?

Ja. Alle Modelle von Levogat AI unterstützen Streaming-Ausgabe.

## Verwandte Links

- [Levogat AI Webseite](https://api.levogat.com)
- [Grok Build offizielle Dokumentation](https://docs.x.ai/build/overview)
- [Grok Build GitHub](https://github.com/xai-org/grok-build)
- [API Dokumentation](https://levogat.apifox.cn/)
