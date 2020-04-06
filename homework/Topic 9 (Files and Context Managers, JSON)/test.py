def open_lockers_counter(n):
    open_count = 0
    for i in range(1, n + 1):
        div_num = 0 # i divisors number
        for j in range(1, i + 1):
            if i % j == 0:
                div_num += 1
        # if divisors number is odd
        if div_num % 2 != 0:
            open_count += 1
    return open_count

print(open_lockers_counter(100))