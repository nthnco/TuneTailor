# TuneTailor

*A personalized Spotify recommender for all moods and music.*

---

## Overview

TuneTailor is a context-aware personalized playlist builder that helps users discover music tailored to their current mood, time of day, or activity. By leveraging Spotify’s rich audio features and user listening history, TuneTailor creates dynamic playlists that feel perfectly tuned to your moment.

---

## Features

- Fetches user playlists and liked songs via Spotify API  
- Extracts and utilizes audio features like tempo, valence, and energy  
- Builds user taste profiles based on listening history  
- Context-aware recommendations based on mood, time, or activity  
- Interactive UI for selecting context and exploring recommended tracks  
- (Planned) Integration with Spotify OAuth for real playlist syncing  

---

## Tech Stack

| Component       | Technology                   |
|-----------------|------------------------------|
| Data Collection | Spotify Web API, spotipy      |
| Data Processing | pandas, NumPy                 |
| Modeling        | scikit-learn, Faiss, UMAP     |
| Backend API     | FastAPI                      |
| Frontend UI     | Streamlit                   |
| Deployment      | Render / Vercel / Docker     |

---

## Getting Started

### Prerequisites

- Python 3.8+  
- Spotify Developer account & API credentials  

### Setup

```bash
git clone https://github.com/yourusername/tunetailor.git
cd tunetailor
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
