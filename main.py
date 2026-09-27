from catalog import add_collectible, get_catalog


def main():
    print("--- Collectibles Catalog System ---")

    try:
        item = add_collectible(
            name="Vintage Watch",
            category="Accessories",
            price=150.0,
            status="disponible",
            description="Reloj de pulsera usado en excelente estado."
        )
        print(f"Coleccionable agregado con éxito: {item}")

    except ValueError as e:
        print(f"Error de validación: {e}")

    print("\nCatálogo actual:")
    print(get_catalog())


if __name__ == "__main__":
    main()

