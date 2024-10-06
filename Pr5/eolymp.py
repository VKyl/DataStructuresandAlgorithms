def get_numbers():
    numbers_amount = int(input())
    for _ in range(numbers_amount):
        yield input()


def test_numbers(numbers):
    phone_set = {}
    for number in numbers:
        number_len = len(number)
        for existing in phone_set.keys():
            if number_len >= phone_set[existing] and number.startswith(existing):
                return False

            if number_len < phone_set[existing] and existing.startswith(number):
                return False
        phone_set[number] = len(number)
    return True



tests_amount = int(input())
for _ in range(tests_amount):
    numbers = sorted(get_numbers())
    result = test_numbers(numbers)
    print("YES" if result else "NO")
