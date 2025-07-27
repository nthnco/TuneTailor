import numpy as np
from typing import List, Dict, Any

def normalize_tempo(features: Dict[str, float]) -> np.ndarray:
    """
    Normalize the tempo feature, all other features should already be between 0-1

    Args:
        features (Dict[str, float]): _description_

    Returns:
        np.ndarray: _description_
    """
    normalized_features = []
    bpm = features['tempo']
    features['tempo'] = (bpm - 60) / (200 - 60)
    for i in features.values():
        normalized_features.append(i)
    return np.array(list(normalized_features))
    
def get_user_embedding(liked_tracks: List[Dict[str, Any]]) -> np.ndarray:
    """
    create a numerical representation of the 
    user's music taste by analyzing their liked tracks.
    Args:
        liked_tracks (List[Dict[str, Any]]): all liked tracks from user

    Returns:
        np.ndarray: user embedding vector of overall music tastes
    """
    all_vectors = []
    for i in liked_tracks:
        normalized_arr = normalize_tempo(i)
        all_vectors.append(normalized_arr)
    return np.mean(np.array(all_vectors), axis = 0)
    