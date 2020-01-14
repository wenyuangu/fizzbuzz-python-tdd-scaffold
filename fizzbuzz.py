def fizzbuzz(n):
    for i in range(1,n + 1):
        print('fizz'[i % 3 * 4:] + 'buzz'[i % 5 * 4:] or i)
