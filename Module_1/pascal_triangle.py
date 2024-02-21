#fun define

def pascal(n):
    for i in range(n):
        # adjust space
        #print(' ' * (n - i), end='')
        # compute power of 11
        print(' '.join(map(str, str(11 ** i))))

#fun exe
user_input=int(input())
pascal(user_input)


