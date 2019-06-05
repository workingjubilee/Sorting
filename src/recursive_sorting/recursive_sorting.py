# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):

#     return merged_arr

# [9, 8, 7, 4, 3, 5, 8, 9, 7, 1, 0, 2, 6, 3, 7]
# [9, 8, 7, 4, 3, 5, 8][9, 7, 1, 0, 2, 6, 3, 7]
# [9, 8, 7][4, 3, 5, 8]
# [9, 8][7]
# [9][8]


def bridge_unshuffle(cut_one, cut_two):
    # print("accepting", cut_one, cut_two)
    len1, len2 = len(cut_one), len(cut_two)
    unshuffled = [0] * (len1 + len2)

    for i in range(len(unshuffled)):
        if cut_one == []:
            unshuffled[i] = cut_two[0]
            del cut_two[0]
        elif cut_two == []:
            unshuffled[i] = cut_one[0]
            del cut_one[0]
        elif cut_one[0] > cut_two[0]:
            # print(cut_one[0], "is greater than", cut_two[0])
            unshuffled[i] = cut_two[0]
            del cut_two[0]
        elif cut_two[0] > cut_one[0]:
            # print(cut_two[0], "is greater than", cut_one[0])
            unshuffled[i] = cut_one[0]
            del cut_one[0]

    # print("returning", unshuffled)
    return unshuffled


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(deck):
    if len(deck) <= 1:
        return deck
    else:
        cut_at = len(deck) // 2
        cut_one = merge_sort(deck[:cut_at])
        cut_two = merge_sort(deck[cut_at:])
        # print("cutting on:", cut_at, "getting:", cut_one, cut_two)
        deck = bridge_unshuffle(cut_one, cut_two)
        return deck


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
    print(bridge_unshuffle([1, 3], [2, 4]))
    print(merge_sort([4, 1, 3, 2]))
