#1
# class Queue:
#     def __init__(self, items, k):
#         self._queue = sorted([*items])
#         self._size = k
#
#     @property
#     def max(self):
#         return self._queue[-1]
#
#     def push(self, item):
#         smallest = self._queue.pop(0) + item
#         self._insert(smallest)
#
#     def _insert(self, item):
#         low, high = 0, self._size - 2
#         while low <= high:
#             mid = (low + high) // 2
#             if self._queue[mid] < item:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#
#         if low >= self._size:
#             self._queue.append(item)
#         else:
#             self._queue.insert(low, item)
#
#     def __str__(self):
#         return str(self._queue)
#
#
# n, k = map(int, input().split())
# clients = list(map(int, input().split()))
# q = Queue(clients[:k], k)
#
# for client in clients[k:]:
#     q.push(client)
#
# print(q.max)

#2
# try:
#     while True:
#         numbers = sorted(list(map(int, input().split())), reverse=True)
#         result = "ok\n\n"
#         size = len(numbers)
#
#         while numbers:
#             n = numbers.pop(0)
#             size -= 1
#
#             if n > size:
#                 result = "fail\n\n"
#                 break
#
#             for i in range(n):
#                 numbers[i] -= 1
#                 if numbers[i] < 0:
#                     result = "fail\n\n"
#                     break
#
#             numbers.sort(reverse=True)
#         print(result)
#
# except EOFError:
#     pass

#3
# n, k = map(int, input().split())
# levels = []
# time_sum = 0
# points_sum = 0
#
# for i in range(n):
#     points, time = map(int, input().split())
#     time_sum += time
#     points_sum += points
#     levels.append((points, time))
#
# if points_sum >= k:
#     levels_table = [time_sum] * (k + 1)
#     levels_table[0] = 0
#
#     for points, time in levels:
#         for point in range(k, -1, -1):
#             if point + points >= k:
#                 levels_table[k] = min(levels_table[k], levels_table[point] + time)
#             else:
#                 levels_table[point + points] = min(levels_table[point + points], levels_table[point] + time)
#
#     print(levels_table[k])
# else:
#     print(-1)

#4
# def check_if_exist(k, desired_dist, stalls, stalls_len):
#     good_stalls = 1
#     dist = 0
#     for i in range(1, stalls_len):
#         dist += stalls[i] - stalls[i-1]
#         if dist >= desired_dist:
#             dist = 0
#             good_stalls += 1
#     return good_stalls >= k
#
# n, k = map(int, input().split())
# stalls = list(map(int, input().split()))
#
#
# left, right = 0, stalls[-1] - stalls[0]
# while left <= right:
#     mid = (left + right) // 2
#     if(check_if_exist(k, mid, stalls, n)):
#         left = mid + 1
#     else:
#         right = mid - 1
#
# print(left - 1)
