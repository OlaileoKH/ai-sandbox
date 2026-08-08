# 🎛️ AI Engineering Parameter Sandbox

An interactive web application designed to test and experiment with AI generation parameters (`temperature` and `top_p`) in real-time using Ollama and the Llama 3.2 (3B) model.

## 🚀 Features
* **Interactive UI:** Built entirely with Streamlit, featuring sleek sliders and wide text areas.
* **Parameter Tuning:** Instantly visualize how changing temperature (0.0 - 2.0) and top_p (0.0 - 1.0) shifts AI focus and creativity.
* **Local Processing:** Queries your local Ollama setup for zero-latency testing and complete privacy.

## 🛠️ Prerequisites

Before launching the web app, ensure you have the following installed on your local computer:
1. **Python 3.8+**
2. **Ollama** (Download from [ollama.com](https://ollama.com))

### Set Up Ollama
Make sure your local background model is running:
```bash
# Download the Llama 3.2 model
ollama pull llama3.2:3b

# Start the Ollama local engine
ollama serve
```

## 💻 Installation & Setup

1. **Clone or download** this repository to your machine.
2. Navigate directly into the project directory:
   ```bash
   cd ai-sandbox
   ```
3. Install the web server and connection packages using the updated requirements file:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 How to Run

Launch the local interactive Streamlit server using your terminal:
```bash
streamlit run app.py
```

Your web browser will automatically launch a new window at `http://localhost:8501`. Feed your custom system prompt instructions, adjust the precision sliders, and hit **Run AI Engine** to view your output!
