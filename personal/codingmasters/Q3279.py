# Q3279. IP주소
# IP주소에는 IPv4와 IPv6의 두 가지 체계가 있습니다.

# IPv4는 "A.B.C.D" 형태의 IP를 말하며, A, B, C, D는 0이상 255이하의 정수입니다.

# IPv6은 "A:B:C:D:E:F:G:H" 형태의 IP를 말하며, A, B, C, D, E, F, G, H는 4자리의 16진수 수입니다.

# IP가 주어졌을 때, 해당 IP가 IPv4 형식인지 IPv6 형식인지 출력하세요.

# [입력값 설명]
# IP가 문자열 형태로 제공됩니다.

# [출력값 설명]
# 해당 IP가 IPv4 형식이면 "IPv4"를, IPv6 형식이면 "IPv6"을 출력합니다.
# print("IPv4" if input().find(':') == -1 else "IPv6")
import sys;print("IPv4" if sys.stdin.readline().find(':') == -1 else "IPv6")