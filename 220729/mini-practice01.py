# 미니 실습 01
def max_of(a):
    max = a[0]
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
    return max

def min_of(a):
    min = a[0]
    for i in range(1, len(a)):
        if a[i] < min:
            min = a[i]
    return min

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']


print(f'{max_of(t)}')
print(f'{max_of(s)}')
print(f'{max_of(a)}')

print(f'{min_of(t)}')
print(f'{min_of(s)}')
print(f'{min_of(a)}')