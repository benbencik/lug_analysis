import numpy as np

dataset = ['1', '2', '3', '4', '5']

for i in range(len(dataset)):
    data = open('L'+dataset[i]).readlines()
    X = []
    Y = []
    for j in range(len(data)):
        data[j] = data[j].strip('\n').split(',')
        X.append(float(data[j][0]))
        Y.append(float(data[j][-1]))
    degree = 4
    polyfit = np.polyfit(X, Y, degree)
    file = open("nL{}".format(dataset[i]), "w") 
    for j in range(len(polyfit)):
        file.write(str(round(polyfit[j], 10)) + '\n') 
    file.close() 
    
    #----------------------------------------------------------------------------
    
    file = open("B{}".format(dataset[i]), "w") 
    file.write(str(round(X[-1], 10)))
    file.close() 
    
    #------------------------------------------------------------------------------

    data = open('P'+dataset[i]).readlines()
    X2 = []
    Y = []
    for j in range(len(data)):
        data[j] = data[j].strip('\n').split(',')
        X2.append(float(data[j][0]))
        Y.append(float(data[j][-1]))
    degree = 6
    polyfit = np.polyfit(X2, Y, degree)
    file = open("nP{}".format(dataset[i]), "w") 
    for j in range(len(polyfit)):
        file.write(str(round(polyfit[j], 10)) + '\n') 
    file.close() 