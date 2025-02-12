from typing import Any, Optional

def linear_search(list:list[Any], target:Any) -> Any:``
    """
    Searching for the position of target in the list 

    Args:
        list (_type_): _description_
        target (_type_): _description_

    Returns: the index position of the target if found, else returns None
    """

    for i in range(0,len(list)): ### len(list) is a O(C) because python keeps track of the length of the list for us.
        if list[i] == target:
            return i
    return None