def generate_detailed_explanation(temp, rain, ndvi, population):

    explanation = ""

    explanation += "ELEPHANT MIGRATION ANALYSIS REPORT\n"
    explanation += "----------------------------------\n\n"

    explanation += f"The current environmental conditions indicate a temperature of {temp}°C, rainfall of {rain} mm, and vegetation index (NDVI) of {ndvi}. "
    explanation += f"The estimated elephant population in this region is approximately {population} individuals.\n\n"

    # Temperature Analysis
    if temp > 32:
        explanation += "High temperature conditions suggest thermal stress on elephant populations. Elephants typically respond to such heat by migrating toward cooler and more shaded forest regions, often moving northward or toward dense canopy areas. Prolonged exposure to such temperatures may also reduce water retention and increase dependency on nearby water bodies.\n\n"
    elif temp < 20:
        explanation += "Lower temperature conditions indicate relatively comfortable thermal conditions for elephants. Migration due to temperature stress is unlikely; however, movement may still occur due to other ecological factors such as food availability or human disturbance.\n\n"
    else:
        explanation += "Moderate temperature conditions provide a relatively stable environment. Temperature alone is not a strong driver of migration in this scenario, allowing other ecological factors to dominate movement decisions.\n\n"

    # Rainfall Analysis
    if rain < 800:
        explanation += "Low rainfall levels indicate potential water scarcity. This significantly influences elephant migration, as elephants require large amounts of water daily. Under such conditions, herds tend to move toward river basins, wetlands, or regions with higher precipitation.\n\n"
    elif rain > 1200:
        explanation += "High rainfall suggests abundant water availability, which supports stable habitats. However, excessive rainfall may lead to flooding in low-lying regions, temporarily displacing elephant populations to slightly elevated terrains.\n\n"
    else:
        explanation += "Moderate rainfall levels indicate sufficient water availability. This supports habitat stability and reduces the urgency for migration driven by water needs.\n\n"

    # NDVI Analysis (Vegetation)
    if ndvi < 0.3:
        explanation += "Low NDVI values indicate sparse vegetation and limited food resources. This is a major driver of migration, as elephants require substantial vegetation for sustenance. Herds are likely to move toward forested regions with higher vegetation density.\n\n"
    elif ndvi > 0.5:
        explanation += "High NDVI values reflect dense vegetation and abundant food supply. Such conditions support stable elephant populations and reduce the need for migration.\n\n"
    else:
        explanation += "Moderate NDVI levels suggest adequate but not abundant vegetation. Elephants may exhibit partial or seasonal migration to optimize food availability.\n\n"

    # Population Pressure
    if population > 1800:
        explanation += "A high population density increases competition for resources such as food and water. This often triggers dispersal behavior, where smaller groups branch out to reduce pressure on the habitat.\n\n"
    elif population < 800:
        explanation += "Lower population density reduces competition and allows elephants to remain within a localized region without significant migration pressure.\n\n"
    else:
        explanation += "Moderate population levels indicate balanced resource usage, with migration influenced more by environmental conditions than competition.\n\n"

    # Combined Ecological Interpretation
    explanation += "When considering all environmental factors together, elephant migration emerges as a survival-driven response to changing ecological conditions. Elephants are highly intelligent and adaptive animals that rely on memory and social learning to navigate landscapes. Their movement patterns are rarely random and are instead guided by known migration corridors, water sources, and forest cover.\n\n"

    explanation += "In realistic ecological scenarios, elephants avoid extreme terrains such as mountainous regions, glaciers, and urbanized zones. Their migration is typically confined to forest corridors and plains where food and water are accessible. The presence of human settlements, agricultural land, and infrastructure also plays a significant role in shaping movement patterns, often leading to human-elephant conflict zones.\n\n"

    explanation += "Overall, the observed migration pattern in this simulation reflects a combination of climatic stress, vegetation availability, and population dynamics. Future environmental changes, particularly those driven by climate change, may further intensify these migration behaviors, making it essential to monitor and manage elephant habitats effectively.\n"

    return explanation