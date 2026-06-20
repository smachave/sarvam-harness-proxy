# Sarvam Agent Harness

A project for setting up and running agents with Sarvam AI models through LiteLLM.

## Quick Start

### Prerequisites

- Python 3.8+ installed
- Git installed

### Installation & Setup

1. **Install litellm**
   ```bash
   pip install litellm
   ```

2. **Set up your Sarvam API key**
   ```bash
   export SARVAM_API_KEY="your_sarvam_api_key_here"
   ```
   > **Note**: Make sure to replace `your_sarvam_api_key_here` with your actual Sarvam API key.

3. **Clone this repository**
   ```bash
   git clone <repository_url>
   cd sarvam-agent-harness
   ```

4. **Launch litellm**
   ```bash
   litellm --config litellm.yaml --port 4000
   ```

The `litellm.yaml` file contains your Sarvam model configuration. The user will manage the rest.

## Usage Examples

### Basic Chat Completion
```bash
curl -X POST http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Hello, how are you?"}]}'
```

## Pi Agent Configuration

This project integrates with Pi Agent for enhanced AI capabilities. Pi Agent is configured through the `~/.pi/agent/models.json` file, which defines available AI providers and models.

For example, here's the actual Sarvam provider configuration from your `~/.pi/agent/models.json`:

```json
{
  "sarvam": {
    "api": "openai-completions",
    "apiKey": "sk-1234",
    "baseUrl": "http://localhost:4000/v1",
    "models": [
      {
        "id": "sarvam-105b",
        "name": "Sarvam 105B"
      },
      {
        "id": "sarvam-30b",
        "name": "Sarvam 30B"
      }
    ]
  }
}
```

### Available Models

Based on the current configuration, these Sarvam AI models are available:

**Sarvam AI Models**:
- Sarvam 105B
- Sarvam 30B

## License

This project is licensed under the MIT License.

---

**Note**: This README assumes you have already obtained a Sarvam API key from the [Sarvam AI website](https://www.sarvam.ai/).