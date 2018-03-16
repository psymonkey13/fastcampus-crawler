file = open('파일이름.txt', 'r')
print('## 파일 한번에 전부 출력하기 ##')
print(file.read())

file.close()

file2 = open('파일이름.txt')
print('## 파일 한줄 한줄 출력하기 ##')
for line in file2.readlines():
    print(line)

file2.close()
