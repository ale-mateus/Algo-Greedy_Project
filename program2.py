from typing import List, Tuple

def program2(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Greedy solution to Program 2 (S2: unimodal values)

    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value (approx greedy result)
    List[int]: the indices of the chosen vaults (1-indexed)
    """

    ############################
    # Add you code here

    remainingVaults = set(range(n)) # all vaults are initially available
    chosenVaults = [] # list of chosen vault indices (1-indexed not starting from 0)

    while remainingVaults:
        # Get the index of the remaining vault with the highest value
        i = max(remainingVaults, key=lambda x: values[x])
        chosenVaults.append(i + 1)  # 1-indexed

        # remove all vaults within k distance while making sure we don't go out of bounds
        for j in range(max(0, i - k), min(n, i + k + 1)):
            remainingVaults.discard(j)

    chosenVaults.sort()
    total = 0
    for idx in chosenVaults:
        total += values[idx - 1]  # subtract 1 because chosenVaults is 1-indexed

    return total, chosenVaults

    ############################
    


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program2(n, k, values)

    print(m)
    for i in indices:
        print(i)
