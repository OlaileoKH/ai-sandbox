import httpx
import streamlit as st


def query_engine(
    systemPrompt: str, user_input: str, temperature: float, top_p: float
):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2:3b",
        "prompt": f"SYSTEM PROMPT: {systemPrompt}\nUSER INPUT: {user_input}",
        "stream": False,
        "options": {"temperature": temperature, "top_p": top_p},
    }
    try:
        response = httpx.post(url, json=payload, timeout=15.0)
        return response.json().get("response")
    except httpx.ConnectError:
        return "Error: Make sure 'ollama serve' is running."


# --- STREAMLIT UI DESIGN ---
st.set_page_config(page_title="AI Parameter Sandbox", page_icon="🎛️")

st.title("🎛️ AI Engineering Parameter Sandbox")
st.markdown(
    "Experiment with your local Llama 3.2 model parameters in real-time."
)

# Text inputs for prompts
system_input = st.text_area(
    "1. System Prompt",
    value="You are a helpful assistant.",
    help="Set the behavior of the AI.",
)
user_input = st.text_area(
    "2. User Input",
    placeholder="Type your message here...",
    help="The question or prompt for the AI.",
)

# Column layout for sliders
col1, col2 = st.columns(2)

with col1:
    temp_input = st.slider(
        "3. Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Higher values mean more creative/random outputs.",
    )

with col2:
    top_p_input = st.slider(
        "4. Top P",
        min_value=0.0,
        max_value=1.0,
        value=0.9,
        step=0.05,
        help="Controls the pool of words considered based on cumulative probability.",
    )

# Run button
if st.button("🚀 Run AI Engine", use_container_width=True):
    if not user_input.strip():
        st.warning("Please enter some user input first!")
    else:
        with st.spinner("🤖 Local AI is thinking..."):
            ai_response = query_engine(
                system_input, user_input, temp_input, top_p_input
            )

        st.subheader("🤖 AI Engine Response:")
        if "Error:" in ai_response:
            st.error(ai_response)
        else:
            st.write(ai_response)
