N = list(map(int, input().split()))
asc_check = sorted(N)
if N == asc_check:
    print("ascending")
elif N == list(reversed(asc_check)):
    print("descending")
else:
    print("mixed")