import math

def calculate_elo(rating1, rating2, result, k_factor=40):
    expectation = (1.0 / (1.0 + pow(10, ((rating1 - rating2) / 400))))
    return round(rating1 + k_factor * (result - expectation), 2)
