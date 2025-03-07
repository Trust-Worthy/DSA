from typing import Any, Optional

def linear_search(list:list[Any], target:Any) -> Any:
    """
    Searching for the position of target in the list. 

    Algorithm Must...
    1) return a value
    2) complete execution in a finite amount of time
    3) must output the same result for a given input set 

    Args:
        list (_type_): _description_
        target (_type_): _description_

    Returns: the index position of the target if found, else returns None
    """

    for i in range(0,len(list)): ### len(list) is a O(C) because python keeps track of the length of the list for us.
        if list[i] == target:
            return i
    return None

def verify(index: Any) -> None:
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers,12)
verify(result)

result = linear_search(numbers,6)
verify(result)

