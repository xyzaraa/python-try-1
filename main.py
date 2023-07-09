''' this is a dummy project
from a beginner-programmer in python
just trying
hehe
'''


global x
x = list_gue = ['deara', 'bibi', 'gerry', 'xyzara', 'oggy']
def dashboard():
    print('Hello Guest, what do you want to do?')
    print('1.Check Data\n2.List\n3.Count Data\n4.Type')
    choose=input('Your Choice: ')
    if choose=='1':
        check_data()
    elif choose=='2':
        show()
    elif choose=='3':
        countdata()
    elif choose=='4':
        tipe()
def check_data():
    check=input('Input Name : ')
    if check in list_gue:
        print('Yes, its included')
    else:
        print('Data not found')

def show():
    print(list_gue)
    choose=input('do you want to delete one of the data? (y/n)')
    if choose=='y':
        change=input('which index you want to delete?: ')
        if change.isdigit():
            index=int(change)
            if index >= 0 and index < len(list_gue):
             deleted_data = list_gue.pop(index)
             print('Updated: ',list_gue)
            else:
                print('invalid index')
    elif choose=='n':
        print('yaudah')
    else:
        print('Invalid Choice')

def countdata():
    x = len(list_gue)
    print('Total Data: ',x)

def tipe():
    x = type(list_gue)
    print('Type of Data: ',x)

dashboard()


