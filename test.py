inputID = 'asdfsd+f'
validID = 0
for i in inputID:
    print(i)
    print(type(i))
    validID = i.isalpha() or i.isdigit()
    if not validID == True:
        break
    else:
        continue


print(validID)
print(type(validID))