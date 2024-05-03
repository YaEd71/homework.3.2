def print_params(a=1, b='строка', c=True):
    if c is None:
        c = []
        c.append(a)
    print(c)
    print(a, b, c)

print_params()
print_params(2, 'eduard', [12])
print_params(b = 25)
print_params(c= [1,2,3])

values_list = [22, 2.2, 'python']
values_dist = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dist)

values_list_2 = [1.2, 'urban']
print_params(*values_list_2, 42)
