def checkio(data: str) -> bool:
 if(len(data)<10): return False
 mayus = 0
 low = 0
 num = 0
 for i in data:
     if(i.isupper()): mayus += 1
     if(i.isdigit()): num += 1
     if(i.islower()): low +=1

 if (mayus ==0 or num == 0 or low ==0): return False
 else: return True
    #replace this for solution


#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
