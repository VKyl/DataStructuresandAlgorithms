# 1 Balls

# n = int(input())
# colors = input().split()
# colorHash = dict()
#
# for color in colors:
#     if color not in colorHash:
#         colorHash[color] = 1
#     else:
#         colorHash[color] += 1
#
# maxi = 0
# for color in colorHash:
#     if colorHash[color] > maxi:
#         maxi = colorHash[color]
#
# print(n - maxi)

# 2 Permutation
# u_input = input().split()
# n = int(u_input[0])
# result = 0
#
# expected_numbers = [False for _ in range(n)]
#
# for number in u_input[1:]:
#     if int(number) <= n:
#         expected_numbers[int(number) - 1] = True
#
# for i in range(n):
#     if not expected_numbers[i]:
#         result = i + 1
#         break
#
# print(result)

# 3 Lost card
# u_input = input().split()
# n = int(u_input[0])
# expected_sum = n*(1 + n)/2
#
# for card in u_input[1:]:
#     expected_sum -= int(card)
# print(int(expected_sum))

# 4 Merge Sort
# n = int(input())
# robots = []
# for _ in range(n):
#     robots.append(tuple(map(int, input().split())))
#
#
# def swap_sort(arr, result, left, mid, right, maximum):
#     while left <= mid and right <= maximum:
#         if arr[left][0] <= arr[right][0]:
#             result.append(arr[left])
#             left += 1
#         else:
#             result.append(arr[right])
#             right += 1
#     return left, right
#
#
# def push_leftovers(arr, result, iterator, end):
#     while iterator <= end:
#         result.append(arr[iterator])
#         iterator += 1
#
#
# def commit_changes(arr, result, minimum, maximum):
#     for i in range(minimum, maximum + 1):
#         arr[i] = result[i - minimum]
#
#
# def merge(arr, minimum, mid, maximum):
#     result = []
#     left = minimum
#     right = mid + 1
#
#     left, right = swap_sort(arr, result, left,
#                             mid, right, maximum)
#     push_leftovers(arr, result, left, mid)
#     push_leftovers(arr, result, right, maximum)
#
#     commit_changes(arr, result, minimum, maximum)
#
#
# def merge_sort(arr, left, right):
#     if left >= right:
#         return
#     mid = (left + right) // 2
#
#     merge_sort(arr, left, mid)
#     merge_sort(arr, mid + 1, right)
#     merge(arr, left, mid, right)
#
#
# merge_sort(robots, 0, n - 1)
#
# for robot in robots:
#     print(robot[0], robot[1])

