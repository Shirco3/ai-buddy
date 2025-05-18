import random

MOVIE_RECOMMENDATIONS = {
    "happy": [
        {
            "title": "La La Land",
            "description": "סרט מוזיקלי צבעוני עם אווירה שמחה 🎶",
            "image": "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png"
        },
        {
            "title": "Paddington 2",
            "description": "הדוב הכי מתוק בעולם – מושלם ליום טוב ☀️",
            "image": "https://upload.wikimedia.org/wikipedia/en/6/6e/Paddington_2.jpg"
        }
    ],
    "sad": [
        {
            "title": "The Secret Life of Walter Mitty",
            "description": "סרט השראה למסע פנימי 🌍",
            "image": "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Secret_Life_of_Walter_Mitty_2013_poster.jpg"
        },
        {
            "title": "Amélie",
            "description": "קסם פריזאי לנפש רגישה 💫",
            "image": "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg"
        }
    ],
    "neutral": [
        {
            "title": "Forrest Gump",
            "description": "החיים הם כמו קופסת שוקולדים 🍫",
            "image": "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg"
        }
    ]
}

def get_movie_by_mood(mood: str) -> dict:
    mood = mood.lower()
    if mood in MOVIE_RECOMMENDATIONS:
        return random.choice(MOVIE_RECOMMENDATIONS[mood])
    return random.choice(MOVIE_RECOMMENDATIONS["neutral"])
