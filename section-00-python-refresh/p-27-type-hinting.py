from typing import List

# the -> tells that the function returns a float
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

list_avg([2, 6, 7])
