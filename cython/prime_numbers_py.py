def main(n):
    k = 0
    i = 2

    for number in range(i, n):
        if is_prime(number):
            k = k + 1


# Python program to check if
# given number is prime or not

# If given number is greater than 1
def is_prime(n):

    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True