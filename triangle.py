x = open("triangle.txt", "r")

def triangle(input):
    sum = 0     # final sum to be printed at end of function
    for line in input:  # obtain each line for parsing
        x = line.split(' ')     # split numbers by spaces
        for num in range(len(x)):
            if x[num] == '\n':      # get rid of endline chars
                x.remove(x[num])
                continue
            x[num] = int(x[num]) # int cast all strings, get rid of endline
        print(max(x))              # maximum of each line to be added to sum
        sum += max(x)
    print("Final sum is: ", sum)

y = triangle(x)