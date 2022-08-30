import sys;
S = sys.stdin.readline()
dict = {"'":"\'", '"':'\"', '\\':'\\\\'}

for key in dict:
    S = S.replace(key, dict[key])
print(S)