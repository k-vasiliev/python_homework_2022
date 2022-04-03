
#создаем функцию, которая суммирует А и B

def plus(a: str, b: str) -> str:
    rslt = a + b
    return rslt

print(type(plus(5,5))) #возвращает int, хотя задавал стринг