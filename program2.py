from typing import List, Tuple

def program2(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Optimized greedy solution to Program 2 (S2: unimodal values)
    Uses a boolean mask instead of rebuilding the vault list every iteration.
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

    total, indices = program2(n, k, values)
    print(total)
    for i in indices:
        print(i)
