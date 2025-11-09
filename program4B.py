from typing import List, Tuple


def program4B(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 4B
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """

    dp = [0] * (n + 1)
    choice = [False] * (n + 1)

    for i in range(1, n + 1):
        # Option 1: skip current vault
        skip = dp[i - 1]
        # Option 2: pick current vault
        prev = i - k - 1
        pick = values[i - 1] + (dp[prev] if prev >= 0 else 0)

        # Choose the better option
        if pick > skip:
            dp[i] = pick
            choice[i] = True
        else:
            dp[i] = skip

    # Reconstruct chosen vault indices
    indices = []
    i = n
    while i > 0:
        if choice[i]:
            indices.append(i)
            i -= (k + 1)
        else:
            i -= 1

    indices.reverse()
    return dp[n], indices

if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program4B(n, k, values)

    print(m)
    for i in indices:
        print(i)