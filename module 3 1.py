calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(a):
    count_calls()
    string = (len(a), a.upper(), a.lower())
    return string


def is_contains(b, c):
    count_calls()
    a = []
    d = False
    for i in c:
        a.append(i.lower())
    list_to_search = a
    string = b.lower()
    if string in list_to_search:
        d = True
    return d


print(string_info('Carbon'))
print(string_info('Armageddon'))
print(string_info('BroadWay'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('GreeN', ['grEEnPiece', 'RocK', 'BeAr']))
print(is_contains('sYsTem', ['Main', 'SYSTEm', 'Ball']))
print(calls)
