def checkPalindrome(candidate: int) -> bool:
    cand = list(str(candidate))
    reversed = cand[::-1]

    return cand == reversed


pals = []

for x in range(999, 0, -1):
    for y in range(999, 0, -1):
        # print(f'{x} x {y}')
        if (checkPalindrome(x * y)):
            pals.append((x * y, x, y))


pals.sort(key=lambda x: x[0])
print(pals)

print(f'the number is: {pals[-1]}')
