import unittest
import importlib
import os
import sys

# Add the script's directory to the Python path to allow importing the module
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

# Dynamically import the module since its name is not a valid Python identifier
ball_classification = importlib.import_module("1_ball_classification")
MarvellousKNeighborsClassifier = ball_classification.MarvellousKNeighborsClassifier

class TestBallClassification(unittest.TestCase):
    def test_MarvellousKNeighborsClassifier(self):
        # Data from the script
        features = [[35,"rough"], [47,"rough"], [90,"smooth"], [48,"rough"],[90,"smooth"],[35,"rough"],[92,"smooth"],[35,"rough"],[35,"rough"],[35,"rough"],[96,"smooth"],[43,"rough"],[110,"smooth"],[35,"rough"],[95,"smooth"]]
        labels = ["tennis", "tennis", "cricket", "tennis", "cricket", "tennis", "cricket", "tennis", "tennis", "tennis", "cricket", "tennis", "cricket", "tennis", "cricket"]
        
        # The function has a hardcoded prediction for [97, 1] which is [97, 'smooth']
        # Based on the data, this should be a cricket ball.
        # The labels are ["tennis", "cricket", ...]. LabelEncoder will encode "cricket" as 0 and "tennis" as 1.
        # The prediction for a smooth heavy ball should be "cricket", which is encoded as 0.
        prediction = MarvellousKNeighborsClassifier(features, labels)
        self.assertEqual(prediction[0], 0)

if __name__ == '__main__':
    # Add the script's directory to the python path to allow running the test directly
    # This is redundant if the test is run with `python -m unittest discover`
    # but it allows running the script directly
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    unittest.main()