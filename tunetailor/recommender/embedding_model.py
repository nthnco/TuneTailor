import numpy as np
from typing import List, Dict, Any

def normalize_features(features: Dict[str, float]) -> np.ndarray:
    """
    Normalize function

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
    return np.array(normalized_features)
    
def get_user_embedding(liked_tracks: List[Dict[str, Any]]) -> np.ndarray:
    # YOUR CODE HERE  
    pass