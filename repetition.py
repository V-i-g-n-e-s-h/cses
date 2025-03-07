"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
Your task is to find the longest repetition in the sequence. 
This is a maximum-length substring containing only one type of character.

Input
The only input line contains a string of n characters.

Output
Print one integer: the length of the longest repetition.

Constraints
1 <= n <= 10^6

Example
Input:
ATTCGGGA

Output:
3
"""

def logic(sequence: str) -> int:
    temp_count, max_count = 1, 1
    for idx in range(1, len(sequence)):
        if sequence[idx-1] == sequence[idx]:
            temp_count += 1
            max_count = max(max_count, temp_count)
        else:
            temp_count = 1
    return max_count


def main() -> None:
    n = input()
    output = logic(sequence = n)
    print(output)


if __name__ == "__main__":
    main()