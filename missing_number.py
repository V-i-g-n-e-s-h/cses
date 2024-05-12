"""
You are given all numbers between 1,2,...,n except one. Your task is to find the missing number.

Input
The first input line contains an integer n.
The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).

Output
Print the missing number.

Constraints
2 <= n <= 2*10^5

Example
Input:
5
2 3 1 5

Output:
4
"""


def logic(total_count: int, numbers: list) -> int:
    sum_of_total_numbers = total_count*(total_count+1)//2
    sum_of_provided_numbers = sum(numbers)
    missing_number = sum_of_total_numbers - sum_of_provided_numbers
    return missing_number


def main() -> None:
    n = int(input())
    nums = list(map(int, input().split()))
    output = logic(total_count = n, numbers = nums)
    print(output)


if __name__ == "__main__":
    main()
