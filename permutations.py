from typing import Generator, List
# from utilities.decors import time_memory_cpu_complexity_decorator


# @time_memory_cpu_complexity_decorator
def answer(n: int) -> Generator[str, None, None]:
    for i in range(2, n + 1, 2):
        yield str(i)
    for i in range(1, n + 1, 2):
        yield str(i)

def main() -> None:
    n = int(input())
    # n = 10000
    if 1 < n < 4:
        print("NO SOLUTION")
    else:
        print(" ".join(answer(n=n)))


if __name__ == "__main__":
    main()

"""
Optimized Code:

from itertools import chain


def main():
    n = int(input())
    if n == 1:
        print(1)
    elif n < 4:
        print("NO SOLUTION")
    else:
        print(" ".join(map(str, chain(range(2, n + 1, 2), range(1, n + 1, 2)))))


if __name__ == '__main__':
    main()

"""

