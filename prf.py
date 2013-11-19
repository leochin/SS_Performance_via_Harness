#-------------------------------------------------------------------------------
# Name:        Performance Test
# Purpose:
#
# Author:      Liang-Huan chin
#
# Created:     19/08/2013
# Copyright:   (c) Leo Chin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from time import gmtime, strftime
import socket as SOCKET
import platform as PF

def readFile(fileName):
    """
    this function read the _prf.txt and return an key_value table containing test name list and execution time

    Input:
        fileName: _prf.txt includes full path

    Output:
        key_value: an array containing key: testname, and value: execution time

    Examples
    --------
      >>> fileNmae = "c:/gpqa/test_prf.txt"
      >>> key_value = [('TEST1', '1.5'), ('TEST2', '3.5'), ...]
    """
    f = open(fileName, 'r')
    testName = []
    time = []
    for line in f:
        if line.find('TEST') > 0:
            token = line.split(' ')
            token2 = token[1].split('	')
            testName.append(token2[0])
            token3 = token2[1].split('	')
            time.append(token3[0])
    key_value = [('{0}'.format(testName[i]), '{0}'.format(time[i])) for i in xrange(len(testName))]
    return key_value

def writeResult(newName, oldName):
    """
    this function compare two _prf.txt file and calculate the differences in execution time and the ratio (difference divided by old execution time)
    Then write the result to a new txt file (named report_file)

    Input:
        newName: _prf.txt includes full path
        oldName: _prf.txt includes full path

    Output:
        Using report_file.write() to write the result directly to txt file
        Following the format of "Test_No. Old_Exe_Time New_Exe_time Diff Ratio"

    Examples
    --------
      >>> writeResult("new_prf.txt", "old_prf.txt")
      >>>
    """
    newF = readFile(newName)
    oldF = readFile(oldName)
    for newItem in newF:
        for oldItem in oldF:
            if newItem[0] == oldItem[0]:
                diff = float(newItem[1]) - float(oldItem[1])
                try:
                    ratio = diff / float(oldItem[1])
                except:
                    ratio = "NA"
                report_file.write(newItem[0]+","+oldItem[1]+","+newItem[1]+","+str(diff)+","+str(ratio)+"\n")


# specify the main path for new and old _prf.txt file and the sub path
mainPath = 'C:/gpqa/pytest/core/stat'
oldPath = 'C:/gpqa/pytest/core/stat'
subPath = ['analyzing_patterns',
           'mapping_clusters',
           'measuring_geographic_distributions',
           'model',
           'modeling_spatial_relationships',
           'rendering',
           'utilities']

# 7 tools
ap = ['generalg', 'globalmorani', 'incrementalsa', 'kfunction', 'nearestneighbor']
mc = ['cluster', 'gi', 'optimizedgi', 'partitional']
mgd = ['centralfeature', 'linear', 'meancenter', 'mediancenter', 'standarddistance', 'standardellipse']
model = ['statModelsTest1', 'statModelsTest2', 'statModelsTest3', 'statModelsTest4', 'statModelsTest5', 'statModelsTest6']
msr = ['exploratoryregression', 'explorecorrelations', 'generateswm', 'geographicallyweightedregression', 'networkswm', 'ols']
render = ['clusterrendered', 'collecteventsrendered', 'countrenderer', 'girendered', 'zrenderer']
util = ['calculatearea', 'calculatedistanceband', 'collectevents', 'exportxyv', 'swm2table']

# create a new text file named "diff.txt" for the result
report_file = open('diff.csv', 'w')
# record time, system name and platform info
report_file.write("File Generated : "+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+"\n")
report_file.write("System Name : "+ SOCKET.gethostname()+"\n")
report_file.write("Platform Name : "+ PF.platform()+"\n\n\n")
report_file.write("TEST No.,Old Exe Time,New Exe Time,Diff,Ratio(Diff/Old Exe Time) \n")

# compare new and old _prf.txt files by the order of tool name (skip model and rendering)
for i in xrange(7):
    if i == 0:
        for tool in ap:
            report_file.write("\n")
            report_file.write("For "+tool+" : \n")
            newName = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            oldName = oldPath + '/'+subPath[i] + '/' + tool + '/' + tool + '_prf.txt'
            writeResult(newName, oldName)
    elif i == 1:
        for tool in mc:
            report_file.write("\n")
            report_file.write("For "+tool+" : \n")
            newName = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            oldName = oldPath + '/'+subPath[i] + '/' + tool + '/' + tool + '_prf.txt'
            writeResult(newName, oldName)
    elif i == 2:
        for tool in mgd:
            report_file.write("\n")
            report_file.write("For "+tool+" : \n")
            newName = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            oldName = oldPath + '/'+subPath[i] + '/' + tool + '/' + tool + '_prf.txt'
            writeResult(newName, oldName)
    elif i == 4:
        for tool in msr:
            report_file.write("\n")
            report_file.write("For "+tool+" : \n")
            newName = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            oldName = oldPath + '/'+subPath[i] + '/' + tool + '/' + tool + '_prf.txt'
            writeResult(newName, oldName)
    elif i == 6:
        for tool in util:
            report_file.write("\n")
            report_file.write("For "+tool+" : \n")
            newName = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            oldName = oldPath + '/'+subPath[i] + '/' + tool + '/' + tool + '_prf.txt'
            writeResult(newName, oldName)
    else:
        msg = "skip model and rendering"

# close the result txt file
report_file.close()

