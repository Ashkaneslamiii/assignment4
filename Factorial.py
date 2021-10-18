
adad = int(input("Please Eneter your number: \n"))

i = 2
tmp1_list =[]
tmp2_list =[]
i_list = []
while (True):

    tmp1 = adad / i
    tmp2 = adad % i
    adad = tmp1
    print(tmp2)
    tmp1_list.append(tmp1)
    tmp2_list.append(tmp2)
    i_list.append(i)

    if (tmp1 == 1):
        print("Your Answer is",i,"!")
        exit()

    elif tmp2 == 0:
        i +=1
    else:
        print("This is not a Factorial Number :( \n")
        exit()
    