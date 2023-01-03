input = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alphabet:
    input = input.replace(i, '*')

print(len(input))