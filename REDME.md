# 🎛️ AI Engineering Parameter Sandbox

An interactive command-line interface (CLI) sandbox designed to test and experiment with AI generation parameters (`temperature` and `top_p`) locally using Ollama and the Llama 3.2 (3B) model.

## 🚀 Features
* **Interactive Parameter Tuning:** Test how different temperature (0.0 - 2.0) and top_p (0.0 - 1.0) values alter AI creativity and focus.
* **Local Processing:** Runs entirely on your machine using Ollama for total data privacy.
* **Error Resilience:** Gracefully catches connection errors if the local server isn't running.

## 🛠️ Prerequisites

Before running the sandbox, you must have the following installed:
1. **Python 3.8+**
2. **Ollama** (Download from [ollama.com](https://ollama.com))

### Setup Ollama
Make sure the Llama 3.2 model is pulled and running locally:
```bash
# Pull the required model
ollama pull llama3.2:3b

# Ensure the Ollama server is active
ollama serve
```

## 💻 Installation & Setup

1. **Clone or download** this repository to your local machine.
2. Navigate into the project directory:
   ```bash
   cd ai-sandbox
   ```
3. Install the required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 How to Run

Execute the main script to launch the interactive terminal hub:
```bash
python main.py
```

Follow the on-screen prompts to input your system instructions, user queries, and parameter metrics to see the local AI engine compile your response.
