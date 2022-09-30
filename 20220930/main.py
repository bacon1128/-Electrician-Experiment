if __name__ == "__main__":
    
    # 讀取一個文字檔，並將其內容轉成list資料型態
    f = open("day1.txt", "r")
    data = f.read().splitlines()

    # 將list內的數字轉成int型態
    data_length = len(data)
    for i in range(data_length):
        data[i] = int(data[i])

    # 當後面的數字比前面數字大，則counter++
    counter = 0
    for i in range(data_length-1):
        if(data[i+1]-data[i]) > 0:
            counter += 1

    print(counter)


'''資料型態轉換的方法
    a = "102"
    a = int(a)
    print(type(a))
'''