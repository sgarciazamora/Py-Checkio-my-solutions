def safe_pawns(pawns: set) -> int:
    columna = "xabcdefghx"
    safe = 0
    for peon in pawns:

     primero = columna[columna.find(peon[0])-1] + (str(int(peon[1])-1))
     segundo = columna[columna.find(peon[0]) + 1] + (str(int(peon[1])-1))

     if(pawns.__contains__(primero) or pawns.__contains__(segundo)):
      safe +=1
     print("El peon "+peon+" está a salvo")
    print("Fin de ejecución, a salvo hay: " +str(safe))
    return safe

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")