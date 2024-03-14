import random


def roll_dice():
    roll = int(
        random.gauss(mu=15, sigma=10)
    )  # Gaussian distribution centered at 20 with a standard deviation of 5
    roll = max(5, roll)  # Ensure the roll is at least 5
    roll = min(20, roll)  # Ensure the roll does not exceed 20
    return roll


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))
