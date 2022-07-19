word =input("영단어를 입력해주세요: ")
word = list(word) 

dl = input("삭제할 단어를 입력해주세요: ")
for i in word:
    if i == dl:
        word.remove(dl)
st = "".join(word)
print(st)
    


