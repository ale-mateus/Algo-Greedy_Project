from typing import List, Tuple

def program2(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 2

    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int: maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """

    # Boolean list to mark available vaults
    available = [True] * n
    chosenVaults = []
    left, right = 0, n - 1

    while left <= right:
        # Move pointers until we find available vaults
        while left <= right and not available[left]:
            left += 1
        while right >= left and not available[right]:
            right -= 1

        # If pointers cross, break
        if left > right:
            break

        # Greedy choice: compare values at the ends
        if values[left] >= values[right]:
            i = left
        else:
            i = right

        # Choose vault (1-indexed)
        chosenVaults.append(i + 1)

        # Block all vaults within k distance
        for j in range(max(0, i - k), min(n, i + k + 1)):
            available[j] = False

    # Compute total value
    total = sum(values[idx - 1] for idx in chosenVaults)
    chosenVaults.sort()

    return total, chosenVaults


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program2(n, k, values)
    
    print(m)
    for i in indices:
        print(i)
