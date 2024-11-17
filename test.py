from main import CRUDProductos

def pruebas_crud():
    crud = CRUDProductos()

    # *** CREAR PRODUCTOS ***
    print("\n[CREAR PRODUCTO - ÉXITO]")
    crud.crear_producto("1", "Producto 1", "Descripción 1", 10.99, 5)  # Éxito
    crud.crear_producto("2", "Producto 2", "Descripción 2", 20.50, 10)  # Éxito

    print("\n[CREAR PRODUCTO - FALLA]")
    crud.crear_producto("1", "Producto Duplicado", "Descripción duplicada", 15.99, 10)  # ID duplicado

    # *** LEER PRODUCTOS ***
    print("\n[LEER PRODUCTOS - ÉXITO]")
    crud.leer_productos()  # Lista con productos

    print("\n[LEER PRODUCTOS - FALLA]")
    print("Intentando leer productos en una lista vacía:")
    crud_vacio = CRUDProductos()
    crud_vacio.leer_productos()  # Lista vacía

    # *** ACTUALIZAR PRODUCTO ***
    print("\n[ACTUALIZAR PRODUCTO - ÉXITO]")
    crud.actualizar_producto("1", nombre="Producto Actualizado", precio=12.99)  # Éxito

    print("\n[ACTUALIZAR PRODUCTO - FALLA]")
    crud.actualizar_producto("999", nombre="Producto Inexistente")  # Producto no encontrado

    # *** ELIMINAR PRODUCTO ***
    print("\n[ELIMINAR PRODUCTO - ÉXITO]")
    crud.eliminar_producto("2")  # Éxito

    print("\n[ELIMINAR PRODUCTO - FALLA]")
    crud.eliminar_producto("999")  # Producto no encontrado

    # *** BUSCAR PRODUCTOS ***
    print("\n[BUSCAR PRODUCTO - ÉXITO]")
    crud.buscar_producto("1")  # Producto encontrado

    print("\n[BUSCAR PRODUCTO - FALLA]")
    crud.buscar_producto("2")  # Producto no encontrado (ya eliminado)

if __name__ == "__main__":
    pruebas_crud()