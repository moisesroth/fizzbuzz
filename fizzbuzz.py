def fizzbuzz(n=15):
    for i in range(1, n+1):
        output = ''
        if i % 3 == 0: output += 'Fizz'
        if i % 5 == 0: output += 'Buzz'
        print output or i

