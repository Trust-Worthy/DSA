from typing import Any

def binary_search(_list:list[int], target:int) -> int:
    """
    For binary search to work, _list must be sorted!

    Time complexity: O(log n)  ### Log base 2 of n ###

    Steps to implement algorithm:

    0) Sort the list if the list isn't already sorted
    1) Find the first index value and the last index value
    2) Find the midpoint using floor (or ceiling function)
    3) Evaluate midpoint against targest (best case scenario)
    4) Compare midpoint value to the target. If target is greater than the midpoint, cut out the bottom half of the list:
    4a) Assign first to (midpoint + 1), and repeat step 2
    5) If target is less than the midpoint, cut the top half of the list out:
    5a) Assign last to (midpoint - 1), and repeat step 2
    6) Repeat steps 2-5

    Args:
        list (list[Any]): _description_
        target (Any): _description_

    Returns:
        Any: _description_
    """
    
    first: int = 0
    last: int = len(_list) - 1 ### Getting the index value so must subtract by one because of zero indexing ###


    while first <= last:
        
        ### Calculate midpoint of the list ###
        midpoint: int = (first + last) // 2 # floor division --> rounds down to nearest whole number

        ### Best Case Scenario for binary_search ###
        if _list[midpoint] == target:
            return midpoint
        elif _list[midpoint] < target:

            ### Point first to value directly greater than the midpoint ###
            first = midpoint + 1
        else:
            ### Point last to the value direcly less than the midpoint ###
            last = midpoint - 1
    
    return None ### If the target isn't a member of the list
        

def verify(index: Any) -> None:
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers,12)
verify(result)

result = binary_search(numbers,6)
verify(result)

