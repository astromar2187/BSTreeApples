import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from BST import BST


class InsertNameWindow:
    def __init__(self, parent, bst):
        self.parent = parent
        self.bst = bst

        self.window = tk.Toplevel(parent)
        self.window.title("Inserir Nome")

        self.lbl_insert = tk.Label(self.window, text="Inserir Nome:")
        self.lbl_insert.pack(pady=10)

        self.entry_name = tk.Entry(self.window)
        self.entry_name.pack(pady=10)

        self.btn_insert_name = ttk.Button(self.window, text="Inserir", command=self.insert_name, style="MeuEstilo.TButton")
        self.btn_insert_name.pack(pady=10)

        self.btn_quit = ttk.Button(self.window, text="Sair", command=self.window.destroy, style="MeuEstilo.TButton")
        self.btn_quit.pack(pady=10)

        # Aplicar o grab_set() para bloquear interações com a janela principal
        self.window.grab_set()

    def insert_name(self):
        name = self.entry_name.get()
        if name:
            self.bst.insert(name)
            messagebox.showinfo("Inserção", f"O nome '{name}' foi inserido na árvore!")
            self.entry_name.delete(0, tk.END)  # Limpa a caixa de texto para inserir o próximo nome

class ShowTreeWindow:
    def __init__(self, parent, bst):
        self.parent = parent
        self.bst = bst

        self.window = tk.Toplevel(parent)
        self.window.title("Árvore Gráfica")

        self.lbl_insert = tk.Label(self.window, text="Visualização da Árvore:")
        self.lbl_insert.pack(pady=10)

        # Carregar a imagem
        self.tree = tk.PhotoImage(file='tree.png')
        self.tree_reduzida = self.tree.subsample(2, 2)  # Reduzir o tamanho 
        self.label_tree = tk.Label(self.window, image=self.tree_reduzida)
        self.label_tree.pack()

        self.btn_quit = ttk.Button(self.window, text="Sair", command=self.window.destroy, style="MeuEstilo.TButton")
        self.btn_quit.pack(pady=10)

        # Aplicar o grab_set() para bloquear interações com a janela principal
        self.window.grab_set()
