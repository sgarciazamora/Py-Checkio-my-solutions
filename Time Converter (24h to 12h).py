def time_converter(time):
    #replace this for solution
    horas = int(time[0]+time[1])
    minutos = int(time[3]+time[4])
    periodo = " a.m."
    casoam=0
    if(horas == 0 ):
        horas=12
        casoam=1
    if(horas>12 ):
        horas = horas-12
        periodo=" p.m."
    if (horas==12 and minutos>=0and casoam== 0):
        periodo=" p.m."
    print("Valor que va a salir: "+str(horas)+ ":"+time[3:]+periodo)
    return str(horas)+ ":"+time[3:]+periodo

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")