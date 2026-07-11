# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## ## How the System Works

This project recommends songs by comparing each song’s musical features with the user’s preferences.

### 1. Song Features

Each `Song` contains information that describes how it sounds:

* **Genre:** The song’s musical category, such as pop, rock, reggaeton, or salsa.
* **Mood:** The main feeling of the song, such as happy, sad, relaxed, romantic, or energetic.
* **Energy:** How intense or active the song sounds, measured from `0.0` to `1.0`.
* **Tempo:** The speed of the song in beats per minute (`BPM`).
* **Valence:** How positive or cheerful the song sounds, measured from `0.0` to `1.0`.
* **Danceability:** How suitable the song is for dancing, measured from `0.0` to `1.0`.
* **Acousticness:** How acoustic the song sounds, measured from `0.0` to `1.0`.

For example, a song with high energy, high valence, and high danceability may be a good choice for a party or workout playlist.

### 2. User Profile

The `UserProfile` stores the user’s musical preferences.

It can include:

* Preferred genre
* Preferred mood
* Preferred energy level
* Preferred tempo
* Preferred valence
* Preferred danceability
* Preferred acousticness
* Songs the user has already liked

For example, a user may prefer:

```text
Genre: Pop
Mood: Happy
Energy: 0.80
Tempo: 120 BPM
Valence: 0.90
Danceability: 0.85
Acousticness: 0.20
```

### 3. Recommendation Score

The `Recommender` compares the user’s preferences with every song in the dataset.

For categorical features such as `genre` and `mood`, the song receives points when its value matches the user’s preference.

For numerical features such as `energy`, `tempo`, and `danceability`, the system calculates how close the song’s value is to the user’s preferred value. A smaller difference produces a higher score.

A simplified scoring system may look like this:

```text
Genre match          = 2 points
Mood match           = 2 points
Similar energy       = up to 1 point
Similar tempo        = up to 1 point
Similar valence      = up to 1 point
Similar danceability = up to 1 point
Similar acousticness = up to 1 point
```

Genre and mood receive more weight because they have a strong influence on the type of music the user wants to hear.

### 4. Selecting Recommendations

After calculating a score for every song, the system:

1. Calculates the similarity score for each song.
2. Sorts the songs from the highest score to the lowest score.
3. Removes songs the user has already heard or selected, when necessary.
4. Returns the top-scoring songs as recommendations.

For example, when the user requests happy, energetic, and danceable music, songs with high valence, energy, and danceability will receive better scores.

### System Flow

```text
Song CSV Dataset
       |
       v
Load Song Features
       |
       v
Read User Preferences
       |
       v
Compare Each Song With the UserProfile
       |
       v
Calculate a Recommendation Score
       |
       v
Sort Songs by Score
       |
       v
Return the Top Recommendations
```

This is a **content-based recommendation system** because it recommends songs based on their musical characteristics and how closely those characteristics match the user’s preferences.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



