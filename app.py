import streamlit as st
import ollama

### Page Config ###
st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠")

### Daily Tip ###
st.info("🌿 Daily Mental Health Tip: Take 5 minutes today to slow down and breathe deeply.")

### Session State ###
st.session_state.setdefault("conversation_history", [])
st.session_state.setdefault("mood_log", [])
st.session_state.setdefault("mental_health_log", [])

### Mood Detection ###
def detect_mood(text):
    text = text.lower()
    if any(word in text for word in ["hopeless", "suicide", "kill myself", "end my life"]):
        return "Emergency"
    elif any(word in text for word in ["stress", "pressure", "tired", "overwhelmed"]):
        return "Stress"
    elif any(word in text for word in ["sad", "lonely", "depressed"]):
        return "Sad"
    elif any(word in text for word in ["anxious", "fear", "panic", "worried"]):
        return "Anxiety"
    else:
        return "Normal"

### Mental Health Area Detection ###
def detect_mental_health_type(text):
    text = text.lower()
    if any(word in text for word in ["depressed", "anxiety", "panic"]):
        return "Psychological Health"
    elif any(word in text for word in ["lonely", "friends", "family", "relationship"]):
        return "Social Health"
    elif any(word in text for word in ["focus", "memory", "concentrate"]):
        return "Cognitive Health"
    elif any(word in text for word in ["sleep", "addiction", "habit"]):
        return "Behavioral Health"
    elif any(word in text for word in ["purpose", "meaning", "empty"]):
        return "Spiritual Well-being"
    elif any(word in text for word in ["exam", "study", "job", "work"]):
        return "Academic / Occupational Health"
    elif any(word in text for word in ["headache", "body pain", "fatigue"]):
        return "Physical–Mental Health"
    elif any(word in text for word in ["sad", "happy", "angry", "stress"]):
        return "Emotional Health"
    else:
        return "General Mental Health"

### Generate Response ###
def generate_response(user_input):
    mood = detect_mood(user_input)
    mental_health_type = detect_mental_health_type(user_input)

    st.session_state["mood_log"].append(mood)
    st.session_state["mental_health_log"].append(mental_health_type)

    # Always save the user's message first
    st.session_state["conversation_history"].append(
        {"role": "user", "content": user_input}
    )

    if mood == "Emergency":
        ai_response = (
            "💔 I'm really sorry you're feeling this way. "
            "You are not alone. Please contact a mental health professional "
            "or a trusted person immediately. If you are in immediate danger, "
            "please call your local emergency number."
        )
        # Save the emergency response to history so it doesn't disappear
        st.session_state["conversation_history"].append(
            {"role": "assistant", "content": ai_response}
        )
        return ai_response, mood, mental_health_type

    # ADDED: System Prompt to give the AI a therapist persona
    system_prompt = {
        "role": "system", 
        "content": "You are a compassionate and empathetic mental health support assistant. Keep your responses brief, supportive, and non-judgmental. Do not diagnose."
    }
    messages_to_send = [system_prompt] + st.session_state["conversation_history"]

    try:
        response = ollama.chat(
            model="qwen2.5:3b",
            messages=messages_to_send
        )
        ai_response = response["message"]["content"]
    except Exception as e:
        ai_response = f"⚠️ Error connecting to Ollama. Please make sure Ollama is running and the model is downloaded. (Error: {e})"

    st.session_state["conversation_history"].append(
        {"role": "assistant", "content": ai_response}
    )

    return ai_response, mood, mental_health_type

### Extra Features ###
def generate_affirmation():
    prompt = "Provide a positive affirmation for someone feeling stressed."
    try:
        response = ollama.chat(model="qwen2.5:3b", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception:
        return "⚠️ Could not generate affirmation. Check Ollama connection."

def generate_meditation_guide():
    prompt = "Provide a 5-minute guided meditation to reduce stress."
    try:
        response = ollama.chat(model="qwen2.5:3b", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception:
        return "⚠️ Could not generate meditation. Check Ollama connection."

### UI ###
st.title("🧠 Mental Health Support Agent")

### ADDED: Sidebar for extra features and session summary ###
with st.sidebar:
    st.header("Self-Care Tools")
    
    if st.button("✨ Give me a Positive Affirmation", use_container_width=True):
        with st.spinner("Generating..."):
            st.success(generate_affirmation())

    if st.button("🧘 Give me a Guided Meditation", use_container_width=True):
        with st.spinner("Generating..."):
            st.info(generate_meditation_guide())
            
    st.divider()
    
    # Clear Chat Button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state["conversation_history"] = []
        st.session_state["mood_log"] = []
        st.session_state["mental_health_log"] = []
        st.rerun()

    # Session Summary moved to sidebar
    if st.session_state.get("mental_health_log"):
        st.divider()
        st.markdown("### 📊 Session Summary")
        most_common = max(
            set(st.session_state["mental_health_log"]),
            key=st.session_state["mental_health_log"].count
        )
        st.write(f"Most discussed area today: **{most_common}**")

### Show chat history (native chat bubbles) ###
for msg in st.session_state["conversation_history"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

### Chat input (interactive, sticks to bottom) ###
user_message = st.chat_input("How can I help you today?")

if user_message:
    # Show the user's message immediately
    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response, mood, mental_health_type = generate_response(user_message)

            st.info(f"🩺 Mental Health Area: {mental_health_type}")

            if mood == "Stress":
                st.warning("Detected Mood: Stress 😰")
            elif mood == "Sad":
                st.info("Detected Mood: Sad 😢")
            elif mood == "Anxiety":
                st.warning("Detected Mood: Anxiety 😟")
            elif mood == "Emergency":
                st.error("🚨 Emergency Support Detected")

            st.markdown(ai_response)

    st.rerun()