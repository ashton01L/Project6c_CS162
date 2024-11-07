# Author: Ashton Lee
# Github User: ashton01L
# Date: 11/6/2024
# Description:Write a recursive function named is_subsequence that takes two string parameters and returns True if the
# first string is a subsequence of the second string, but returns False otherwise.
def is_subsequence(small, large):
    """
    Recursively checks if the first string (small) is a subsequence of the second string (large).

    :param:
        small (str): The string that to check as a subsequence.
        large (str): The string in which to check for the subsequence.

    :return:
        bool: True if 'small' is a subsequence of 'large', False otherwise.
    """
    # Base case 1: If 'small' is empty, it is a subsequence of any string
    if not small:
        return True

    # Base case 2: If 'large' is empty but 'small' is not, 'small' cannot be a subsequence
    if not large:
        return False

    # Recursive case: if the first characters match, move to the next character of both strings
    if small[0] == large[0]:
        return is_subsequence(small[1:], large[1:])

    # Otherwise, move to the next character of 'large' only
    return is_subsequence(small, large[1:])
