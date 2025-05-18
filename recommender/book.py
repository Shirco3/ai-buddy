import random

BOOK_RECOMMENDATIONS = {
    "happy": [
        {
            "title": "The Alchemist – Paulo Coelho",
            "description": "סיפור הרפתקאות עם תובנות על החיים, חלומות וגורל ✨",
            "url": "https://www.goodreads.com/book/show/865.The_Alchemist"
        },
        {
            "title": "Atomic Habits – James Clear",
            "description": "ספר פרקטי ומרומם על איך לשנות הרגלים קטנים בגדול 🎯",
            "url": "https://jamesclear.com/atomic-habits"
        }
    ],
    "sad": [
        {
            "title": "Man's Search for Meaning – Viktor E. Frankl",
            "description": "מסע עמוק ומשמעותי שמראה איך למצוא תקווה במצבים הכי קשים 🌱",
            "url": "https://www.goodreads.com/book/show/4069.Man_s_Search_for_Meaning"
        },
        {
            "title": "The Power of Now – Eckhart Tolle",
            "description": "על חיבור לרגע הזה והשקטת המחשבות 😌",
            "url": "https://www.eckharttolle.com/power-of-now-excerpt/"
        }
    ],
    "neutral": [
        {
            "title": "Sapiens – Yuval Noah Harari",
            "description": "סקירה היסטורית מדהימה של האנושות 🧠",
            "url": "https://www.ynharari.com/book/sapiens/"
        }
    ]
}

def get_book_by_mood(mood: str) -> dict:
    mood = mood.lower()
    if mood in BOOK_RECOMMENDATIONS:
        return random.choice(BOOK_RECOMMENDATIONS[mood])
    return random.choice(BOOK_RECOMMENDATIONS["neutral"])
