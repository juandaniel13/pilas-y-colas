import threading
import time
import random

from user import *
from pago import *
from estrategia import *
from cola import Cola

def main() -> None:
    """
    Función principal que simula el proceso de compra de boletas.
    """
    COSTO_BOLETA = 500000

    # Crear objetos de pago
    PAGO_DIGITAL = PagoDigital()
    PAGO_EFECTIVO = PagoEfectivo()

    # Crear lista de clientes
    CLIENTES = [
        UsuarioIntermedio("Johan", "correo1@gmail.com", PAGO_DIGITAL),
        UsuarioIntermedio("Andres", "correo2@gmail.com", PAGO_EFECTIVO),
        UsuarioPrivilegiado("Daniel", "correo3@gmail.com", PAGO_DIGITAL),
        UsuarioPrivilegiado("Juan", "correo4@gmail.com", PAGO_EFECTIVO),
    ]

    # Crear una cola para manejar la espera de los clientes
    COLA = Cola()

    # Crear una estrategia de pago
    estrategia = ContextoEstrategia()

    # Variable para controlar la ejecución del hilo
    ejecutar = True

    # Función para enviar clientes a comprar
    def mandar_clientes_a_comprar() -> None:
        """
        Función que envía clientes a comprar boletas.
        """
        while ejecutar:
            time.sleep(1)
            cliente = random.choice(CLIENTES)
            estrategia.establecer_estrategia(cliente)
            resultado, cantidad_boletas = estrategia.definir_pago(COSTO_BOLETA, cliente)
            COLA.queue((resultado, cantidad_boletas, str(cliente)))

    # Iniciar hilo para enviar clientes a comprar
    ejecucion_clientes = threading.Thread(target=mandar_clientes_a_comprar)
    ejecucion_clientes.start()

    # Bucle principal de procesamiento
    while True:
        time.sleep(3)
        if COLA.tam() == 0:
            continue

        print(f"Clientes en cola: {COLA}")
        resultado, cantidad_boletos, datos_cliente = COLA.dequeue()
        print()
        print(f"Compra: {resultado}, Cantidad Boletas: {cantidad_boletos} \n {datos_cliente}")
        print()

        if COLA.tam() >= 20:
            ejecutar = False

        if not ejecutar and COLA.tam() == 0:
            break

    ejecucion_clientes.join()

if __name__ == '__main__':
    main()
