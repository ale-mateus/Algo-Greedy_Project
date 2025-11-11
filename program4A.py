from typing import List, Tuple


def program4A(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 4A
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    ############################
    memo = [-1] * (n + 1)   # memo[i] stores dp(i), -1 means "not computed"

    def dp(i: int) -> int:
        if i < 0:
            return 0
        if memo[i] != -1:
            return memo[i]

        max_compatible = 0
        for j in range(i - k - 1, -1, -1):  # check all previous vaults
            max_compatible = max(max_compatible, dp(j))

        memo[i] = values[i] + max_compatible
        return memo[i]

    # compute all dp values to ensure memo is filled
    for i in range(n):
        dp(i)

    # Find the best value and its ending index
    best_val = max(memo)
    best_i = memo.index(best_val)

    # Reconstruct chosen vaults
    chosen = []
    i = best_i
    while i >= 0:
        chosen.append(i + 1)
        i -= (k + 1)
    chosen.reverse()

    return best_val, chosen
    ############################


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program4A(n, k, values)

    print(m)
    for i in indices:
        print(i)