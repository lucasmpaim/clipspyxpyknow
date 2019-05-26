

def pyread_float(msg):
    try:
        return float(input(msg))
    except ValueError:
        print('Este dado é inválido, por favor, informe um número')
        return pyread_float(msg)

