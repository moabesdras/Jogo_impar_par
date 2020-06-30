def calcula_par_impar(num1, num2):
    num1 = num1
    num2 = num2
    resul = (num1 + num2) % 2
    par_impar = ""
    if resul == 0:
        par_impar = "par"
    elif resul == 1:
        par_impar = "impar"

    return par_impar