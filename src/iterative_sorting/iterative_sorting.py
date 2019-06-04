# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        start = arr[i]

        for j in range(i + 1, len(arr)):
            check = arr[j]

            if start > check:
                arr[i] = check
                arr[j] = start
                start = check

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    progress = 0

    def bubble_loop(arr):
        progress = 0
        for i in range(0, len(arr) - 1):
            apple = arr[i]
            orange = arr[i+1]

            if apple > orange:
                arr[i] = orange
                arr[i+1] = apple
            else:
                progress += 1

        return arr, progress

    while progress < (len(arr) - 1):
        arr, progress = bubble_loop(arr)
        # print(arr)

    # progress = 0
    # i = arr[0]
    # j = arr[1]
    # if j < i:
    #     arr[0] = j
    #     arr[1] = i
    # else:
    #     pass
    # progress += 1
    # ( so a for-loop )

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


if __name__ == '__main__':
    select_test = [5, 4, 3, 2, 1]
    selection_sort(select_test)
    bubble_test = [5, 4, 3, 2, 1]
    bubble_sort(bubble_test)
    print(select_test, bubble_test)
