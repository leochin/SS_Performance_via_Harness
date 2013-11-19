#-------------------------------------------------------------------------------
# Name:        comparison
# Purpose:
#
# Author:      Liang-Huan Chin
#
# Created:     22/08/2013
# Copyright:   (c) Leo Chin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import glob as GLOB
from time import strftime, localtime
import socket as SOCKET
import platform as PF

def readCSV(file):
    """
    this function read the summary.csv and return an key_value table containing tool name, test name list ,execution time, and memory

    Input:
        fileName: csv files under the same directory with this script

    Output:
        key_value: an array containing : tool name, testname, execution time, memory

    Examples
    --------
      >>> fileNmae = "c:/gpqa/summary.csv"
      >>> key_value = [('GeneralG','TEST1', '1.5','300'), ('GeneralG','TEST2', '3.5', '200'), ...]
    """
    test = []
    time = []
    mem = []
    toolList = []
    tool=""
    for line in file:
        if line.find('For') != -1:
            tool = line[4:]
        if line.find('TEST') != -1:
            token = line.split(',')
            if token[1].find('Time') ==-1:
                toolList.append(tool)
                test.append(token[0])
                time.append(token[1])
                mem.append(token[2])
    t_test_t_m = [('{0}'.format(toolList[i]), '{0}'.format(test[i]), '{0}'.format(time[i]), '{0}'.format(mem[i])) for i in xrange(len(test))]
    return t_test_t_m


# create a new csv file named "summary.csv" for the result
compare_file = open('compare'+strftime("%Y-%m-%d", localtime())+'.csv', 'w')
# record time, system name and platform info
compare_file.write("File Generated : "+ strftime("%Y-%m-%d %H:%M:%S", localtime())+"\n")
compare_file.write("System Name : "+ SOCKET.gethostname()+"\n")
compare_file.write("Platform Name : "+ PF.platform()+"\n\n\n")


csvList = GLOB.glob('*.csv')
files = []
for csv in csvList:
    csvPath = csv.replace("\\","/")
    if csvPath.find("summary") != -1:
        files.append(csvPath)

print files

f1 = open(files[0], 'r')
compare_file.write("File 1 is "+files[0]+"\n")
f2 = open(files[1], 'r')
compare_file.write("File 2 is "+files[1]+"\n\n")

table1 = readCSV(f1)
table2 = readCSV(f2)

# write the value into csv file followed the format of Test No. Time, Memory
compare_file.write("Tool Name,TEST No.,Time(s),Difference in Time(s), Ratio (Difference/ Exe time in File2), Mem(mb)\n")

for item2 in table2:
    for item1 in table1:
        # check if it is the same tool and the same test
        if (item1[0] == item2[0]) & (item1[1] == item2[1]):
            diffTime = float(item2[2]) - float(item1[2])
            diffMem = float(item2[3]) - float(item1[3])
            try:
                ratioTime = diffTime / float(item1[2])
            except:
                ratioTime = "NA"

    compare_file.write(item2[0]+","+item2[1]+","+item2[2]+","+str(diffTime)+","+str(ratioTime)+","+str(diffMem)+"\n")

compare_file.close()