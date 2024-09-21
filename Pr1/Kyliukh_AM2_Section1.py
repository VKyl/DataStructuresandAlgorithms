# Simple problem #1
# def simple_problem():
#     n = int(input())
#     print(n//10, n % 10)
#
#
# simple_problem()

# Numbers problem #2
# def numbers():
#     n = int(input())
#     counter: int = 0 if n != 0 else 1
#     while n != 0:
#         counter += 1
#         n = n//10
#     print(counter)
#
#
# numbers()

# Gardener #10
# def gardener():
#     n = int(input())
#     k = 0
#     water_amount = 0
#     while water_amount <= 1/2:
#         water_amount += 1/(n-k)
#         k += 1
#     print(n - k + 1)
#
#
# gardener()

# Rabbit-failure #14
# def prime(number):
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
#
# def rabbit_failure():
#     n, ticket_number = map(int, input().split())
#
#     for i in range(1, n):
#         if prime(ticket_number + i):
#             print(i - 1)
#             break
#         if i == n - 1:
#             print(-1)
#
#
# rabbit_failure()
