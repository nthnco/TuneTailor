import numpy as np
import pytest
from tunetailor.recommender.embedding_model import normalize_tempo, get_user_embedding


def test_normalize_tempo():
    features = {
        "valence": 0.8,
        "energy": 0.6, 
        "danceability": 0.7,
        "tempo": 120
    }
    
    result = normalize_tempo(features)
    
    # Check tempo normalization: (120 - 60) / (200 - 60) = 0.428
    assert abs(result[3] - 0.428) < 0.01
    # Check other features unchanged
    assert result[0] == 0.8  # valence
    assert result[1] == 0.6  # energy
    assert result[2] == 0.7  # danceability


def test_get_user_embedding():
    liked_tracks = [
        {"valence": 0.8, "energy": 0.5, "danceability": 0.7, "tempo": 120},
        {"valence": 0.6, "energy": 0.3, "danceability": 0.6, "tempo": 90},
        {"valence": 0.9, "energy": 0.7, "danceability": 0.8, "tempo": 130}
    ]
    
    embedding = get_user_embedding(liked_tracks)
    
    # Check shape
    assert embedding.shape == (4,)
    # Check valence average: (0.8 + 0.6 + 0.9) / 3 = 0.77
    assert abs(embedding[0] - 0.77) < 0.01
    # Check all values in reasonable range
    assert all(0 <= val <= 1 for val in embedding)


def test_normalize_tempo_edge_cases():
    # Test tempo at boundaries
    features_low = {"valence": 0.5, "energy": 0.5, "danceability": 0.5, "tempo": 60}
    features_high = {"valence": 0.5, "energy": 0.5, "danceability": 0.5, "tempo": 200}
    
    result_low = normalize_tempo(features_low)
    result_high = normalize_tempo(features_high)
    
    assert result_low[3] == 0.0  # Min tempo normalized to 0
    assert result_high[3] == 1.0  # Max tempo normalized to 1