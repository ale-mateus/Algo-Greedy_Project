from typing import List, Tuple

def program2(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Greedy solution to Program 2 (S2: unimodal values)

    Parameters:
    n (int): number of vaults
    k (int): no two chosenVaults vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value (approx greedy result)
    List[int]: the indices of the chosen vaults (1-indexed)
    """

    ############################
    # Add you code here

    remaining = set(range(n))
    chosen = []

    while remaining:
        # find the index of the largest value among remaining
        i = max(remaining, key=lambda x: values[x])
        chosen.append(i + 1)  # 1-indexed

        # remove all vaults within k distance
        for j in range(max(0, i - k), min(n, i + k + 1)):
            remaining.discard(j)

    chosen.sort()
    total = sum(values[i-1] for i in chosen)
    return total, chosen

    ############################
    


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program2(n, k, values)

    print(m)
    for i in indices:
        print(i)
