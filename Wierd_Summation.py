n = int(input())
numbers = list(map(int,input().split()))

def left_limit(numbers):
    stack = []
    left_subarr = []
    n = len(numbers)
    index = len(stack) - 1
    for i in range(n) :

        while (len(stack) != 0 and numbers[i] >= numbers[stack[index]]) :
            stack.pop()

        if (len(stack) != 0) :
            left_subarr.append(stack[index])
        else :
            left_subarr.append(-1)

        stack.append(i)
    return left_subarr

def right_limit(numbers): 
    stack = []
    right_subarr = []
    index = len(stack) - 1 
    n = len(numbers)
    for i in range (n-1,-1,-1) :

        while (len(stack) != 0 and numbers[i] > numbers[stack[index]]) :
            stack.pop()

        if (len(stack) != 0) :
            right_subarr.append(stack[index])
        else :
            right_subarr.append(n)

        stack.append(i)

    right_subarr = right_subarr[::-1]
    return right_subarr

def length(left_subarr, right_subarr, numbers):
    mod = 10 ** 9 + 7
    n = len(numbers)
    Length = [None]*n
    answer = [None]*n

    for k in range (n) :
        r = right_subarr[k] - 1
        l = left_subarr[k] + 1
        x = r - k + 1
        y = k-l

        Sum = (((x)*(x+1))//2)

        Length[k] = (((y)*(y+1))//2) * x
        Length[k] += ((y+1)*Sum)

        answer[k] = (numbers[k]*Length[k])

    return answer

left_subarr = left_limit(numbers)
right_subarr = right_limit(numbers)
answer = length(left_subarr, right_subarr, numbers)

summation = 0
for k in range (n) :
    summation += answer[k]

print(summation % (10**9 + 7))