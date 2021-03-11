cpdef void main(int n):
    cdef int k = 0
    cdef int i = 2
    cdef int number

    for number in range(i, n):
        if is_prime(number):
            k = k + 1



# Python program to check if
# given number is prime or not

# If given number is greater than 1
cpdef bint is_prime(int n):

    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    cdef int i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True