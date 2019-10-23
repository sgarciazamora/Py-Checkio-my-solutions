def checkio(text: str) -> str:
    lower = text.lower()
    repetida = lower[0]
    veces = 0
    for i in lower:
        if i.isalpha():
            if(lower.count(i)> veces):
                veces = lower.count(i)
                repetida=i
            elif lower.count(i)==veces:
                if i < repetida:
                    repetida= i
                    veces = lower.count(i)

    return repetida





if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")