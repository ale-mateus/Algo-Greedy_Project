from typing import List, Tuple


def program3(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]:
    """
    Solution to Program 3
    
    Parameters:
    n (int): number of vaults
    k (int): no two chosen vaults are within k positions of each other
    values (List[int]): the values of the vaults

    Returns:
    int:  maximal total value
    List[int]: the indices of the chosen vaults(1-indexed)
    """
    ############################    

    best_sum = 0
    best_choice = []

    def backtrack(i, last_index, current_sum, current_choice):
        nonlocal best_sum, best_choice

        # Base case: processed all vaults
        if i == n:
            if current_sum > best_sum:
                best_sum = current_sum
                best_choice = current_choice.copy()
            return

        # Option 1: Skip vault i
        backtrack(i + 1, last_index, current_sum, current_choice)

        # Option 2: Take vault i (if spacing allows)
        if i - last_index > k:
            current_choice.append(i + 1)  # store 1-indexed
            backtrack(i + 1, i, current_sum + values[i], current_choice)
            current_choice.pop()  # undo choice for recursion

    # Start recursion
    backtrack(0, -10**9, 0, [])

    return best_sum, best_choice

    ############################


if __name__ == '__main__':
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    m, indices = program3(n, k, values)

    print(m)
    for i in indices:
        print(i)