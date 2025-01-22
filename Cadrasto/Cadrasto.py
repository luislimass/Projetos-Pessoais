import tkinter as tk
from tkinter import ttk, messagebox
import json

class ProductApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro e Listagem de Produtos")
        self.products = []
        self.load_products()
        
        self.create_main_window()

    def create_main_window(self):
        # Frames
        self.form_frame = ttk.Frame(self.root, padding="10")
        self.form_frame.grid(row=0, column=0, sticky="nsew")

        self.list_frame = ttk.Frame(self.root, padding="10")
        self.list_frame.grid(row=0, column=1, sticky="nsew")

        self.create_form()
        self.create_list()

    def create_form(self):
        ttk.Label(self.form_frame, text="Nome do Produto:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(self.form_frame, width=30)
        self.name_entry.grid(row=0, column=1, sticky="w")

        ttk.Label(self.form_frame, text="Descrição do Produto:").grid(row=1, column=0, sticky="w")
        self.desc_entry = ttk.Entry(self.form_frame, width=30)
        self.desc_entry.grid(row=1, column=1, sticky="w")

        ttk.Label(self.form_frame, text="Valor do Produto:").grid(row=2, column=0, sticky="w")
        self.value_entry = ttk.Entry(self.form_frame, width=30)
        self.value_entry.grid(row=2, column=1, sticky="w")

        ttk.Label(self.form_frame, text="Disponível para Venda:").grid(row=3, column=0, sticky="w")
        self.available_var = tk.StringVar(value="sim")
        ttk.Radiobutton(self.form_frame, text="Sim", variable=self.available_var, value="sim").grid(row=3, column=1, sticky="w")
        ttk.Radiobutton(self.form_frame, text="Não", variable=self.available_var, value="não").grid(row=3, column=2, sticky="w")

        ttk.Button(self.form_frame, text="Cadastrar Produto", command=self.add_product).grid(row=4, column=0, columnspan=3, pady=10)

    def create_list(self):
        self.tree = ttk.Treeview(self.list_frame, columns=("Valor"), show="headings")
        self.tree.heading("#1", text="Nome")
        self.tree.heading("Valor", text="Valor")
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.list_frame.rowconfigure(0, weight=1)
        self.list_frame.columnconfigure(0, weight=1)

        ttk.Button(self.list_frame, text="Novo Produto", command=self.switch_to_form).grid(row=1, column=0, pady=10)

        self.refresh_list()

    def switch_to_form(self):
        self.form_frame.tkraise()

    def refresh_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        sorted_products = sorted(self.products, key=lambda p: p['value'])
        for product in sorted_products:
            self.tree.insert("", "end", values=(product['name'], product['value']))

    def add_product(self):
        name = self.name_entry.get().strip()
        desc = self.desc_entry.get().strip()
        try:
            value = float(self.value_entry.get().strip())
        except ValueError:
            messagebox.showerror("Erro", "O valor do produto deve ser numérico.")
            return
        available = self.available_var.get()

        if not name or not desc:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        self.products.append({"name": name, "description": desc, "value": value, "available": available})
        self.save_products()
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        self.refresh_list()
        self.list_frame.tkraise()

    def save_products(self):
        with open("products.json", "w") as file:
            json.dump(self.products, file)

    def load_products(self):
        try:
            with open("products.json", "r") as file:
                self.products = json.load(file)
        except FileNotFoundError:
            self.products = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductApp(root)
    root.mainloop()
