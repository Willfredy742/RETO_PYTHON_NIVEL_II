from validations import validate_not_empty, validate_price, validate_status, validate_description

catalog = []


def add_collectible(name, category, price, status, description):
    clean_name = validate_not_empty(name, "name")
    clean_category = validate_not_empty(category, "category")
    clean_price = validate_price(price)
    clean_status = validate_status(status)
    clean_description = validate_description(description)

    new_item = {
        "id": len(catalog) + 1,
        "name": clean_name,
        "category": clean_category,
        "price": clean_price,
        "status": clean_status,
        "description": clean_description
    }

    catalog.append(new_item)
    return new_item


def get_catalog():
    return catalog