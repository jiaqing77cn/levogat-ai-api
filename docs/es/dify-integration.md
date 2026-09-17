# Guía de integración de Dify: configurar API compatible con OpenAI

> Conecta Dify con Levogat AI: una sola Key para acceder a más de 500 modelos de IA.

## ¿Qué es Dify?

Dify es una plataforma de desarrollo de aplicaciones LLM de código abierto, que soporta gestión de base de conocimientos, orquestación de Agentes y automatización de flujos de trabajo. Al integrarse con Levogat AI, Dify puede llamar a GPT-5.6, Claude 4.8, Gemini, DeepSeek y todos los demás modelos.

## Pasos de Configuración

### 1. Obtener la Levogat API Key

Ve a [Levogat AI](https://api.levogat.com) -> Regístrate -> Consola -> Crear Key

### 2. Configurar el Proveedor de Modelos en Dify

Entra en Dify -> Configuración -> Proveedores de Modelos -> Selecciona **OpenAI API Compatible**:

| Campo de Configuración | Valor |
|------------------------|-------|
| API Key | Tu Levogat API Key |
| API endpoint | `https://api.levogat.com/v1` |
| Nombre del modelo | `gpt-5.6-sol` / `claude-sonnet-4-6` / `deepseek-reasoner` etc. |

### 3. Añadir Múltiples Modelos

En la página de "Modelos" de Dify, añade los modelos que necesites:

**Configuración recomendada:**

| Uso | Modelo | Grupo Recomendado |
|-----|--------|-------------------|
| Asistente conversacional | `claude-sonnet-4-6` | Por defecto (1.0x) |
| Asistente de programación | `gpt-5.6-sol` | Codex exclusivo (0.8x) |
| Procesamiento de textos largos | `gemini-2.5-pro` | Gemini-CLI mixto (1.0x) |
| Tareas de razonamiento | `deepseek-reasoner` | Oferta especial (0.6x) |
| Conversación diaria | `gpt-5.6-luna` | Codex exclusivo (0.8x) |

### 4. Usar en Aplicaciones

Al crear una aplicación, selecciona el modelo añadido en el menú desplegable "Modelo".

## Configuración de Base de Conocimientos RAG

Uso de la función de base de conocimientos de Dify con Levogat AI:

1. **Modelo de Embedding**: Usa `text-embedding-3-large` (soportado por Levogat)
2. **Modelo rerank**: No soportado por ahora, puedes desactivar rerank
3. **Modelo de conversación**: Recomendado `claude-sonnet-4-6` o `gpt-5.6-sol`

### Estimación de Costos de Base de Conocimientos

| Cantidad de Documentos | Costo de Embedding | Costo por Conversación |
|------------------------|--------------------|-----------------------|
| 100 | ~$0.02 | ~$0.01 |
| 1000 | ~$0.20 | ~$0.01 |
| 10000 | ~$2.00 | ~$0.02 |

## Configuración de Flujo de Trabajo del Agent

Flujo de trabajo típico de Dify Agent + Levogat AI:

```
Entrada del usuario -> Claude Sonnet 4.6 (reconocimiento de intención)
                   -> DeepSeek R1 (análisis de razonamiento)
                   -> GPT-5.6 Sol (generación de respuesta)
```

Con una sola API Key puedes usar todos los modelos, sin necesidad de múltiples cuentas.

## Dify Desplegado con Docker

Si despliegas Dify con Docker, establece las variables de entorno en `docker-compose.yml`:

```yaml
services:
  api:
    environment:
      - OPENAI_API_KEY=TuLevogatKey
      - OPENAI_API_BASE=https://api.levogat.com/v1
```

## Preguntas Frecuentes

### P: Dify muestra el error "model not found"

Asegúrate de que el nombre del modelo coincida exactamente. La lista de modelos soportados por Levogat está en la [tabla de precios del README](../../README_ES.md#-precios-de-modelos-en-tiempo-real).

### P: La salida en streaming no funciona

Activa la opción "Salida en streaming" en la configuración del modelo de Dify. Todos los modelos de Levogat soportan streaming.

### P: ¿Cómo controlar los costos?

1. Usa el grupo de oferta especial (multiplicador 0.6x)
2. Para textos largos usa Gemini 2.5 Flash ($0.30/M de entrada)
3. Para conversación diaria usa GPT-5.6 Luna ($0.80/M de entrada)
4. Establece límites de tokens en Dify

## Enlaces Relacionados

- [Levogat AI - Sitio Oficial](https://api.levogat.com)
- [Documentación Oficial de Dify](https://docs.dify.ai)
- [Documentación de la API](https://levogat.apifox.cn/)
- [Guía de Selección de Modelos](./model-selection-guide.md)
- [Calculadora de Costos](./cost-calculator-guide.md)
