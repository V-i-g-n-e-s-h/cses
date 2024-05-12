"""
You are given an array of n integers. 
You want to modify the array so that it is increasing, 
i.e., every element is at least as large as the previous element.

On each move, you may increase the value of any element by one. 
What is the minimum number of moves required?

Input
The first input line contains an integer n: the size of the array.
Then, the second line contains n integers 1, 2, ..., n: the contents of the array.

Output
Print the minimum number of moves.

Constraints
1 <= n <= 2*10^5
1 <= i <= 10^9

Example
Input:
5
3 2 5 1 7

Output:
5
"""

def logic(count: int, numbers: list) -> int:
    swaps = 0
    for idx in range(1, count):
        if numbers[idx-1] > numbers[idx]:
            swaps += numbers[idx-1] - numbers[idx]
            numbers[idx] += numbers[idx-1] - numbers[idx]
    return swaps

def main() -> None:
    n = int(input())
    nums = list(map(int, input().split()))
    output = logic(count = n, numbers = nums)
    print(output)


if __name__ == "__main__":
    main()