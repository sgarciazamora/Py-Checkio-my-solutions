VOWELS = "aeiouy"

def translate(phrase):
    traducida=""
    Consonante = 0
    Vocal = 0

    for word in phrase:
     if(word in VOWELS and word !=" " and Consonante==0):
      Vocal +=1

      if (Vocal==3):
          traducida +=word
          Vocal=0
          continue
     elif word != " " :
         if Consonante == 0:
          Consonante +=1
          traducida += word
          continue
         Consonante=0
         continue
     elif word == " ":
         traducida += " "


    return traducida

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
