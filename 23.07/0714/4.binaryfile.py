data = []
with open('./test.bin', 'wb') as file :
    file.write("안녕하세요.".encode())
with open('./test.bin', 'rb') as file :
    content = file.read()
    print(content.decode())
