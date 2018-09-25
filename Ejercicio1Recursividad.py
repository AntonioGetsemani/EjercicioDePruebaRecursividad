author = 'Antonio Getsemani'

def ConvertirNumero(num):
    if num == 0:
        return ""
    else:
        return str(num % 2) + ConvertirNumero(num//2)
print(ConvertirNumero(8))




























