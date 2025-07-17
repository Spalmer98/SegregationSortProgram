# 1. Name:
#      Spencer Palmer
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      This program will take an array of numbers in any order and organize the array from smallest number to largest number
#      by creating two pointers and a pivot point to locate and swap values depending on if they are smaller or larger than the pivot point value.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the recursion to work without entering an infinite loop. I had to review and refrence the solution design and realized
#      that trying to do the recursion in the segregate function was causing an infinite loop because it wasn't moving on through the code. I refrenced the 
#      design solution and implemented the sort_recursion function which exits the function once the pointers are in the same location. This way, when the recursion
#      happens, it has a condition that ends the loop and moves on to the next part of the program.
# 5. How long did it take for you to complete the assignment?
#      Total time after reading, designing, writing, testing, and troubleshooting the project I spent roughly 5 hours on this project.

import os, random

def read():
    '''
        Reads in an array of random numbers from 1 to 20 and returns them to the caller.
    '''

    # Define the range and the desired number of items in array
    min_value = 1
    max_value = 20
    num_items = 20

    # Generate the list using a random integer function from the random library
    array = [random.randint(min_value, max_value) for _ in range(num_items)]

    return array

def segregate(data, index_start, index_end):
    '''
        Takes the array and start/end pointers of the array, creates a pivot pointer, and uses that pivot point as a refrence to 
        sort the array. Placing all the values smaller than the value at the pivot point to the left and all the values larger
        than the pivot point to the right and returning an index value back to the calling function for a new pivot point.
    '''
    # If the start pointer and the end pointer are the same then the item is in the correct spot
    # and return the start pointer for the new pivot point
    if index_start == index_end:
        return index_start
    
    # Create a pivot point that is always the middle (rounding down) of the array that is being sorted
    index_pivot = int(((index_start + 1) + index_end) / 2)

    # Itterate through the array to locate any items larger and smaller than the value of the item at the pivot point
    while index_start < index_end:
        while data[index_start] <= data[index_pivot] and index_start < index_end:
            index_start += 1
        while data[index_end] >= data[index_pivot] and index_start < index_end:
            index_end -= 1

        # If the start pointer is less than the end pointer than the value at the start pointer is greater than
        # the value at the pivot pointer and the value at the end pointer is less than the value at the pivot pointer 
        # so swap the values at the start and end pointers so the smaller value is to the left of the pivot pointer and 
        # the larger value is to the right of the pivot pointer
        if index_start < index_end:
            data[index_start], data[index_end] = data[index_end], data[index_start]

    # If the value at the start pointer (scanning for values larger than the pivot) is greater than the value at the pivot pointer
    # and the start pointer is greater than the pivot pointer then reduce the start pointer by 1
    # This is allowing the program to place the pivot value to the left of the larger value (start pointer) at line 63
    if data[index_start] > data[index_pivot] and index_start > index_pivot:
        index_start -= 1

    # Swaping the values within the array placing the value at the pivot point in it's correct/sorted location in the array
    data[index_start], data[index_pivot] = data[index_pivot], data[index_start]

    # Return the start pointer because this is going to be the new pivot pointer
    return index_start

def sort(array):
    '''
        Takes the given array and finds the beginning and end of that array to use later for the starting pointers and passes
        the information to the sort_recursion function.
    '''

    # Set the start and end pointer values
    start = 0
    end = len(array) - 1

    # Call the recursion function to run through and continue sorting until the array is sorted smallest to largest
    sort_recursion(array, start, end)

    # Return the array
    return array

def sort_recursion(data, start, end):
    '''
        Takes the given array and start, end perameters and passes them into the segregate function in a recursive manner to
        repeat steps until the array gets sorted.
    '''

    # If the end pointer is less than 0 or the end pointer minus the start pointer is less than 1 then the array either contains 
    # no items, or the pointers are the same so the value is in the correct location in the array so return to the calling function
    if end < 0 or end - start < 1:
        return

    # Run the segregate function and store the value returned as the pivot pointer
    index_pivot = segregate(data, start, end)

    # Call this function within itself to continue sorting the left and right of the pivot point by passing in the returned pivot pointer
    # and adding or subracting 1 to it which gives the start or end pointer for the next round of sorting.
    sort_recursion(data, start, index_pivot -1)
    sort_recursion(data, index_pivot + 1, end)

    # No return neccessary since we are manipulating the array passed in from the sort function

def clear_screen():
    '''
        Clears the screen to keep the output looking clean.
    '''

    # Check the operating system
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Linux and macOS
        _ = os.system('clear')

def main():
    '''
        Main function that gets the array and passes it to the sort function then displaying the results.
    '''

    # Clears the screen
    clear_screen()

    # Gets the array that will be used
    array = read()

    # Displays the results of the sorting program
    print(f"\n{sort(array)}") 

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
    main()
    # test_cases()
    print()