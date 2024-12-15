import tkinter as tk
from tkinter import messagebox

def create_gui(root):
    """Создает графический интерфейс."""
    font_size = 14
    font = ("Arial", font_size)

    # Создаем главное окно
    window = tk.Tk()
    window.title("Калькулятор наружной рекламы")

    # Увеличиваем размер шрифта для всех меток
    font_size = 14  # Размер шрифта
    font = ("Times New Roman", font_size) # Шрифт и его размер

    # Надписи и поля ввода
    area_label = tk.Label(window, text="Площадь (кв.м):", font=font)
    area_label.grid(row=0, column=0, padx=10, pady=15, sticky="w") # Увеличенное pady
    area_entry = tk.Entry(window, font=font)
    area_entry.grid(row=0, column=1, padx=10, pady=15)

    material_cost_label = tk.Label(window, text="Стоимость материала (руб./кв.м):", font=font)
    material_cost_label.grid(row=1, column=0, padx=10, pady=15, sticky="w")
    material_cost_entry = tk.Entry(window, font=font)
    material_cost_entry.grid(row=1, column=1, padx=10, pady=15)

    installation_cost_label = tk.Label(window, text="Стоимость монтажа (руб.):", font=font)
    installation_cost_label.grid(row=2, column=0, padx=10, pady=15, sticky="w")
    installation_cost_entry = tk.Entry(window, font=font)
    installation_cost_entry.grid(row=2, column=1, padx=10, pady=15)

    additional_services_cost_label = tk.Label(window, text="Дополнительные услуги (руб.):", font=font)
    additional_services_cost_label.grid(row=3, column=0, padx=10, pady=15, sticky="w")
    additional_services_cost_entry = tk.Entry(window, font=font)
    additional_services_cost_entry.grid(row=3, column=1, padx=10, pady=15)

    calculate_button = tk.Button(root, text="Рассчитать", command=lambda: process_calculation(root), font=font)
    calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

    result_label = tk.Label(root, text="", font=font)
    result_label.grid(row=5, column=0, columnspan=2)

    #Добавляем обработку вывода результата и ошибок
    def process_calculation(root):
        try:
            area = float(area_entry.get())
            material_cost = float(material_cost_entry.get())
            installation_cost = float(installation_cost_entry.get())
            additional_services_cost = float(additional_services_cost_entry.get())

            if area <= 0 or material_cost <= 0:
                raise ValueError("Площадь и стоимость материала должны быть положительными числами.")
            if installation_cost < 0 or additional_services_cost < 0:
                raise ValueError("Стоимость монтажа и дополнительных услуг не могут быть отрицательными.")

            total_cost = calculate_cost(area, material_cost, installation_cost, additional_services_cost)
            result_label.config(text=f"Итоговая стоимость: {total_cost:.2f} руб.")

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла неизвестная ошибка: {e}")


    #Возвращаем необходимые переменные для доступа из main.py
    return area_entry, material_cost_entry, installation_cost_entry, additional_services_cost_entry, result_label


