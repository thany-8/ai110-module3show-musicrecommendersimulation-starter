"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:  # works as `python -m src.main` (from repo root) and `python src/main.py`
    from src.recommender import load_songs, recommend_songs
    from src.user_profile import user_profile
except ModuleNotFoundError:
    from recommender import load_songs, recommend_songs
    from user_profile import user_profile


def main() -> None:
    songs = load_songs("data/songs.csv")

    recommendations = recommend_songs(user_profile, songs, k=5)

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
