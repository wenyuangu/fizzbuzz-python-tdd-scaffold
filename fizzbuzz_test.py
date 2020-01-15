# @File  : fizzbuzz_test.py
# @Author: Wenyuan Gu
# @Date  : 2020/1/15


import pytest
from fizzbuzz import fizzbuzz

class Test_fizzbuzz():
    def test2(self):
        assert fizzbuzz(2) == 2
    def test3(self):
        assert fizzbuzz(3) == 'Fizz'
    def test5(self):
        assert fizzbuzz(5) == 'Buzz'
    def test15(self):
        assert fizzbuzz(15) == 'FizzBuzz'

if __name__ == "__main__":
    pytest.main()
