
rows = int(input('rows no.of'))
for i in range(rows+1):
    for j in range(i):
        print(j+1,end='')
    print("\r")
