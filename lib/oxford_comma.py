def oxford_comma(items):
    x = []
    if len(items) == 1:
        x = items[0]
    elif len(items) == 2:
        x = ' and '.join(items)
    else:
        x = ', '.join(items[:-1]) + ', and ' + items[-1]
    return x

result = oxford_comma(["Boniface"])
print(result)
