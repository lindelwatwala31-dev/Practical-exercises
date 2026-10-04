# Question 1.1

import math
def min_rooms_needed(num_guests:int) -> int:
    """
    Returns the minimum number of rooms needed to accommodate the given number of guests,
    where each room holds a maximum of 3 people.
    """
    if num_guests <= 0:
        return 0
    return math.ceil(num_guests / 3)




   