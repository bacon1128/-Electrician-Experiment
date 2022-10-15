import random
#使用者輸入（Commit）
if __name__ == "__main__":
    user_input = input("Type a word:")
    print("Your input is", user_input)

    #指定一個正確答案（Commit）(簡易)
    f = open("C:\\Users\\Administrator\\Documents\\GitHub\\Electrician-Experiment\\20221014\\words.txt", "r")
    dictionary = f.read().splitlines()
    f.close()

    answer = random.sample(dictionary, 1)[0]
    print(answer)

    #check valid
    if not user_input in dictionary:
        print("Please input an valid word")
        exit()

    #判斷使用者輸入與解答（Commit）
    for i in range(5):
        if user_input[i] == answer[i]:
            print("🟩", end='')
        elif user_input[i] in answer:
            print("🟨", end='')
        else:
            print("⬛", end='')