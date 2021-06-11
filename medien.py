import csv
with open('SOCR-HeightWeight.csv')as f:
    reader=csv.reader(f)
    fileData=list(reader)
    
    #to remove the index of given data we are using pop method
    fileData.pop(0)
    print(len(fileData))

    heightData=[]
    for i in range(len(fileData)):
        height=fileData[i][1]
        heightData.append(float(height))

heightData.sort()
n=len(heightData)  
if n % 2 == 0   :
    medien1=float(heightData[n//2]) 
    medien2=float(heightData[n//2-1])
    finalMedien=medien1+medien2
else:
    finalMedien=float(heightData[n//2])
print(finalMedien)
