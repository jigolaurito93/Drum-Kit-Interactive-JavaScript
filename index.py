def fibonacci(n):
    output = []
    if n == 1:
            output = [0]
    elif n == 2:
            output = [0,1]
    else:
          output = [0,1]
          x = 2
          for i in range(n):
            while x < n:
                 output.append(output[-1] + output[-2])
                 x +=1
        
    print(output)

fibonacci(16)
        
