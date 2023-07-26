from random import choice

class RandomWalk:
    """A class to gnerate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for a step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        return direction * distance
    
    def fill_walk(self):
        """Caluculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go, and how far to go.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                """If the values of both x_step and y_step are 0, the walk doesn’t go anywhere; when this happens, we continue the loop"""
                continue

            # Calcuate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            """To get the next x-value for the walk, we add the value in x_step to the last value stored in x_values,
             and do the same for the y-values."""

            self.x_values.append(x)
            self.y_values.append(y)