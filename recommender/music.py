import random

MUSIC_RECOMMENDATIONS = {
    "happy": [
        {
            "title": "Happy – Pharrell Williams",
            "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
        },
        {
            "title": "Can't Stop the Feeling – Justin Timberlake",
            "url": "https://www.youtube.com/watch?v=ru0K8uYEZWw"
        }
    ],
    "sad": [
        {
            "title": "Let It Be – The Beatles",
            "url": "https://www.youtube.com/watch?v=QDYfEBY9NM4"
        },
        {
            "title": "Someone Like You – Adele",
            "url": "https://www.youtube.com/watch?v=hLQl3WQQoQ0"
        }
    ],
    "neutral": [
        {
            "title": "Bohemian Rhapsody – Queen",
            "url": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ"
        }
    ]
}

def get_song_by_mood(mood: str) -> dict:
    mood = mood.lower()
    if mood in MUSIC_RECOMMENDATIONS:
        return random.choice(MUSIC_RECOMMENDATIONS[mood])
    return random.choice(MUSIC_RECOMMENDATIONS["neutral"])
