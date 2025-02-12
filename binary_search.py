from typing import Any

def binary_search(_list:list[int], target:int) -> int:
    """


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
    
        



