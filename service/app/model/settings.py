import numpy as np

MEAN = np.array([0.485, 0.456, 0.406])
STD = np.array([0.229, 0.224, 0.225])

TATTOO_TYPE_MAPPING = {
    'Traditional': 0,
    'New school': 1,
    'Realism': 2,
    'Engraving': 3,
    'Japanese': 4,
    'Chicano': 5,
    'Minimalist': 6,
    'Linework': 7,
    'Other': 8,
}

NUM_TO_TYPE = {
    0: 'Traditional',
    1: 'New school',
    2: 'Realism',
    3: 'Engraving',
    4: 'Japanese',
    5: 'Chicano',
    6: 'Minimalist',
    7: 'Linework',
    8: 'Other'
 }
