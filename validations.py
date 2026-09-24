def validate_not_empty(value, field_name):
    if not value.strip():
        raise ValueError(f"El campo '{field_name}' no puede estar vacío.")
    return value.strip()

