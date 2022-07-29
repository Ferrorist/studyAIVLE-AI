#import copy
# 미니 실습 03
# 보초법 연습. if문을 만날 때마다 count하기.
def linear_search(a, find):
    count = 0
    i = 0
    while True:
        count += 1
        if len(a) == i:
            return (-1, count)
        count += 1
        if a[i] == find:
            return (i, count)
        i += 1

def lsearch_s(a, find): #보초법 사용
#    LIST = copy.deepcopy(a)
    LIST = a.copy()
    LIST.append(find) # index : append하기 전 len(LIST)
    count = 0
    i = 0
    while True:
        count += 1
        if LIST[i] == find:
            return (i, count) # i == append하기 전 len(LIST) 이라면 탐색하려는 원소가 존재하지 않음을 의미.
        i += 1
 
a = [2, 5, 1, 3, 9, 6, 7]
index1, count1 = linear_search(a, 7)
index2, count2 = lsearch_s(a, 7)

if index1 == -1 and index2 == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'선형검색 While 문에서 검색값은 a[{index1}]에 있습니다.')
    print(f'선형검색 보초법에서 검색값은 a[{index2}]에 있습니다.')
    print(f'선형검색 While 문에서 if문은 {count1}만큼 실행되었습니다.')
    print(f'선형검색 보초법에서 if문은 {count2}만큼 실행되었습니다.')