# 🎵 Music Recommender Simulation

## Project Summary

This project is a small content-based music recommendation system built with Python.

The system compares songs from a CSV dataset with a predefined user taste profile. Each song receives a similarity score based on features such as genre, mood, energy, tempo, valence, danceability, and acousticness.

The songs with the highest scores are returned as recommendations. The program also explains why each song was selected, making the recommendation process easier to understand.

This project demonstrates how recommendation systems transform user preferences and item features into ranked predictions.

---

## How the System Works

The system uses a **content-based recommendation approach**.

Instead of comparing the user with other listeners, it compares each song directly with the user's preferred musical characteristics.

### Song Features

Each song in `songs.csv` contains the following information:

| Feature | Description |
|---|---|
| `id` | Unique identifier for the song |
| `title` | Name of the song |
| `artist` | Name of the artist |
| `genre` | Musical category, such as pop or reggaeton |
| `mood` | General feeling of the song, such as happy or relaxed |
| `energy` | How intense the song sounds, from `0.0` to `1.0` |
| `tempo_bpm` | Speed of the song in beats per minute |
| `valence` | How positive or cheerful the song sounds |
| `danceability` | How suitable the song is for dancing |
| `acousticness` | How acoustic the song sounds |

### User Profile

The user profile stores the listener's preferred genres, moods, and target values for the numerical features.

Example:

```python
user_profile = {
    "favorite_genres": ["pop", "reggaeton"],
    "favorite_moods": ["happy", "energetic"],
    "target_energy": 0.80,
    "target_tempo_bpm": 115,
    "target_valence": 0.85,
    "target_danceability": 0.80,
    "target_acousticness": 0.20
}
```

This profile represents a listener who prefers happy, energetic, danceable music with low acousticness.

---

## Algorithm Recipe

Each song begins with a score of `0`.

The recommender adds points based on how closely the song matches the user's profile.

### Categorical Features

```text
Genre match = 2.0 points
Mood match  = 2.0 points
```

Genre and mood receive higher weights because they strongly influence the type of music the listener expects.

The system may also award partial credit when a genre belongs to a related genre family. For example, `indie pop` may be considered related to `pop`.

### Numerical Features

The recommender compares these numerical features:

- Energy
- Tempo
- Valence
- Danceability
- Acousticness

For features measured from `0.0` to `1.0`, similarity is based on the absolute difference between the song value and the user's target.

```text
similarity = 1 - absolute difference
```

Example:

```text
User target energy = 0.80
Song energy        = 0.70

Difference         = |0.80 - 0.70| = 0.10
Energy similarity  = 1 - 0.10 = 0.90
```

A smaller difference produces a higher similarity score.

Tempo is normalized separately because it is measured in beats per minute instead of on a `0.0` to `1.0` scale.

### Final Ranking

After scoring every song, the system:

1. Calculates a score for each song.
2. Stores the reasons that contributed to the score.
3. Sorts the songs from highest score to lowest score.
4. Selects the top `k` songs.
5. Displays the song title, score, and explanation.

---

## System Flow

```text
songs.csv
    |
    v
Load song data
    |
    v
Read the user profile
    |
    v
Compare each song with the user's preferences
    |
    v
Calculate similarity scores
    |
    v
Sort songs from highest to lowest score
    |
    v
Return the top recommendations with explanations
```

---

## Project Structure

```text
AI_ENGINEEER PROJECT #3/
├── data/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── recommender.py
│   └── user_profile.py
├── tests/
├── .gitignore
├── ai_interactions.md
├── model_card.md
├── README.md
└── requirements.txt
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m src.main
```

---

## Running Tests

Run the test suite with:

```bash
pytest
```

The tests are located in:

```text
tests/test_recommender.py
```

---

## Sample Recommendation Output

```text
Top recommendations:

Sunrise City — Score: 0.96
Because: Recommended because 'pop' is a favorite genre; mood 'happy'
matches your taste; energy level is close to your target; positivity is
close to your target; tempo is close to your target; danceability is
close to your target; acousticness is close to your target.

Shape of You — Score: 0.91
Because: Recommended because 'pop' is a favorite genre; mood 'happy'
matches your taste; positivity is close to your target; danceability is
close to your target.

Happy — Score: 0.89
Because: Recommended because 'pop' is a favorite genre; mood 'happy'
matches your taste; energy level is close to your target; acousticness
is close to your target.
```

### Demo

Add a screenshot or video of the running project here.

```markdown
![Music recommender output](images/recommender-output.png)
```

---

## Experiments

### Experiment 1: Increasing the Genre Weight

I increased the genre weight to make exact genre matches more important.

This caused the system to recommend more songs from the user's favorite genres. However, it also reduced the variety of the recommendations because songs from other genres received lower scores even when their mood and numerical features were similar.

### Experiment 2: Adding Mood

Adding mood improved the recommendations because songs could match the emotional experience the user wanted.

For example, a happy song from a related genre could rank higher than an exact genre match with a very different mood.

### Experiment 3: Adding Numerical Features

Energy, tempo, valence, danceability, and acousticness helped the system distinguish between songs within the same genre.

For example, the system could separate energetic pop songs from calm or acoustic pop songs.

---

## Limitations and Risks

This system has several limitations:

- The dataset contains a small number of songs.
- Song features were manually labeled and may be subjective.
- Mood and genre do not always have one correct label.
- The system may over-prioritize genre and ignore songs from unfamiliar genres.
- A single user profile cannot represent every listening situation.
- A user may prefer different music while studying, exercising, relaxing, or attending a party.
- The system does not analyze song lyrics.
- The system does not learn from skips, likes, repeated plays, or listening history.
- Songs with missing or inaccurate feature values may receive unfair scores.
- The recommender may repeatedly suggest similar songs and reduce musical variety.

Because this is a content-based system, the quality of the recommendations depends heavily on the quality of the dataset and the selected feature weights.

---

## Reflection

This project helped me understand how a recommendation system converts information into a prediction. Each song is represented by features, and the user is represented by a taste profile. The system compares the two, calculates a score, and ranks the songs. I learned that changing a feature weight can significantly change the recommendations.

I also learned that bias can appear through manually selected labels and scoring rules. For example, giving genre too much weight may prevent the user from discovering songs from different genres that still match their preferred mood, energy, or danceability. A more advanced system could improve over time by learning from user likes, skips, ratings, and listening behavior.

For more details, see the project model card:

[**Model Card**](model_card.md)

---

## Future Improvements

Future versions of the project could:

- Allow the user to enter preferences through an interface.
- Learn from likes and dislikes.
- Create separate profiles for studying, exercising, and relaxing.
- Recommend songs from related genres.
- Prevent repeated recommendations.
- Use a larger and more diverse song dataset.
- Add a web interface using Flask or Streamlit.
- Connect to a music API for real song information.

---

## Technologies Used

- Python
- CSV
- Pytest
- Visual Studio Code
- Git and GitHub