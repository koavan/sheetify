import pprint

flag = 0

def sheetify(indict, inlist, row, col, order, index=0):
    global flag
    temp = ''
    if order == len(indict.keys()):
        flag = 1
        return False

    key = list(indict.keys())[order]
    val = indict[key]
    print('{} {} {} {} {}'.format(order,row, col, index, val))

    if type(val) == list:
        print('damn its a list')
        if index == len(val):
            return False
        elif index == 0:
            inlist[row].append(val[index])
        else:
            tlist = []
            for i in range(0,order):
                tlist.append('')
            tlist.append(val[index])
            inlist.append(tlist)

        if not sheetify(indict, inlist, row+1, col, order, index+1):
            # inlist.append([])
            return False
    else:
        inlist[row].append(val)
        temp = sheetify(indict, inlist, row, col+1, order+1)
        if not temp:
            if flag == 1:
                return False
        
        temp2 = sheetify(indict, inlist, row, col+2, order+2)
        if not temp2:
            return False

    return True

mydict = {'Name': 'dayanraj',
 'PubliclyAccessible': 'True',
 'values' : [
     1,
     2,
     3,],
 'profession': 'engineer',
    }

pp = pprint.PrettyPrinter()
result = [[]]
print(len(mydict))
print(sheetify(mydict, result, 0, 0, 0))

pp.pprint(result)