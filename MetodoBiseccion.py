
def biseccion(polinomio, segmento, error=0.3):
    a, b = segmento['a'], segmento['b']
    Fa, Fb = calcularX(polinomio,a), calcularX(polinomio,b)
    if Fa * Fb > 0:
        return None
    while (b - a > error):
        x = (a + b) / 2.0
        f = calcularX(polinomio,x)
        if f * Fa > 0:
            a = x
        else:
            b = x
    return x




def main():
    print("════════════════════════════════════════════════════════════════════════════════")
    print(">> Bienvenido al programa para calcular el metodo de biseccion <<")
    print("════════════════════════════════════════════════════════════════════════════════")
    gradoMaximo = int(input("<< Ingrese el grado maximo de tu polinomio: "))
    polinomio = []
    imprimirPolinomio(polinomio)
    print("════════════════════════════════════════════════════════════════════════════════")
    i = gradoMaximo;
    while (i >= 0 ):
        polinomio.append(float(input(f"<< Ingrese el coeficiente de la X de grado {i}: ")))
        i-= 1
    print("════════════════════════════════════════════════════════════════════════════════")
    a = float(input("<< Ingrese el valor inicial del intervalo: "))
    b = float(input("<<  Ingrese el valor final del intervalo:  "))
    print("════════════════════════════════════════════════════════════════════════════════")

    valorBiseccion = biseccion(polinomio, {"a":a,"b":b}, 0.00003)
    if valorBiseccion!=None:
        print(f">> El resultado de la Biseccion es: {valorBiseccion}")
    else:
        print('>> No hay cambio de signo, no se puede utilizar el metodo de biseccion')
    print("════════════════════════════════════════════════════════════════════════════════")

    print(">> Desarrolladores: Guido Scarpati Soto  y Matias Picon <<")
    print("════════════════════════════════════════════════════════════════════════════════")


def calcularX(polinomio, x):
    resultado = 0;
    for i in range(len(polinomio)):
        resultado += polinomio[i] * x ** i

    return resultado

def imprimirPolinomio(polinomio):
    for i in range(len(polinomio)):
        if polinomio[i]!=0:
            print(end=f"{polinomio[i]}X^{i} ")




if __name__ == '__main__':
    main()
    input()
