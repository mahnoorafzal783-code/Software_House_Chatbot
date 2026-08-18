import streamlit as st
import os
from dotenv import load_dotenv
from database import save_conversation, get_conversations
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)


# ==============================
# AI RESPONSE FUNCTION
# ==============================

def get_ai_response(user_message):

    project_id = st.session_state.get("project_id", "TEMP")

    history = get_conversations(project_id)

    messages = [
        {
            "role": "system",
            "content": """
You are the official AI assistant for a Software House.

Your ONLY purpose is to help users with Software House
services and software-related projects.

You can help with:

- Website development
- E-commerce websites
- Mobile app development
- Web applications
- Custom software
- AI solutions
- AI chatbots
- UI/UX design
- Software project requirements
- Project cost estimates
- Project timelines
- Software House services

You must NOT answer unrelated questions.

For example, do not answer questions about:
- Personal information about people
- Celebrities
- Politics
- Entertainment
- Recipes
- Weather
- General unrelated knowledge
- Other topics that are not related to software or the Software House

If the user asks an unrelated question, reply:

"Sorry, I can only help with Software House services,
software projects, websites, apps, AI solutions,
and other software-related topics."

Always stay focused on the Software House business.
"""
        }
    ]


    # Add previous conversation to AI memory

    for old_user_message, old_ai_response in history:

        messages.append({
            "role": "user",
            "content": old_user_message
        })

        messages.append({
            "role": "assistant",
            "content": old_ai_response
        })


    # Add current user message

    messages.append({
        "role": "user",
        "content": user_message
    })


    # Get AI response

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages
    )


    ai_response = response.choices[0].message.content


    # Save conversation

    save_conversation(
        project_id=project_id,
        user_message=user_message,
        ai_response=ai_response
    )


    return ai_response


# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="Software House AI",
    page_icon="🤖",
    layout="centered"
)


# ==============================
# CUSTOM DESIGN
# ==============================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #eef7ff,
        #f5efff
    );
}


/* Robot */

.bot-face {
    width: 120px;
    height: 120px;

    border-radius: 50%;

    margin: 15px auto;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 65px;

    background:
        linear-gradient(
            135deg,
            #60a5fa,
            #a78bfa
        );

    box-shadow:
        0 10px 35px
        rgba(99,102,241,0.35);
}


/* Title */

.main-title {

    text-align: center;

    font-size: 40px;

    font-weight: 800;

    color: #5b21b6;

}


/* Subtitle */

.subtitle {

    text-align: center;

    font-size: 17px;

    color: #475569;

    margin-bottom: 25px;

}


/* Section title */

.quick-title {

    text-align: center;

    font-size: 22px;

    font-weight: 700;

    color: #4c1d95;

    margin: 20px 0;

}


/* Buttons */

.stButton > button {

    border-radius: 14px;

    border: none;

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #8b5cf6
        );

    color: white;

    font-weight: 600;

    padding: 10px;

    box-shadow:
        0 5px 15px
        rgba(99,102,241,0.25);

}


.stButton > button:hover {

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        );

}


/* Chat */

[data-testid="stChatMessage"] {

    border-radius: 18px;

    padding: 8px;

}


/* Chat input */

[data-testid="stChatInput"] {

    border-radius: 18px;

}

</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="bot-face">🤖</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">Software House AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Websites • Apps • AI • Software Solutions ✨'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ==============================
# QUICK ACTIONS
# ==============================

st.markdown(
    '<div class="quick-title">⚡ Quick Actions</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    website_button = st.button(
        "🌐 Website Idea",
        use_container_width=True
    )

    app_button = st.button(
        "📱 App Idea",
        use_container_width=True
    )

    estimate_button = st.button(
        "💰 Project Estimate",
        use_container_width=True
    )


with col2:

    business_button = st.button(
        "💡 Software Business Idea",
        use_container_width=True
    )

    requirements_button = st.button(
        "📝 Project Requirements",
        use_container_width=True
    )

    ai_button = st.button(
        "🤖 Ask Software AI",
        use_container_width=True
    )


# ==============================
# QUICK PROMPTS
# ==============================

quick_prompt = None


if website_button:

    quick_prompt = (
        "Give me a professional website idea "
        "for a business."
    )


elif app_button:

    quick_prompt = (
        "Suggest a useful mobile app idea "
        "and explain its main features."
    )


elif estimate_button:

    quick_prompt = (
        "Give me a general software project "
        "cost estimate and development timeline."
    )


elif business_button:

    quick_prompt = (
        "Suggest a software business idea "
        "that a Software House could develop."
    )


elif requirements_button:

    quick_prompt = (
        "Help me create clear requirements "
        "for my software project."
    )


elif ai_button:

    quick_prompt = (
        "What Software House services can you "
        "help me with?"
    )


# ==============================
# QUICK RESPONSE
# ==============================

if quick_prompt:

    st.chat_message(
        "user"
    ).write(quick_prompt)


    with st.spinner("✨ Thinking..."):

        answer = get_ai_response(
            quick_prompt
        )


    st.chat_message(
        "assistant"
    ).write(answer)


# ==============================
# CHAT
# ==============================

st.divider()


st.markdown(
    '<div class="quick-title">'
    '💬 Chat with Software House AI'
    '</div>',
    unsafe_allow_html=True
)


user_message = st.chat_input(
    "✨ Type your software-related question..."
)


if user_message:

    st.chat_message(
        "user"
    ).write(user_message)


    with st.spinner("🤖 Thinking..."):

        ai_response = get_ai_response(
            user_message
        )


    st.chat_message(
        "assistant"
    ).write(ai_response)