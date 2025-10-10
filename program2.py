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
    # Greedy algorithm implementation

    remainingVaults = list(range(n))  # all vaults are initially available
    chosenVaults = []  # list of chosen vault indices (1-indexed)

    while remainingVaults:
        # Compare the first and last remaining vaults based on their values
        if values[remainingVaults[0]] >= values[remainingVaults[-1]]:
            i = remainingVaults[0]
        else:
            i = remainingVaults[-1]

        # Choose this vault (convert to 1-indexed)
        chosenVaults.append(i + 1)

        # Remove all vaults within k distance (inclusive)
        to_remove = set(range(max(0, i - k), min(n, i + k + 1)))
        remainingVaults = [v for v in remainingVaults if v not in to_remove]

    # Sort chosen vaults in ascending order
    chosenVaults.sort()

    # Calculate total value
    total = sum(values[idx - 1] for idx in chosenVaults)

    return total, chosenVaults

    ############################


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program2(n, k, values)

    print(m)
    for i in indices:
        print(i)
