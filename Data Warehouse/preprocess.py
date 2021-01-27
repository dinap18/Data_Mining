"""
Data Mining Assignment 1
Dina Pinchuck 337593958
Liel Orenstein 209220730

"""
from collections import defaultdict
"""
def convert2arff(num_of_files):
    fout=open("hospital.arff", "w")
    fout.write("@relation patients_temperatures\n")
    fout.write("@attribute ward numeric\n")
    fout.write("@attribute patients_ID numeric\n")
    fout.write("@attribute time numeric\n")
    fout.write("@attribute temperatue numeric\n\n")
    fout.write("@data\n")
    for ward in range(1, num_of_files+1):
        fin=open(str(ward)+".txt", "r")
        for time in range(60*24):
            s=fin.readline().split()
            for patient in range(len(s)):
                fout.write(str(ward)+","+str(patient+1)+",")
                fout.write(str(time)+","+s[patient]+"\n")
        fin.close()
    fout.close()

convert2arff(3)
"""
def convert2arff(wardNumber):
    fout=open("ward.arff", "w")
    fout.write("@relation patients_temperatures\n")
    fout.write("@attribute patients_ID numeric\n")
    fout.write("@attribute time numeric\n")
    fout.write("@attribute average_temperature numeric\n\n")
    fout.write("@data\n")
    timeDict=defaultdict(list)
    fin=open(str(wardNumber)+".txt", "r")
    for time in range(60*24):
        s=fin.readline().split()
        for patient in range(len(s)):
            temp=float(s[patient])
            if temp>=36:
                if temp>43:
                    temp = (temp - 32) * 5/9 
                if temp>=36 and temp<=43:
                    timeDict[patient+1,time//60].append(temp)
    fin.close()
    for patient,time in timeDict:
        lst=timeDict[patient,time]
        avg=round(sum(lst)/len(lst),1)
        fout.write(str(patient)+","+ str(time) +","+ str(avg) + "\n")
    fout.close()   
    
convert2arff(1)   

def variance(ward):
    fin=open(ward,"r")
    lines=fin.readline()
    while lines!='@data\n':
        lines=fin.readline() 
    temp=[]
    lines=fin.readline().split(',')
    while lines !=['']:
        temp.append(float(lines[2]))
        lines=fin.readline().split(',')
    fin.close()
    avg=sum(temp)/len(temp)
    squared=[i**2 for i in temp]
    result=(1/len(temp))*sum(squared)-avg**2
    return result
    
    
print(variance("ward.arff"))