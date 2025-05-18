import streamlit as st

st.set_page_config(page_title="AI Buddy", page_icon="🧠")

st.title("🧠 AI Buddy")
st.write("היי! אני כאן כדי להמליץ לך על משהו נחמד להיום")

mood = st.text_input("איך את מרגישה היום? 😄😐😢")

if mood:
    st.subheader("המלצה יומית:")

    if "עייף" in mood or "עייפה" in mood or "עצוב" in mood:
        st.write("🎬 סרט: *The Secret Life of Walter Mitty* – קליל ומעורר השראה 💫")
        st.write("🎧 שיר: *Let It Be – The Beatles* 🎵")
    elif "שמח" in mood or "מעולה" in mood:
        st.write("🎬 סרט: *La La Land* – מוזיקלי, צבעוני ומלא שמחת חיים 🎶")
        st.write("🎧 שיר: *Happy – Pharrell Williams* 😎")
    else:
        st.write("🎬 סרט: *Forrest Gump* – תמיד טוב, תמיד מרגש")
        st.write("🎧 שיר: *Bohemian Rhapsody – Queen*")

    st.caption("💡 בקרוב נוסיף המלצות לבלוגים, ספרים ואולי גם בדיחות 🤖")
