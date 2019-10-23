from typing import List

def checkio(game_result: List[str]) -> str:
  for i in range(3):
     if game_result[i][0] ==  game_result[i][1] == game_result[i][2]:
         print("Mi fila es: "+game_result[i][0]+game_result[i][1]+game_result[i][2])
         print("Se ha cumplido la fila igual, y su valor : "+ game_result[i][0])
         if game_result[i][0] != ".":
             return game_result[i][0]
             break
         continue

     if game_result[0][i] == game_result[1][i] == game_result[2][i] :
         print("Mi columna es: "+game_result[0][i]+game_result[1][i]+game_result[2][i])
         print("Se ha cumplido la columna igual, y el valor es : "+game_result[0][i])
         if game_result[0][i]!=".":
          return  game_result[0][i]
          break
         continue
     if game_result[0][0] == game_result[1][1] == game_result[2][2]:
         if game_result[0][0] != ".":
             return game_result[0][0]
             break
         continue
     if game_result[0][2] == game_result[1][1] == game_result[2][0]:
         if game_result[0][i] != ".":
             return game_result[0][2]
             break
         continue

  print("Se devuelve D ya que no se han cumplido las condiciones")
  print("Mi matriz es : ")
  print(game_result[0][0] + game_result[0][1] + game_result[0][2])
  print(game_result[1][0] + game_result[1][1] + game_result[1][2])
  print(game_result[2][0] + game_result[2][1] + game_result[2][2])
  return "D"





if __name__ == '__main__':
    print("Example:")

    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")