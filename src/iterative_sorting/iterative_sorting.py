import copy
# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        start = arr[i]
        # print(arr)
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    # print(arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    def bubble_loop(arr):
        progress = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                progress += 1
        return arr, progress

    while True:
        arr, progress = bubble_loop(arr)
        # print(arr, progress)
        if progress >= (len(arr) - 1):
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


if __name__ == '__main__':
    def basic_tests(sort):
        test_dict = {
            "sorted_list": [1, 2, 3, 4, 5],
            "nearly_sorted": [1, 3, 2, 4, 5],
            "reversed_list": [5, 4, 3, 2, 1],
            "awkward_list": [5, 2, 3, 4, 1]}

        for k, v in test_dict.items():
            sort(v)
        return test_dict

    select_tests = basic_tests(selection_sort)
    bubble_tests = basic_tests(bubble_sort)
    count_tests = basic_tests(count_sort)

    # selects = selection_sort(copy(reversed_array))
    # bubble_test = [5, 4, 3, 2, 1]
    # bubble_sort(bubble_test)
    # bubble_test = [5, 4, 3, 2, 1]
    # print(select_test, bubble_test)
