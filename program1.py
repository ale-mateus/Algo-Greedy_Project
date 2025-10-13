from typing import List, Tuple


def program1(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 1
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    ############################
    # Add you code here
    ############################
    total, indices = 0, []

    for i in range(n - 1, -1, -(k + 1)):
        total += values[i]
        indices.append(i + 1)

    return total, indices # replace with your code


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program1(n, k, values)

    print(m)
    for i in indices:
        print(i)