"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs
import src.recommender

print("Recommender loaded from:")
print(src.recommender.__file__)


def main() -> None:
    songs = load_songs("data/songs.csv") 

  # User taste profile: one target value per feature identified in Step 1.
    # Keys mirror the UserProfile dataclass so the dict and OOP paths stay consistent.
    user_prefs = {
        "favorite_genre": "pop",      # matched exactly or by family (pop-family = 17/30 songs)
        "favorite_mood": "happy",     # used for mood match + explanations
        "target_energy": 0.8,         # closeness-scored on a 0-1 scale
        "target_valence": 0.85,       # "happy" songs average ~0.86 valence in this catalog
        "likes_acoustic": False,      # maps to acousticness (low weight; ~-0.87 corr. with energy)
    }
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
