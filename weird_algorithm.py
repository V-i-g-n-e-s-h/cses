"""
Consider an algorithm that takes as input a positive integer n. 
If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. 
The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
    3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
Your task is to simulate the execution of the algorithm for a given value of n.

Input
The only input line contains an integer n.

Output
Print a line that contains all values of n during the algorithm.

Constraints
1 <= n <= 10^6

Example
Input:
3

Output:
3 10 5 16 8 4 2 1
"""

def logic(num: int) -> list:
    ans = []
    while num != 1:
        ans.append(num)
        num = (num*3)+1 if num&1 else num//2
    ans.append(num)
    return ans


def main() -> None:
    print(" ".join(map(str, logic(num = int(input())))))


if __name__ == "__main__":
    main()