import streamlit as st
from recommender.movie import get_movie_by_mood
from recommender.music import get_song_by_mood
from recommender.book import get_book_by_mood
from recommender.blog import get_blog_by_mood

st.set_page_config(page_title="AI Buddy", page_icon="🧠")
st.markdown(
    """
    <style>
    .stButton>button {
          html, body, .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%) !important;
    }        color: #222;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #ffbbbb;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1 style='text-align: center;'>🧠 AI Buddy</h1>", unsafe_allow_html=True)
st.write("ברוכה הבאה! אני כאן כדי להמליץ לך על משהו נחמד להיום 🎬🎧📘📰")

mood = st.text_input("איך את מרגישה היום? 😄😐😢 (עברית או אנגלית)")

if mood:
    if st.button("🎲 תן לי המלצה!"):
        mood = mood.lower()
        if any(word in mood for word in ["שמח", "happy", "כיף", "מעולה"]):
            detected_mood = "happy"
        elif any(word in mood for word in ["עצוב", "עייף", "down", "bad", "בלאי", "דאון"]):
            detected_mood = "sad"
        else:
            detected_mood = "neutral"

        # סרט
        movie = get_movie_by_mood(detected_mood)
        # שיר
        song = get_song_by_mood(detected_mood)
        # ספר
        book = get_book_by_mood(detected_mood)
        # בלוג
        blog = get_blog_by_mood(detected_mood)

        # טורים
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🎬 סרט:")
            st.image(movie["image"], width=250)
            st.markdown(f"**{movie['title']}**")
            st.write(movie["description"])

            st.subheader("📘 ספר:")
            st.markdown(f"[{book['title']}]({book['url']})")
            st.write(book["description"])

        with col2:
            st.subheader("🎧 שיר:")
            st.markdown(f"[{song['title']}]({song['url']})")

            st.subheader("📰 בלוג:")
            st.markdown(f"[{blog['title']}]({blog['url']})")
            st.write(blog["description"])
