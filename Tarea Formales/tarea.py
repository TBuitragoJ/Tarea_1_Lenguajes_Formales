def compute_failure(b):
    n = len(b)
    f = [0] * (n + 1)
    t = 0

    for s in range(1, n):
        while t > 0 and b[s] != b[t]:
            t = f[t]
        if b[s] == b[t]:
            t += 1
            f[s + 1] = t
        else:
            f[s + 1] = 0

    return f


print(compute_failure("ababc"))