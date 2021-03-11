import timeit

cy = timeit.timeit(
    "prime_numbers_cy.main(100000)", setup="import prime_numbers_cy", number=100
)
py = timeit.timeit(
    "prime_numbers_py.main(100000)", setup="import prime_numbers_py", number=100
)

print(cy, py)
print("Cython is {}x fast".format(py / cy))
