from typing import Counter






def count_sent():
    sent = input("Enter your Sentence, Please:\n")
    sent_list = list(sent)
    count = 0
    for i in range (len(sent_list)):
        if sent[i] == " ":
            count +=1
    if sent[i] != " ":        
        count +=1
        print("You inserted ",count,"Vocabulary")
    else:
        print("You inserted ",count,"Vocabulary")

    ans = input("Do you want to continue? y or n? \n")
    if ans == "y":
        count_sent()
    else:
        print("Bye Bye, See you soon, We are waiting here for you :)")
        exit()

count_sent()