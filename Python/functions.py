def getName(name):
    print('Name is:',name)
    
getName('Harry')
getName('Sejal')

def getInfo(firstName, lastName = 'Ab', major = 'Computer Science'):
    print(firstName, lastName, 'majors in', major)
    
getInfo('Abc')
getInfo('Tony', 'Stark', 'CS')
getInfo('Tony', major='CS', lastName='Stark')