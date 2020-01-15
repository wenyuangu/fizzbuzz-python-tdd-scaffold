# @File  : fizzbuzz.py
# @Author: Wenyuan Gu
# @Date  : 2020/1/15


def fizzbuzz(n):
    return 'Fizz'[n % 3 * 4:] + 'Buzz'[n % 5 * 4:] or n


def main():
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == '__main__':
    main()