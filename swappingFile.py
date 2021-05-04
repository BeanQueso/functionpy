def swappingFileData():
    file1DataPath = input("Enter the file path of the data that needs to be copied: ")
    file2DataPath = input("Enter the file path of the place the data needs to go to: ")

    with open(file1DataPath, 'r') as data_a:
        d_data_a = data_a.read()
    with open(file2DataPath, 'r') as data_b:
        d_data_b = data_b.read()
    with open(file1DataPath, 'w') as data_a:
        d_data_a.write(data_b)
    with open(file2DataPath, 'w') as data_b:
        d_data_b.write(data_a)

swappingFileData()