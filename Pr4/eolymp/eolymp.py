def check_if_exist(k, desired_dist, stalls, stalls_len):
    good_stalls = 1
    dist = 0
    for i in range(1, stalls_len):
        dist += stalls[i] - stalls[i-1]
        if dist >= desired_dist:
            dist = 0
            good_stalls += 1
    return good_stalls >= k

n, k = map(int, input().split())
stalls = list(map(int, input().split()))


left, right = 0, stalls[-1] - stalls[0]
while left < right:
    mid = left + right // 2
    if(check_if_exist(k, mid, stalls, n)):
        left = mid + 1
    else:
        right = mid

print(left)
