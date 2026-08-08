import httpx

def query_engine(systemPrompt: str, user_input: str, temperature: float, top_p: float):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2:3b",
        "prompt": f"""
        SYSTEM PROMPT: {systemPrompt}
        USER INPUT: {user_input}
        """,
        "stream": False,
        "options": {
            "temperature": temperature,
            "top_p": top_p
        }
    }
    try:
        response = httpx.post(url, json=payload, timeout=15.0)
        return response.json().get("response")
    except httpx.ConnectError:
        return "Error: Make sure 'ollama serve' is running."

# --- INTERACTIVE TERMINAL TESTING HUB ---
print("==================================================")
print("🎛️ THE ULTIMATE AI ENGINEERING PARAMETER SANDBOX")
print("==================================================")

sys_input = input("1. Enter your system prompt: ")
user_input = input("2. Enter your user input: ")

temp_input = float(input("3. Enter temperature (0.0 - 2.0): "))
top_p_input = float(input("4. Enter top_p (0.0 - 1.0): "))

print("\n⚙️ Calculating words using M5 Silicon Gates...")
ai_response = query_engine(sys_input, user_input, temp_input, top_p_input)
print("\n🤖 AI Engine Response:")
print(ai_response)