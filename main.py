class Producto:
    def __init__(self, id, nombre, descripcion, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class CRUDProductos:
    def __init__(self):
        self.productos = []
        self.productoNoEncontrado = "Producto no encontrado."

    def crear_producto(self, id, nombre, descripcion, precio, cantidad):
        if any(producto.id == id for producto in self.productos):
            print("Error: Ya existe un producto con el mismo ID.")
            return
        nuevo_producto = Producto(id, nombre, descripcion, precio, cantidad)
        self.productos.append(nuevo_producto)
        print("Producto creado exitosamente.")

    def leer_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
        else:
            for producto in self.productos:
                print(producto)

    def actualizar_producto(self, id, nombre=None, descripcion=None, precio=None, cantidad=None):
        if precio is not None and precio < 0:
            print("Error: El precio no puede ser negativo.")
            return
        if cantidad is not None and cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            return
        for producto in self.productos:
            if producto.id == id:
                if nombre:
                    producto.nombre = nombre
                if descripcion:
                    producto.descripcion = descripcion
                if precio:
                    producto.precio = precio
                if cantidad:
                    producto.cantidad = cantidad
                print("Producto actualizado exitosamente.")
                return
        print(self.productoNoEncontrado)

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                print("Producto eliminado exitosamente.")
                return
        print()

    def buscar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                print(f"Producto encontrado: {producto}")
                return producto
        print(self.productoNoEncontrado)
        return None


if __name__ == "__main__":
    crud = CRUDProductos()

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Crear producto")
        print("2. Leer productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                crud.crear_producto(id, nombre, descripcion, precio, cantidad)
            except ValueError:
                print("Error: Precio y cantidad deben ser valores numéricos.")

        elif opcion == "2":
            crud.leer_productos()

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            nombre = input("Nuevo nombre (presione Enter para no cambiar): ")
            descripcion = input("Nueva descripción (presione Enter para no cambiar): ")
            precio = input("Nuevo precio (presione Enter para no cambiar): ")
            cantidad = input("Nueva cantidad (presione Enter para no cambiar): ")

            try:
                crud.actualizar_producto(
                    id,
                    nombre=nombre if nombre else None,
                    descripcion=descripcion if descripcion else None,
                    precio=float(precio) if precio else None,
                    cantidad=int(cantidad) if cantidad else None,
                )
            except ValueError:
                print("Error: Precio y cantidad deben ser valores numéricos.")

        elif opcion == "4":
            id = input("ID del producto a eliminar: ")
            crud.eliminar_producto(id)

        elif opcion == "5":
            id = input("Ingrese el ID del producto a buscar: ")
            crud.buscar_producto(id)

        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")



