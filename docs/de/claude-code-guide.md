# Claude Code Drittanbieter-API Einrichtungsguide (China)

> Die komplette Anleitung zur Einrichtung von Claude Code mit einem Drittanbieter-API-Key in China — ohne VPN, niedrige Latenz, unterstützt Claude Opus 5 / Sonnet 5. In 5 Minuten fertig.

> 👉 **API-Key holen**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=claude-code-guide&utm_campaign=docs-funnel) (kostenlose Testguthaben — Alipay/WeChat/Crypto)

## Was ist Claude Code

Claude Code ist der offizielle KI-Programmierassistent von Anthropic, der direkt im Terminal verwendet werden kann und Code-Generierung, Refactoring, Bug-Fixing und Test-Erstellung unterstützt.

## Konfigurationsschritte

### 1. Claude Code installieren

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Umgebungsvariablen konfigurieren

```bash
# Zur ~/.bash_profile oder ~/.zshrc hinzufügen
export ANTHROPIC_AUTH_TOKEN="Dein Levogat API Key"
export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"

# Aktivieren
source ~/.bash_profile
```

### 3. Mit der Nutzung beginnen

```bash
cd your-project
claude
```

## Empfohlene Gruppen

| Gruppe | Multiplikator | Anwendungsbereich |
|------|------|---------|
| Standard (Azure+MJ) | 1.0x | Tägliche Nutzung, hohes Preis-Leistungs-Verhältnis |
| CC Exklusiv | 2.4x | Speziell für Claude Code optimiert, höchste Stabilität |
| anti/kiro | 1.2x | Preis-Leistungs-Sieger |

## Häufige Fragen

### F: Claude Code meldet "authentication failed"

Überprüfe, ob die Umgebungsvariablen korrekt gesetzt sind:
```bash
echo $ANTHROPIC_AUTH_TOKEN
echo $ANTHROPIC_BASE_URL
```

### F: Die Antwortgeschwindigkeit ist langsam

Versuche, die Gruppe zu wechseln. Die CC-exklusive Gruppe ist speziell für Claude Code optimiert und schneller.

### F: Wird Claude Opus 4.8 unterstützt?

Ja. Gib in Claude Code `/model` ein, um das Modell zu wechseln.

## Verwandte Links

- [Levogat AI Webseite](https://api.levogat.com)
- [Claude Code offizielle Dokumentation](https://docs.anthropic.com/en/docs/claude-code)
- [API Dokumentation](https://levogat.apifox.cn/)
