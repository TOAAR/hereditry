import random

def calculate_probabilities(data):
    probabilities = {}
    for _, row in data.iterrows():
        name = row['name']
        trait = row['trait']
        probabilities[name] = {
            'gene': {
                2: random.uniform(0.001, 0.3),
                1: random.uniform(0.3, 0.7),
                0: random.uniform(0.7, 1.0)
            },
            'trait': {
                True: random.uniform(0.1, 1.0),
                False: random.uniform(0.0, 0.9)
            }
        }
    return probabilities
