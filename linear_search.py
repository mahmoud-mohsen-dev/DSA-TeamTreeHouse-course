def linear_search(list, target):
    """
        Returns the index position of the target if found, else returns None
    """
    
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

# res = linear_search([2,1,2,3,4,5], 3)



def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

res = linear_search(numbers, 12)
verify(res)

res = linear_search(numbers, 6)
verify(res)

# this code has a run time equal O(n)