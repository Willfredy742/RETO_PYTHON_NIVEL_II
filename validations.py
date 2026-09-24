def validate_not_empty(value, field_name):
    if not value.strip():
        raise ValueError(f"El campo '{field_name}' no puede estar vacío.")
    return value.strip()

def validate_price(price):
    price = float(price)
    if price <= 0:
        raise ValueError("El precio debe ser mayor a cero.")
    return price

def validate_status(status):
    allowed = ["disponible", "reservada", "vendida"]
    status = status.strip().lower()
    if status not in allowed:
        raise ValueError("Estado inválido.")
    return status

