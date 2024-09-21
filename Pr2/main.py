# def bunny():
#     month_amount = int(input())
#     BUNNY_EATEN = int(input())
#     bunny_amount = 1
#
#     for _ in range(month_amount):
#         if bunny_amount == 0:
#             break
#         if bunny_amount > BUNNY_EATEN:
#             bunny_amount = max(bunny_amount - BUNNY_EATEN, 0)
#         bunny_amount *= 2
#     print(bunny_amount)
#
# def young_gardener():
#   leaf_levels_amount = int(input())
#   water_amount = leaf_levels_amount * (leaf_levels_amount + 1) + 1
#
#   print(water_amount)
#
# def height():
#     def range_len(data, range_start, range_end):
#         counter = 0
#         for item in data:
#             if range_start <= item <= range_end:
#                 counter += 1
#         print(counter)
#
#
#     while True:
#         try:
#             n = int(input())
#             heights_data = list(map(int, input().split()))
#             range_start, range_end = map(int, input().split())
#             range_len(heights_data, range_start, range_end)
#         except EOFError:
#             break
#
#     main()
#
# def stack():
#     try:
#         n, a, b, c, x = map(int, input().split())
#     except EOFError:
#         return
#
#     stack: list = []
#     suma = 0
#
#     for i in range(n):
#         x = ((a * (x ** 2) + x * b + c) // 100) % 10 ** 6
#
#         if x % 5 < 2:
#             if stack:
#                 stack.pop()
#         elif not stack:
#             stack.append(x)
#         else:
#             stack.append(min(x, stack[-1]))
#
#         if stack:
#             suma += stack[-1]
#
#     print(suma)
#
# stack()

