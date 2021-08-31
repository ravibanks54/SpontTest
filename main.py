import copy
from collections import deque

"""
Problem Statement:
Implement linear search in a language of your choice. Linear search is a way to find a target value within a list—it
checks each element in a list and sees if it matches a certain value.
Please include the language in a comment at the top of the file, I may not be familiar!

Returns index in array of search_term if found. Otherwise returns -1.
"""


def linear_search(array, search_term) -> int:
    for idx, value in enumerate(array):
        if value == search_term:
            return idx
    return -1


"""
Problem Statement:
Write a function which returns a boolean depending on if the string input is a palindrome. 
It should ignore capitalization and whitespace.

Returns True if input is a palindrome, otherwise returns False. Empty strings are not considered palindromes.
Note: This is trivial with Python's built-in reverse method. I've chosen not to use it here.
"""


def is_palindrome(word: str) -> bool:
    word = word.upper()
    word = word.replace(" ", "")
    if len(word) == 0:
        return False
    for i in range(int(len(word) / 2)):
        char = word[i]
        reverse_char = word[len(word) - 1 - i]
        if char != reverse_char:
            return False
    return True


"""
Problem Statement:
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. 
For example, the below matrix contains 5 islands:
Implement a function which returns the correct number of islands given a matrix with a recursive approach.
Same function with an iterative approach.
"""


def islands_recursive(arr):
    island_count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # Iterate until you find a 1.
            # Zero it out
            # Then find all neighbors that are also 1 and 0 them out
            if arr[i][j] == 1:
                visit_island_recursive(arr, i, j)
                island_count += 1
    return island_count


def visit_island_recursive(arr, i, j):
    if indices_out_of_bounds(arr, i, j):
        return
    if arr[i][j] == 0:
        return
    arr[i][j] = 0
    # Top Left
    visit_island_recursive(arr, i - 1, j - 1)
    # Top
    visit_island_recursive(arr, i - 1, j)
    # Top Right
    visit_island_recursive(arr, i - 1, j + 1)
    # Left
    visit_island_recursive(arr, i, j - 1)
    # Right
    visit_island_recursive(arr, i, j + 1)
    # Bottom Left
    visit_island_recursive(arr, i + 1, j - 1)
    # Bottom
    visit_island_recursive(arr, i + 1, j)
    # Bottom Right
    visit_island_recursive(arr, i + 1, j + 1)


def indices_out_of_bounds(arr, i, j) -> bool:
    return i < 0 or j < 0 or i >= len(arr) or j >= len(arr[i])


def islands_iterative(arr) -> int:
    island_count = 0
    queue = deque()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # Iterate until you find a 1.
            # Zero it out
            # Then queue all neighbors that are also 1 and zero them out as well
            if arr[i][j] == 1:
                queue.append((i, j))
                while len(queue) > 0:
                    i, j = queue.popleft()
                    arr[i][j] = 0
                    if not indices_out_of_bounds(arr, i - 1, j - 1) and arr[i - 1][j - 1] == 1:
                        queue.append((i - 1, j - 1))
                    if not indices_out_of_bounds(arr, i - 1, j) and arr[i - 1][j] == 1:
                        queue.append((i - 1, j))
                    if not indices_out_of_bounds(arr, i - 1, j + 1) and arr[i - 1][j + 1] == 1:
                        queue.append((i - 1, j + 1))
                    if not indices_out_of_bounds(arr, i, j - 1) and arr[i][j - 1] == 1:
                        queue.append((i, j - 1))
                    if not indices_out_of_bounds(arr, i, j + 1) and arr[i][j + 1] == 1:
                        queue.append((i, j + 1))
                    if not indices_out_of_bounds(arr, i + 1, j - 1) and arr[i + 1][j - 1] == 1:
                        queue.append((i + 1, j - 1))
                    if not indices_out_of_bounds(arr, i + 1, j) and arr[i + 1][j] == 1:
                        queue.append((i + 1, j))
                    if not indices_out_of_bounds(arr, i + 1, j + 1) and arr[i + 1][j + 1] == 1:
                        queue.append((i + 1, j + 1))
                island_count += 1
    return island_count


island_test_1 = [
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

island_test_2 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

island_test_3 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]

island_test_4 = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

if __name__ == '__main__':
    assert linear_search(["hello", "world"], "world") == 1
    assert linear_search(["hola", "mundo"], "hello") == -1
    assert linear_search([], "hello") == -1
    assert is_palindrome("racecar")
    assert is_palindrome("Ka Y a K")
    assert is_palindrome("k")
    assert not is_palindrome("")
    assert not is_palindrome(" hello world ")
    assert islands_recursive(copy.deepcopy(island_test_1)) == 5
    assert islands_recursive(copy.deepcopy(island_test_2)) == 0
    assert islands_recursive(copy.deepcopy(island_test_3)) == 1
    assert islands_recursive(copy.deepcopy(island_test_4)) == 5
    assert islands_iterative(copy.deepcopy(island_test_1)) == 5
    assert islands_iterative(copy.deepcopy(island_test_2)) == 0
    assert islands_iterative(copy.deepcopy(island_test_3)) == 1
    assert islands_iterative(copy.deepcopy(island_test_4)) == 5
    print("Completed successfully.")
