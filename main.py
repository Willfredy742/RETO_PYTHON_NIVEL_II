from catalog import add_collectible, get_catalog

def main():
    while True:
        print("\n--- Collectibles Catalog System ---")
        print("1. Agregar una pieza")
        print("2. Mostrar el catálogo")
        print("3. Salir")

        choice = input("\nElige una opción (1-3): ").strip()

        if choice == "1":
            try:
                name = input("Nombre: ")
                category = input("Categoría: ")
                price = float(input("Precio: "))
                status = input("Estado (disponible/reservada/vendida): ")
                description = input("Descripción (debe contener 'usada'): ")

                new_item = add_collectible(name, category, price, status, description)
                print(f"\n¡Coleccionable agregado con éxito!: {new_item}")
            except ValueError as e:
                print(f"\nError de validación: {e}")

        elif choice == "2":
            catalog_items = get_catalog()
            if not catalog_items:
                print("\nEl catálogo está vacío.")
            else:
                print("\nCatálogo actual:")
                for item in catalog_items:
                    print(item)

        elif choice == "3":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 3.")

if __name__ == "__main__":
    main()

