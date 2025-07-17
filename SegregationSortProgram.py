# 1. Name:
#      Spencer Palmer
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      This program will take an array of numbers in any order and organize the array from smallest number to largest number
#      by creating two pointers and a pivot point to locate and swap values depending on if they are smaller or larger than the pivot point value.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting
# 5. How long did it take for you to complete the assignment?
#      Total time after reading, designing, writing, testing, and troubleshooting the project I spent roughly 5 hours on this project.

def read():
    '''
        Reads in an array of random numbers from 1 to 20 and returns them to the caller.
    '''
    array = [12, 1, 3, 9, 4, 16, 5, 18, 10, 11, 20, 17, 7, 8, 15, 6, 2, 19, 13, 14]
    return array

def segregate(data, index_start, index_end):
    '''
        Takes the array and starting pointers of the array, creates a pivot point, and uses that pivot point as a refrence to 
        sort the array.
    '''
    original_start = index_start
    original_end = index_end

    if index_start == index_end:
        return data
    elif data[index_start] == data[index_end]:
        return data
    
    index_pivot = int(((index_start + 1) + index_end) / 2)

    while index_start < index_end:
        while data[index_start] <= data[index_pivot] and index_start < len(data) - 1:
            index_start += 1
        while data[index_end] >= data[index_pivot] and index_end > 0:
            index_end -= 1

        if index_start < index_end:
            data[index_start], data[index_end] = data[index_end], data[index_start]

    if data[index_start] > data[index_pivot]:
        data[index_start - 1], data[index_pivot] = data[index_pivot], data[index_start - 1]
        index_pivot = index_start - 1
    else:
        data[index_start], data[index_pivot] = data[index_pivot], data[index_start]

    # data = segregate(data, original_start, index_pivot - 1)
    # data = segregate(data, index_pivot + 1, original_end)

    return index_pivot, data

def sort(array):
    '''
        Takes the given array and sorts them into order from smallest to largest. It calls the segregate function to perform the 
        task of moving values.
    '''
    data = array
    index_start = 0
    if len(data) == 0:
        index_end = 0
    else:
        index_end = len(data) - 1
    data = segregate(data, index_start, index_end)

    return data

# def segregate_recursion(data, index_start, index_end):
#     original_start = index_start
#     original_end = index_end

#     index_pivot, data = segregate(data, index_start, index_end)

#     for i in range(len(data)):
#         index_pivot, data = segregate(data, original_start, index_pivot - 1)
#         index_pivot, data = segregate(data, index_pivot + 1, original_end)
#         i += 1

#     return data

def main():
    '''
        Main function that gets the array and passes it to the sort function then displaying the results.
    '''

    array = read()
    print(sort(array)) 

def test_cases():
    '''
        Test Cases to check for possible errors
    '''

    # Empty
    try:
        assert sort([]) == [], '\nError testing "Empty", expected output: []'
        print('\n----Test "Empty" Passed!----')
    except Exception as e:
        print(e)

    # Single Item
    try:
        assert sort([15]) == [15], '\nError testing "Single Item", expected output: [15]'
        print('\n----Test "Single Item" Passed!----')
    except Exception as e:
        print(e)

    # Multiple Items
    try:
        results = sort([1, 10, 8, 3, 5, 9, 6])
        assert sort([1, 10, 8, 3, 5, 9, 6]) == [1, 3, 5, 6, 8, 9, 10], '\nError testing "Multiple Items", expected output: [1, 3, 5, 6, 8, 9, 10]'
        print('\n----Test "Multiple Items" Passed!----')
    except Exception as e:
        print(e)
        print(f"Results: {results}")

    # Largest Value in Middle
    try:
        results = sort([1, 3, 8, 10, 5, 9, 6])
        assert sort([1, 3, 8, 10, 5, 9, 6]) == [1, 3, 5, 6, 8, 9, 10], '\nError testing "Largest Value in Middle", expected output: [1, 3, 5, 6, 8, 9, 10]'
        print('\n----Test "Largest Value in Middle" Passed!----')
    except Exception as e:
        print(e)
        print(f"Results: {results}")

    # Smallest Value in Middle
    try:
        results = sort([10, 3, 8, 1, 5, 9, 6])
        assert sort([10, 3, 8, 1, 5, 9, 6]) == [1, 3, 5, 6, 8, 9, 10], '\nError testing "Smallest Value in Middle", expected output: [1, 3, 5, 6, 8, 9, 10]'
        print('\n----Test "Smallest Value in Middle" Passed!----')
    except Exception as e:
        print(e)
        print(f"Results: {results}")

    # Duplicate Values
    try:
        results = sort([1, 3, 8, 10, 5, 9, 3])
        assert sort([1, 3, 8, 10, 5, 9, 3]) == [1, 3, 3, 5, 8, 9, 10], '\nError testing "Duplicate Values", expected output: [1, 3, 3, 5, 8, 9, 10]'
        print('\n----Test "Duplicate Values" Passed!----')
    except Exception as e:
        print(e)
        print(f"Results: {results}")


if __name__ == "__main__":
    # main()
    test_cases()