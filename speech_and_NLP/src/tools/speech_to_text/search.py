def search(text, searchText):
    textArray = text.split()
    for i in range(len(textArray)):
        print(str(i) + "番目" + textArray[i])
        textArray[i] = textArray[i].split(',')
        for j in range(len(textArray[i])):
            print(textArray[i][j])
            if textArray[i][j] == searchText:
                print(textArray[i-1][0] + "が、" + textArray[i][j] + "として認識されました。")
        print(str(i) + "番目の添え字は、" + text[i])