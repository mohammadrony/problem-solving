def multiplication_series(m, n):
    if m == 0:
        return

    print(f"{m} * {n} = {m*n}")
    multiplication_series(m - 1, n)
    return


print(multiplication_series(10, 5))
