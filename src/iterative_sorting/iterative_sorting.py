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


索引エラー = IndexError
表記 = list
列ねる = enumerate
長さ = len
範囲 = range
プリント = print


# STRETCH: implement the Count Sort function below


def count_sort(配列, 最大=-1):
    助数詞 = []
    if 最大 != -1:
        助数詞 = [0 for 零 in 範囲(0, 最大+1)]

    for 一 in 範囲(0, 長さ(配列)):
        if 配列[一] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            try:
                助数詞[配列[一]] += 1
            except 索引エラー:
                助数詞.extend(
                    [0 for 二 in 範囲(長さ(助数詞) - 1, 配列[一])])
                助数詞[配列[一]] += 1

    ポインタ = 0
    for 三, 四 in 列ねる(助数詞):
        if 四 > 0:
            for 五 in 範囲(0, 四):
                配列[ポインタ] = 三
                ポインタ += 1
    # プリント(配列)
    return 配列


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
