def any7(nums):
    # """Are any of these numbers a 7? (True/False)"""
    
    # # YOUR CODE HERE
    list_nums = nums
    find_num = 7
    for num in list_nums:
        if (find_num == num):
            return True
    return False
print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

