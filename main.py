if __name__ == '__main__':
    with open('happy.txt', mode='a') as my_file:
        text = my_file.write(':)')
        print(text)


    '''
    test_file = open('test.txt')

    print(test_file)#<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>
    print(test_file.read())#Hello I am the 'test' txt.              4: How are you doing?
    test_file.seek(0)
    print(test_file.read())#Hello I am the 'test' txt.              4: How are you doing?

    print(test_file.readline())#Hello I am the 'test' txt.
    print(test_file.readline())
    print(test_file.readline())# :)

    print(test_file.readlines()) #["Hello I am the 'test' txt.\n", '\n', ':)\n', 'how are you doing?']

    test_file.close()
    '''
