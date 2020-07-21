from util11 import *
from collections import defaultdict
from os import path
import psutil
import time
from config import ICE

""" 
        General basic methods :  connectIDA, saveIDM, disconnectIDA, 
                                showChildrenDict, showChildrenList, showChildrenListValue, 
                                showSingleChild, showChildrenByType
"""



def connectIDA(building_path = ICE.building_path):
    """
    :param: building_path
    :return: building:object
    """
    # Connecting to the IDA ICE API.
    pid = start()
    test = ida_lib.connect_to_ida(b"5945", pid.encode())
    # Open a saved building
    building = call_ida_api_function(ida_lib.openDocument, building_path.encode())
    return building,pid



def connectIDA2(building_path):
    """
    :param: building_path
    :return: building:object
    """
    # Connecting to the IDA ICE API.
    pid = start()
    test = ida_lib.connect_to_ida(b"5945", pid.encode())
    # Open a saved building
    building = call_ida_api_function(ida_lib.openDocument, building_path.encode())
    return building


def openIDM(building_path):
    # Open a saved building only when IDA ICE instance is running.
    building = call_ida_api_function(ida_lib.openDocument, building_path.encode())
    return building



def saveIDM(building, apath='', unpacked = 1):
    """
        Path empty: save;    Path: save as...
        packed:0 (default)   unpaced:1
    """

    res1 = call_ida_api_function(ida_lib.saveDocument, building, apath.encode(), unpacked)            #b"D:\\ide_mine\\changing\\ut1_2.idm"
    if len(apath) > 0:
        count = 0
        while True:
            if path.exists(apath):
                print('Successfully save file :', apath)
                break
            else:
                print('Unable to save the file to', apath)
                if count ==5:
                    break
                count += 1
                print('Attempt to save the file again.', 5-count)
                time.sleep(2)

    return res1

def disconnectIDA(building):
    """
    :param building: object
    :return: end message:
    """
    saveIDM(building)
    end = ida_lib.ida_disconnect()
    return end

def runEnergySimu(building):
    res = call_ida_api_function_j(ida_lib.runSimulation, building, 2)
    print('Simulation begins. ')
    return res

def killprocess(pid):
    time.sleep(2)
    p = psutil.Process(int(pid))
    p.terminate()
    time.sleep(2)


# 应该新建dictionary 把东西列出来，避免重复寻找
def showChildrenDict(parent):
    children = call_ida_api_function(ida_lib.childNodes, parent)
    nameList = defaultdict(int)
    for child in children:
        name = ida_get_name(child['value'])
        nameList[child['value']] = name

    str(nameList)
    return nameList

def showChildrenList(parent):
    children = call_ida_api_function(ida_lib.childNodes, parent)
    nameList = []
    for child in children:
        name = ida_get_name(child['value'])
        nameList.append(name)

    str(nameList)
    return nameList

# Be carefully when using this function since some children may not have values
def showChildrenDictValue(parent):
    children = call_ida_api_function(ida_lib.childNodes, parent)
    print("name:value")
    valueList =dict
    for child in children:
        name = ida_get_name(child['value'])
        value = ida_get_value(child['value'])
        valueList[child['value']]=value
        # valueList[name]=value

    str(valueList)
    return valueList

def showSingleChild(parent, child_name):
    element = ida_get_named_child(parent, child_name)
    element_val = None
    print(element)
    try:
        element_val = ida_get_value(element)
        # print("The current %s value is %s, and the type is %s" % (child_name, tuple(element_val), type(element_val)))
        print(element_val)
    except:
        pass

    return element, element_val

def showChildrenByType(parent, child_type):
    """

    :param parent:
    :param child_type: ZONE, WINDOW, DET-WINDOW, OPENING
    :return: children: list
    """
    print('Known types: ZONE, WINDOW, DET-WINDOW, OPENING')
    children = call_ida_api_function(ida_lib.getChildrenOfType, parent,child_type.encode())
    for i, val in enumerate(children):
        print("Child %s is %s" %(i,val))

    return children

def setAttribute(object, text):
    """

    :param object:
    :param text: follow the json format --  "{\"type\":\"number\",\"value\":" + "{0:.1f}".format(new_dx) + "}"
    :return:
    """
    # text_to_send = "{\"type\":\"number\",\"value\":" + "{0:.1f}".format(new_dx) + "}"
    res = call_ida_api_function(ida_lib.setAttribute, b"VALUE", object, text.encode())
    return res


#Unit test

def main():
    building = connectIDA('D:\\ide_mine\\changing\\ut2_wwr0.1.idm')
    res = saveIDM(building)
    print(res)


if __name__ == "__main__":
    main()
