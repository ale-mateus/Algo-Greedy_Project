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
        if i >= n:
            return 0

        # If computed before, return stored value
        if memo[i] != -1:
            return memo[i]

        # Option 1: skip vault i
        skip = dp(i + 1)

        # Option 2: take vault i
        take = values[i] + dp(i + k + 1)

        # Store and return best
        memo[i] = max(skip, take)
        return memo[i]

    # Reconstruct chosen vaults
    chosen = []
    i = 0
    while i < n:
        # If taking vault i leads to the dp result, we choose it
        if dp(i) == values[i] + dp(i + k + 1):
            chosen.append(i + 1)
            i += k + 1
        else:
            i += 1

    return dp(0), chosen
    ############################



if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program4A(n, k, values)

    print(m)
    for i in indices:
        print(i)