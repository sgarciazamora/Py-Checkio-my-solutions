def sun_angle(time):
    #replace this for solution
    tiempo =time
    decimales = time[-2]+time[-1]
    decimales = str((100*int(decimales)/60).__round__(2)).replace(".","")
    decimales=decimales[0]+decimales[1]
    hora = time[0]+time[1]+decimales[0]+decimales[1]
    hora=int(hora)
    if(hora<600 or hora>1800):
        return "I don't see the sun!"
    else:
        hora = hora - 600
        return hora * 90/600


    return time

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:45"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")