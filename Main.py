import tkinter as tk
def copy_text():
    # Получаем текст из первого текстового поля
    text_to_copy = entry1.get()
    # Очищаем второе текстовое поле и вставляем туда текст
    entry2.delete(0, tk.END)
    entry2.insert(0, text_to_copy)
# Создание главного окна
root = tk.Tk()
root.title("Текстовое копирование")
# Создание первого текстового поля
entry1 = tk.Entry(root)
entry1.pack(padx=10, pady=5)
# Создание второго текстового поля
entry2 = tk.Entry(root)
entry2.pack(padx=10, pady=5)
# Создание кнопки для копирования текста
copy_button = tk.Button(root, text="Копировать текст из первого поля во второе", command=copy_text)
copy_button.pack(pady=5)
# Запуск основного цикла событий
print("Hello world")
root.geometry("400x200")
root.mainloop()
