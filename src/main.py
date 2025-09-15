import random
from typing import List, Tuple


def main():
    pass

def monty_hall_problem(switch_doors: bool) -> bool:
    """Simulates the Monty Hall problem.

    :param switch_doors: Whether to switch doors after the initial choice.
    :type switch_doors: bool
    :return: True if the contestant wins the car, False otherwise.
    :rtype: bool
    """
    mh_doors: List = ['Goat', 'Goat', 'Car']
    random.shuffle(mh_doors)
    initial_choice: int = random.choice(range(3))

    revealed_door: int = random.choice([i for i in range(3) if mh_doors[i] != 'Car' and i != initial_choice])

    if switch_doors:
        final_choice: int = [i for i in range(3) if i != initial_choice and i != revealed_door][0]
    else:
        final_choice: int = initial_choice
    
    return mh_doors[final_choice] == 'Car'


def simulate_mh_problem(num_of_times: int) -> Tuple[int, int]:
    """Simulates the Monty Hall problem multiple times.

    :param num_of_times: Number of times to simulate the problem.
    :type num_of_times: int
    :return: A tuple containing the number of wins without switching and the number of wins with switching.
    :rtype: Tuple[int, int]
    """
    num_wins_without_switching = sum(monty_hall_problem(False) for _ in range(num_of_times))
    num_wins_with_switching = sum(monty_hall_problem(True) for _ in range(num_of_times))
    
    return num_wins_without_switching, num_wins_with_switching

if __name__ == '__main__':
    main()
    