def countWords():
    filename= input("Enter the file name: ")
    noofwords=0
    file= open(filename,'r')
    for line in file:
        words= line.split()
        noofwords= noofwords+len(words)
        print(words)
    print('The number of words used are',+noofwords) 
    

countWords()      