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

## Detailed Setup

### Step 1: Install Dependencies

Install the required Python package:
```bash
pip install litellm
```

### Step 2: Configure API Key

Set your Sarvam API key as an environment variable:

**Linux/macOS:**
```bash
export SARVAM_API_KEY="your_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set SARVAM_API_KEY="your_api_key_here"
```

**Windows (PowerShell):**
```powershell
$env:SARVAM_API_KEY="your_api_key_here"
```

To make the environment variable persistent, add it to your shell profile (`.bashrc`, `.zshrc`, etc.) or system environment variables.

### Step 3: Clone the Repository

```bash
git clone https://github.com/smachave/sarvam-agent-harness.git
cd sarvam-agent-harness
```

### Step 4: Launch LiteLLM

Start LiteLLM using the configuration file:

```bash
litellm --config litellm.yaml --port 4000
```

The `litellm.yaml` file should contain your Sarvam model configuration.

## Usage Examples

### Basic Chat Completion
```bash
curl -X POST http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Hello, how are you?"}]}'
```

### Streaming Response
```bash
curl -X POST http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Tell me a story"}], "stream": true}'
```

### Custom Parameters
```bash
curl -X POST http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Explain quantum computing"}], "temperature": 0.7, "max_tokens": 500}'
```

## Configuration Options

LiteLLM supports various configuration options. View all available options with:

```bash
litellm --help
```

Common options include:
- `--temperature`: Control randomness (0.0 to 2.0)
- `--max_tokens`: Maximum response length
- `--stream`: Enable streaming responses
- `--api_base`: Custom API endpoint (if needed)

## Troubleshooting

### API Key Not Working
- Verify your API key is set correctly: `echo $SARVAM_API_KEY`
- Ensure the API key is valid and not expired
- Check that you have the necessary permissions for the model

### Model Not Found
- Verify the model name is correct: `litellm --list-models`
- Ensure you have access to the specific Sarvam model
- Check your API plan/subscription level

### Connection Issues
- Verify internet connectivity
- Check if the Sarvam API endpoint is accessible
- Try with a simpler model first

### Common Errors

**"Invalid API Key"**
- Double-check the API key format
- Ensure no extra spaces or quotes

**"Model not found"**
- List available models: `litellm --list-models`
- Verify model name spelling

**"Rate limit exceeded"**
- Reduce request frequency
- Check your API plan limits

## Getting Help

- Check the [LiteLLM documentation](https://docs.litellm.ai/)
- Review Sarvam AI's official documentation
- File issues in the repository if you encounter bugs

## License

This project is licensed under the MIT License.

---

**Note**: This README assumes you have already obtained a Sarvam API key from the [Sarvam AI website](https://www.sarvam.ai/).