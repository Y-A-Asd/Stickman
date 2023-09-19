import collections
number = int(input("Your number: "))

def encr(number:int)->int:
    list_of_digits = [int(i) for i in str(number)]
    count = {}
    for i in list_of_digits:
        if i not in count:
            count.update({i:1})
        else:
            count.update({i:count[i]+1})
    # t = sorted([str(key) + str(value) for key, value in count.items()])
    output = "".join(sorted(''.join(sorted([str(key) + str(value).replace("1","") for key, value in count.items()]))))
    # output = output.replace("1","")
    # print(output)
    if int(output) == number:
        print(output)
        exit()
    else:
        return encr(int(output))


encr(number)
