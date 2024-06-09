def main():
    for _ in range(int(input())):
        x, y = map(int, input().split()) # 3, 2
        maxx = max(x, y) # 3
        inner_square = (maxx-1)**2 # 2 ** 2 = 4
        if inner_square%2 == 0:
            val = inner_square + y + maxx - x # 4 + 2 + 3 - 3 = 6
        else:
            val = inner_square + maxx - y - x
        print(val)

if __name__ == "__main__":
    main()