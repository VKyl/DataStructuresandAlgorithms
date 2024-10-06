# 1
#
# n = int(input())
# stage1 = int(input())
# stage2 = int(input())
#
# while stage1 ^ stage2:
#     if stage1 >= stage2:
#         stage1 >>= 1
#     else:
#         stage2 >>= 1
# print(stage1)

# 2
#
# def get_numbers():
#     numbers_amount = int(input())
#     for _ in range(numbers_amount):
#         yield input()
#
#
# def test_numbers(numbers):
#     phone_set = {}
#     for number in numbers:
#         number_len = len(number)
#         for existing in phone_set.keys():
#             if number_len >= phone_set[existing] and number.startswith(existing):
#                 return False
#
#             if number_len < phone_set[existing] and existing.startswith(number):
#                 return False
#         phone_set[number] = len(number)
#     return True
#
#
# tests_amount = int(input())
# for _ in range(tests_amount):
#     numbers = sorted(get_numbers())
#     result = test_numbers(numbers)
#     print("YES" if result else "NO")
