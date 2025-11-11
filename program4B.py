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

    
    if n == 0:
        return 0, []

    # dp[i] corresponds to vault i (0-indexed internally)
    dp = [0] * n
    prev = [-1] * n   # for reconstruction

    # Fill DP table
    for i in range(n):
        dp[i] = values[i]  # option: start new chain at vault i
        prev[i] = -1

        # Check all previous vaults j < i
        for j in range(i):
            if i - j > k:  # spacing constraint
                if dp[j] + values[i] > dp[i]:
                    dp[i] = dp[j] + values[i]
                    prev[i] = j

    # Find best ending vault
    best_sum = 0
    best_last = -1
    for i in range(n):
        if dp[i] > best_sum:
            best_sum = dp[i]
            best_last = i

    # Reconstruct chosen vaults
    indices = []
    i = best_last
    while i != -1:
        indices.append(i + 1)  # convert to 1-indexed
        i = prev[i]

    indices.reverse()
    return best_sum, indices

if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program4B(n, k, values)

    print(m)
    for i in indices:
        print(i)