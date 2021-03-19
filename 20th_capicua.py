a = 100
b = 1000
c = 0

for i in range(a, b + 1):
    num_s = str(i)
    num_list = list(num_s)
    if num_list == num_list[::-1]:
        cap = "".join(num_list)
        c += 1
        if c == 20:
            print(cap)
            break
