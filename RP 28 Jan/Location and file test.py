from orbit import ISS


for i in range (100):
    file = (open('test of file2022.txt', 'a'))
    location = ISS.coordinates()
    file.writelines(f'{location} {i:03d}')
    file.writelines('\n')
    file.close()
