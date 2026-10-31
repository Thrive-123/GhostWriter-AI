
import streamlit as st
import ollama

st.set_page_config(
    page_title="GhostWriter AI",
    page_icon="👻",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #100d1c, #21132f, #101827);
    color: white;
}
h1, h2, h3, p, label {
    color: #f2eaff !important;
}
.stButton button {
    background-color: #7c3aed;
    color: white;
    border-radius: 10px;
    border: none;
    width: 100%;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("👻 GhostWriter AI")
st.caption("Unleash the stories hiding in the shadows...")
st.write("Create mysterious and terrifying stories with local AI.")

st.divider()

prompt = st.text_area(
    "🕯️ Describe your story idea",
    placeholder="Example: A student receives messages from a haunted classroom..."
)

genre = st.selectbox(
    "Choose your horror theme",
    [
        "Haunted House",
        "Ghost Story",
        "Paranormal Mystery",
        "Psychological Horror",
        "Cursed Object",
        "Supernatural Mystery"
    ]
)

length = st.selectbox(
    "Story Length",
    ["Short", "Medium", "Long"]
)

intensity = st.select_slider(
    "Fear Level",
    options=["Mild", "Creepy", "Terrifying"]
)

if st.button("👻 Generate My Story"):
    if not prompt.strip():
        st.warning("Please enter a story idea first!")
    else:
        with st.spinner("The ghost is writing your story..."):
            try:
                response = ollama.chat(
                    model="gemma3:1b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are GhostWriter AI, a creative horror "
                                "story writer. Write original, immersive "
                                "stories with suspense, atmosphere and "
                                "a memorable ending. Do not claim the "
                                "stories are real events."
                            )
                        },
                        {
                            "role": "user",
                            "content": f"""
                            Create an original horror story.

                            Idea: {prompt}
                            Theme: {genre}
                            Length: {length}
                            Fear level: {intensity}

                            Give the story a creative title.
                            Make it engaging and well structured.
                            """
                        }
                    ]
                )

                story = response["message"]["content"]

                st.session_state["story"] = story

            except Exception as e:
                st.error(f"AI Error: {e}")
                st.info(
                    "Make sure Ollama is running and "
                    "gemma3:1b is installed."
                )

if "story" in st.session_state:
    st.divider()
    st.subheader("📜 Your Haunted Story")
    st.markdown(st.session_state["story"])

    st.download_button(
        "⬇️ Download Story",
        data=st.session_state["story"],
        file_name="my_ghost_story.txt",
        mime="text/plain"
    )

    st.button(
        "🔮 Generate Another",
        on_click=lambda: st.session_state.pop("story", None)
    )

st.divider()
st.caption("Powered by Gemma 3 1B • Ollama • Streamlit")
st.caption("👻 Your imagination. Your local AI. Your story.")
