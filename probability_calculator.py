import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        
        drawn_balls = random.sample(self.contents, num_balls)
        # Remove the drawn balls from the hat
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the drawn balls
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1
        
        # Check if all expected conditions are met
        meets_criteria = True
        for color, min_count in expected_balls.items():
            if drawn_count.get(color, 0) < min_count:
                meets_criteria = False
                break
        
        if meets_criteria:
            successful_experiments += 1
    
    return successful_experiments / num_experiments


# Solve the specific problem
if __name__ == "__main__":
    hat = Hat(blue=5, red=4, green=2)
    
    # We want at least 1 red ball AND at least 2 green balls
    probability = experiment(
        hat=hat,
        expected_balls={'red': 1, 'green': 2},
        num_balls_drawn=4,
        num_experiments=100000  # More experiments for better accuracy
    )
    
    print(f"Probability of drawing at least 1 red and 2 green balls from 4 draws: {probability:.6f}")
    print(f"As percentage: {probability * 100:.2f}%")

