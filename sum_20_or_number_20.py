def make_twenty(a,b):
    if a==20 or b==20:
        return True
    elif int(a) + int(b) ==20:
        return True
    else:
        return False
    
result = make_twenty(input("first_number ? "), input("second_number ? "))
print(result)
        