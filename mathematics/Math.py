class Math:
    def __init__(this, numbers):
        this.numbers = this.strToNumber(numbers)


    def strToNumber(this, numbersStr):
        numbers = []
        for s in numbersStr:
            #Verifica se existe um . no número
            if '.' in s:
                numbers.append(this.strToFloat(s))
            else:
                numbers.append(this.strToInt(s))
        return numbers

    #Converte a String para INT
    def strToInt(this, nStr):
        return int(nStr)

    # Converte a String para FLOAT
    def strToFloat(this, nStr):
        return float(nStr)

    #Faz as operações de SOMA
    def addition(this):
        result = 0
        for n in this.numbers:
            result += n
        return result

    # Faz as operações de MULTIPLICAÇÃO
    def multiplication(this):
        result = 0
        for n in this.numbers:
            #Na primeira vez só atribui o valor a variável result, caso contratrio sempre vai multiplicar por ZERO
            if result == 0:
                result = n
            else:
                result *= n
        return result

    # Faz as operações de DIVISÃO
    def division(this):
        result = 0
        for n in this.numbers:
            # Na primeira vez só atribui o valor a variável result, caso contratrio sempre vai multiplicar por ZERO
            if result == 0:
                result = n
            else:
                result /= n
        return result

    # Faz as operações de SUBTRAÇÃO
    def subtraction(this):
        result = 0
        for n in this.numbers:
            # Na primeira vez só atribui o valor a variável result, caso contratrio sempre vai multiplicar por ZERO
            if result == 0:
                result = n
            else:
                result -= n
        return result
