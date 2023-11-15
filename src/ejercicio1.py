"""
Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que contenga cada domicilio una sola vez. 
"""

def obtener_domicilios_facturas(facturas):
    domicilios = {}

    for cliente, _, _, domicilio in facturas:
        if cliente not in domicilios:
            domicilios[cliente] = set()

        domicilios[cliente].add(domicilio)

    return {cliente: list(domicilios_cliente) for cliente, domicilios_cliente in domicilios.items()}

if __name__=="__main__":

    compras = [
        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
        ("Jorge Russo", 7, 699, "Mirasol 218"),
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
        ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
        ("Jorge Russo", 15, 958, "Mirasol 218"),
    ]

    resultado = obtener_domicilios_facturas(compras)

    for cliente, domicilios in resultado.items():
        print(f'Cliente: {cliente}, Domicilios: {domicilios}')
