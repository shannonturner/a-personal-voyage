
""" A Personal Voyage - Drake Equation Minigame """

def drake_equation(
        rate_star_formation = 0,
        fraction_stars_with_planets = 0,
        average_goldilocks_per_star_with_planets = 0,
        planets_that_develop_life = 0,
        planets_with_life_develop_intelligence = 0,
        planets_with_technological_civilizations = 0,
        technological_civilizations_survive = 0
        ):


        # Courtesy of Wikipedia: 
    
        # Original estimates in 1961:
        
        # rate_star_formation = 1 / year
        # fraction_stars_with_planets = (0.2 to 0.5)
        # average_goldilocks_per_star_with_planets = (1 to 5)
        # planets_that_develop_life = 1 (100%)
        # planets_with_life_develop_intelligence = 1 (100%)
        # planets_with_technological_civilizations = (0.1 to 0.2)
        # technological_civilizations_survive = (1000 to 100,000,000 years)

        # Recent Estimates:

        # rate_star_formation = 7 / year
        # fraction_stars_with_planets = 1 (100%)
        # average_goldilocks_per_star_with_planets = (1 to 5)
        # planets_that_develop_life = 1 (100%)
        # planets_with_life_develop_intelligence = 1 (100%)
        # planets_with_technological_civilizations = (0.1 to 0.2)
        # technological_civilizations_survive = (1000 to 100,000,000 years)

        rate_star_formation = int(rate_star_formation) # per year
        fraction_stars_with_planets = float(fraction_stars_with_planets) # 0.1 - 1.0
        average_goldilocks_per_star_with_planets = int(average_goldilocks_per_star_with_planets) # 1 - 50
        planets_that_develop_life = int(planets_that_develop_life) # 1 - 100
        planets_with_life_develop_intelligence = int(planets_with_life_develop_intelligence) # 1 - 100
        planets_with_technological_civilizations = float(planets_with_technological_civilizations) # 0.1 - 1.0
        technological_civilizations_survive = int(technological_civilizations_survive) # 100 - 5,000,000,000

        return int(rate_star_formation * fraction_stars_with_planets * average_goldilocks_per_star_with_planets * planets_that_develop_life * planets_with_life_develop_intelligence * planets_with_technological_civilizations * technological_civilizations_survive)
