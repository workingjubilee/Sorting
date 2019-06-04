# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):

#     return merged_arr

# [9, 8, 7, 4, 3, 5, 8, 9, 7, 1, 0, 2, 6, 3, 7]
# [9, 8, 7, 4, 3, 5, 8][9, 7, 1, 0, 2, 6, 3, 7]
# [9, 8, 7][4, 3, 5, 8]
# [9, 8][7]
# [9][8]


def cut_decks():

    return


def bridge_shuffle(cut_one, cut_two):
    len1, len2 = len(cut_one), len(cut_two)
    shuffled = [0] * (len1 + len2)
    print(len1, len2)
    print(shuffled)

    for i in range(len(shuffled)):
        print(i)
        if cut_one == []:
            print("finishing...")
            shuffled[i] = cut_two[0]
            del cut_two[0]
        elif cut_two == []:
            print("finishing...")
            shuffled[i] = cut_one[0]
            del cut_one[0]
        elif cut_one[0] > cut_two[0]:
            print(cut_one[0], "is greater than", cut_two[0])
            shuffled[i] = cut_two[0]
            del cut_two[0]
        elif cut_two[0] > cut_one[0]:
            print(cut_two[0], "is greater than", cut_one[0])
            shuffled[i] = cut_one[0]
            del cut_one[0]

    return shuffled

    # [1, 3][2, 4]


# TO-DO: implement the Merge Sort function below USING RECURSION


# def merge_sort(arr):

#     merge_sort(arr)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


if __name__ == '__main__':
    print(bridge_shuffle([1, 3], [2, 4]))
