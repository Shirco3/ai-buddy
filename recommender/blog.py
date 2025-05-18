import random

BLOG_RECOMMENDATIONS = {
    "happy": [
        {
            "title": "Tiny Buddha – How to Be Happy Now",
            "description": "טיפים פשוטים ומשמעותיים לשמחה יומיומית 💛",
            "url": "https://tinybuddha.com/blog/how-to-be-happy-now/"
        },
        {
            "title": "Zen Habits – Joy in the Present Moment",
            "description": "פוסט קצר על איך למצוא שלווה והשראה ברגעים הקטנים 🌼",
            "url": "https://zenhabits.net/joy/"
        }
    ],
    "sad": [
        {
            "title": "Mark Manson – The Subtle Art of Not Giving a F*ck",
            "description": "בלוג כנה ומשחרר על קבלה עצמית ואיזון רגשי 😌",
            "url": "https://markmanson.net/not-giving-a-fuck"
        },
        {
            "title": "Psychology Today – Coping with Depression",
            "description": "מאמר מעשי להתמודדות עם רגשות קשים ומחשבות שליליות 🫂",
            "url": "https://www.psychologytoday.com/us/blog/in-practice/201403/10-ways-fight-depression"
        }
    ],
    "neutral": [
        {
            "title": "Farnam Street – Mental Models",
            "description": "בלוג חכם על חשיבה ביקורתית ולמידה עמוקה 🔍",
            "url": "https://fs.blog/mental-models/"
        }
    ]
}

def get_blog_by_mood(mood: str) -> dict:
    mood = mood.lower()
    if mood in BLOG_RECOMMENDATIONS:
        return random.choice(BLOG_RECOMMENDATIONS[mood])
    return random.choice(BLOG_RECOMMENDATIONS["neutral"])
