import random


class Environment:
    """
        A class to simulate the environment for a humanoid robot,
        including obstacle detection.
    """
    def detect_obstacle(self):
        """
        Simulate the detection of an obstacle.

        Returns:
            bool: True if an obstacle is detected, False otherwise.
        """
        return random.choice([True, False])
