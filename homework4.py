# Task 1
try:
    with open('email.txt') as source, open('gmail.txt', 'w') as target:
        for line in source:
            res = line.split()[-1]
            if res.endswith('gmail.com'):
                # target.write(f'{res}\n')
                print(res, file=target)
except Exception as e:
    print(e)