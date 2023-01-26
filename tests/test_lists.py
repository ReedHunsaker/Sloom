import functools
from sloom.Core.List import *

def test_type_append():
    intList = List(int)
    intList.append(2)
    try:
        intList.append("3")
    except TypeError:
        assert True
    if intList.count == 1: assert False

def test_extend():
    tempList = ["a", "b", "c"]
    strList = List(str)
    strList.append("d")
    tempExtendedList = strList.contents + tempList
    strList.extend(tempList)
    assert strList.contents == tempExtendedList

def test_filter():
    intList = List(int)
    intList.append(1)
    intList.append(49)
    intList.append(3)
    intList.append(9)
    count = intList.count
    intList.filter(lambda x: x<10)
    assert intList.count == count

def test_map():
    fn = lambda x: 2 * x
    test_list = [2,4,6]
    intList = List(int)
    intList.extend(test_list)
    intList.map(fn)
    assert intList.contents == list(map(fn, test_list))

def test_reduce():
    fn = lambda acc, i: acc + i
    test_list = [4,5,6,7,8]
    intList = List(int)
    intList.extend(test_list)
    intList_reduced = intList.reduce(fn)
    testList_reduced = functools.reduce(fn, test_list)
    assert intList_reduced == testList_reduced

def test_count():
    intList = List(int)
    intList.append(1)
    assert intList.count() == 1

