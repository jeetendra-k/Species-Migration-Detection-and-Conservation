def habitat_score(temp, rain, ndvi):
    # Normalize components
    rain_norm = rain / 1500
    temp_penalty = temp / 50

    score = (ndvi * 0.5) + (rain_norm * 0.3) - (temp_penalty * 0.2)
    
    return round(score, 3)