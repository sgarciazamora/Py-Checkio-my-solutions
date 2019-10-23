def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    actual = ""
    veces =1
    mejor =0
    # your code here


    for letra in line:
        if letra=="":
            return 0
        if(letra == actual):
            veces +=1
            if(veces>mejor):
                mejor=veces
        else:
            if (veces > mejor):
                mejor = veces
            actual=letra
            veces = 1


    return mejor

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')