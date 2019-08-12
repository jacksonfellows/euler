with open('../13-Large Sum Input.txt', 'r') as f:
    lines = f.readlines()

ans = 0

for line in lines:
    ans += int(line)

print(str(ans)[:10])
