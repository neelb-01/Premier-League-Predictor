# Premier League Predictor

A machine learning project that predicts English Premier League outcomes with **XGBoost**. It is trained on match and team statistics scraped from [FBref](https://fbref.com/en/comps/9/Premier-League-Stats).

> **Status:** Early development. The scripts and structure below are planned and not built yet.

---

## Roadmap

The project is built in three phases. Each phase builds on the one before it.

- [ ] **Phase 1: Match result (H / D / A)**
  A multiclass XGBoost classifier that predicts whether a fixture ends in a home win, a draw, or an away win, with a probability for each outcome.
- [ ] **Phase 2: Exact scoreline**
  Two XGBoost regressors with a Poisson objective (`count:poisson`), one for home goals and one for away goals. Their expected-goal outputs give a scoreline probability matrix (e.g. P(2–1)). Result probabilities can then be derived from this matrix and compared with Phase 1.
- [ ] **Phase 3: Final league table**
  A Monte Carlo simulation of the remaining fixtures, run thousands of times with the Phase 2 scoreline probabilities. It produces projected points, a distribution of final positions, and title, top-four and relegation probabilities for each club.

---

## Data Source

All data comes from **FBref** (powered by Opta):

- Premier League fixtures and results (date, home/away teams, score, venue)
- Team match logs: shooting, passing, possession, defensive actions
- Expected goals: **xG** and **xGA**

### Scraping etiquette

- FBref rate-limits aggressive traffic. Keep to **at most one request every ~6 seconds**, or you risk a temporary IP ban.
- Cache raw HTML/CSV in `data/raw/` so each page is downloaded only once.
- Credit FBref and Opta as the data source in any output you publish.
- FBref's advanced-stat coverage can change over time. Treat the scraper as something that may need maintenance.

---

## Features (planned)

Every feature is computed from information available **before kick-off**, to avoid data leakage.

| Feature group      | Examples                                                         |
|--------------------|------------------------------------------------------------------|
| Rolling form       | Average goals, xG, xGA, shots, and possession over the last N matches |
| Venue              | Home/away indicator, home- and away-specific form                |
| Opponent strength  | Opponent's rolling form, Elo-style rating, previous season's finish |
| Schedule           | Rest days since the last match                                   |
| Head-to-head       | Recent results between the two clubs                             |

---

## Modelling & Evaluation

- **Time-based splits only.** Train on earlier seasons and test on later ones. Never shuffle matches randomly.
- **Baselines** to beat:
  - Always predict a home win
  - Bookmaker-implied probabilities (if odds data is added)

| Phase | Metrics |
|-------|---------|
| 1. Match result | Accuracy, log loss, Brier score |
| 2. Scoreline    | MAE on goals, exact-score hit rate, log loss on derived H/D/A |
| 3. League table | Points MAE and position error against the actual final table |

---

## Project Structure (proposed)

```
Premier-League-Predictor/
├── data/
│   ├── raw/            # Cached FBref pages / CSVs
│   └── processed/      # Cleaned match-level datasets with features
├── notebooks/          # Exploration and analysis
├── src/
│   ├── scrape.py       # Download and cache FBref data
│   ├── features.py     # Build pre-match features
│   ├── train.py        # Train XGBoost models
│   ├── predict.py      # Predict upcoming fixtures
│   └── simulate.py     # Monte Carlo season simulation (Phase 3)
├── models/             # Saved trained models
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
git clone <repo-url>
cd Premier-League-Predictor
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Core dependencies: `pandas`, `numpy`, `requests`, `beautifulsoup4`, `lxml`, `xgboost`, `scikit-learn`, `matplotlib`, `jupyter`.

### Usage (planned)

```bash
# 1. Scrape FBref data for a range of seasons
python src/scrape.py --seasons 2019-2025

# 2. Build features and train the model
python src/train.py

# 3. Predict upcoming fixtures
python src/predict.py

# 4. (Phase 3) Simulate the rest of the season
python src/simulate.py --runs 10000
```

---

## Disclaimer

This project is for **educational and research purposes only**. It is not betting advice. Football is unpredictable, so use the predictions at your own risk.
All match data belongs to FBref / Opta. Follow their terms of use.

## License

MIT (to be confirmed)
