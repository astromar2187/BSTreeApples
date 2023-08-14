import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from BST import BST

class ShowEmptyTreeWindow:
    def __init__(self, parent):
        self.parent = parent

        self.window = tk.Toplevel(parent)
        self.window.title("Erro: árvore vazia")

        # Carregar a imagem
        self.error = tk.PhotoImage(file="iconX-quadrado.png")
        self.error_reduzida = self.error.subsample(4, 4)  
        self.label_error = tk.Label(self.window, image=self.error_reduzida)
        self.label_error.image = self.error_reduzida
        self.label_error.pack()

        self.lbl_error = tk.Label(self.window, text=":/ Ainda não há maçãs nesta árvore", font=("Roboto", 18, "bold"))
        self.lbl_error.pack(pady=10)

        self.lbl_error = tk.Label(self.window, text="Crie uma árvore BST primeiro!", font=("Roboto", 12))
        self.lbl_error.pack(pady=10)

        self.btn_quit = ttk.Button(self.window, text="Voltar", command=self.window.destroy, style="MeuEstilo.TButton")
        self.btn_quit.pack(pady=10)

        # Aplicar o grab_set() para bloquear interações com a janela principal
        self.window.grab_set()

class InsertNameWindow:
    def __init__(self, parent, bst):
        self.parent = parent
        self.bst = bst

        self.window = tk.Toplevel(parent)
        self.window.title("Inserir Nome")

        self.window.geometry("400x400")

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
        self.label_tree = tk.Label(self.window, image=self.tree)
        self.label_tree.image = self.tree
        self.label_tree.pack()

        self.btn_quit = ttk.Button(self.window, text="Sair", command=self.window.destroy, style="MeuEstilo.TButton")
        self.btn_quit.pack(pady=10)

        # Aplicar o grab_set() para bloquear interações com a janela principal
        self.window.grab_set()

class ShowInfoWindow:
    def __init__(self, parent, bst):
        self.parent = parent
        self.bst = bst

        self.window = tk.Toplevel(parent)
        self.window.title("Informações da Árvore")

        self.window.geometry("400x300")

        self.lbl_info = tk.Label(self.window, text="Informações da Árvore:", font=("Roboto", 18, "bold"))
        self.lbl_info.pack(pady=10)

        # Exibir informações
        self.lbl_size = tk.Label(self.window, text=f"Tamanho: {self.bst.size}", font=("Roboto", 16))
        self.lbl_size.pack()
        
        self.lbl_height = tk.Label(self.window, text=f"Altura: {self.bst.get_height(self.bst.root)}", font=("Roboto", 16))
        self.lbl_height.pack()

        self.lbl_min = tk.Label(self.window, text=f"Nó mínimo: {self.bst.find_min()}", font=("Roboto", 16))
        self.lbl_min.pack()

        self.lbl_max = tk.Label(self.window, text=f"Nó máximo: {self.bst.find_max()}", font=("Roboto", 16))
        self.lbl_max.pack()

        self.btn_quit = ttk.Button(self.window, text="Sair", command=self.window.destroy, style="MeuEstilo.TButton")
        self.btn_quit.pack(pady=10)

        # Aplicar o grab_set() para bloquear interações com a janela principal
        self.window.grab_set()

class ShowTraversalsWindow:
    def __init__(self, parent, bst):
        self.parent = parent
        self.bst = bst

        self.window = tk.Toplevel(parent)
        self.window.title("Travessias da Árvore")
        self.window.geometry("400x400")

        self.lbl_travessia = tk.Label(self.window, text="Travessia: ", font=("Roboto", 18, "bold"))
        self.lbl_travessia.pack(pady=10)

        # Implementação para mostrar as travessias da árvore
        inorder_traversal = self.bst.inorder_traversal()
        preorder_traversal = self.bst.preorder_traversal()
        postorder_traversal = self.bst.postorder_traversal()

        # Criar um label para cada travessia
        label_inorder = tk.Label(self.window, text="In-order: {}".format(inorder_traversal), font=("Roboto", 12))
        label_preorder = tk.Label(self.window, text="Pre-order: {}".format(preorder_traversal), font=("Roboto", 12))
        label_postorder = tk.Label(self.window, text="Post-order: {}".format(postorder_traversal), font=("Roboto", 12))

        # Packar os labels no popup
        label_inorder.pack()
        label_preorder.pack()
        label_postorder.pack()


        self.btn_quit = ttk.Button(self.window, text="Sair", command=self.window.destroy, style="MeuEstilo.TButton")
        self.btn_quit.pack(pady=10)

        # Aplicar o grab_set() para bloquear interações com a janela principal
        self.window.grab_set()

class ShowLevelOrderWindow:
    def __init__(self, parent, bst):
        self.parent = parent
        self.bst = bst

        self.window = tk.Toplevel(parent)
        self.window.title("Travessia em Nível")
        self.window.geometry("400x400")

        self.lbl_travessia = tk.Label(self.window, text="Travessia em Nível: ", font=("Roboto", 18, "bold"))
        self.lbl_travessia.pack(pady=10)

        # Implementação para mostrar a travessia em nível da árvore
        level_order_traversal = self.bst.level_order()

        # Criar um label para a travessia em nível
        label_level_order = tk.Label(self.window, text="Level-order: {}".format(level_order_traversal), font=("Roboto", 12))

        # Packar o label no popup
        label_level_order.pack()

        self.btn_quit = ttk.Button(self.window, text="Sair", command=self.window.destroy, style="MeuEstilo.TButton")
        self.btn_quit.pack(pady=10)

        # Aplicar o grab_set() para bloquear interações com a janela principal
        self.window.grab_set()
