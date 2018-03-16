file = open('파일이름.txt', 'w+')
file.write('이글을?')
file.writelines([
    '여러줄을\n',
    '쓸거에요\n',
    '블라블라'
])
file.close()