def calculate_cost(area, material_cost, installation_cost, additional_services_cost):
    """Вычисляет итоговую стоимость."""
    total_cost = (area * material_cost) + installation_cost + additional_services_cost
    return total_cost

