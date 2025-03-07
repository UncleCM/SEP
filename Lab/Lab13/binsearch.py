# binsearch.py
class InvalidArgument(Exception):
    pass

def binsearch(dataList, key):
    # Check if dataList is a list
    if not isinstance(dataList, list):
        raise InvalidArgument("The first argument must be a list.")
    
    # Check for empty list
    if not dataList:
        return None
    
    low = 0
    high = len(dataList) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Integer division
        try:
            if dataList[mid] == key:
                return mid
            elif dataList[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        except TypeError:
            # If comparison fails due to type mismatch
            raise InvalidArgument("List elements must be comparable with the key.")
    
    return None  # Key not found