import tkinter as tk
from gui import create_gui
from calculator import calculate_cost

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Калькулятор стоимости рекламных материалов")
    create_gui(root)
    root.mainloop()

