import random

def random_walk(n):
    """Returns coordinates after n block random walk.
    Input Int
    Output Tuple"""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1),(0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x,y)

def walk_without_ride_home(number_of_walks, max_return_home):
    for walk_length in range(1,100):
        no_ride = 0
        longest_walk =0
        for i in range(number_of_walks):
            (x, y) = random_walk(number_of_walks)
            distance = abs(x)+ abs(y)
            if distance <= max_return_home:
                no_ride += 1
            no_ride_percentage = float(no_ride) / number_of_walks
        if no_ride_percentage > 0.5:
            longest_walk = walk_length
    return longest_walk

print(walk_without_ride_home(100, 4))
