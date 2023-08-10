import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from BST import BST
from ExtraWindows import InsertNameWindow, ShowTreeWindow
from BSTVizualizer import TreeVisualizer

class BSTApp:
    def __init__(self, root):
        self.bst = None  # Inicialmente, a árvore está vazia
        self.initialize_gui(root)

    def initialize_gui(self, root):
        self.root = root
        self.root.title("BYSTree Apples")

        # Carregar a imagem
        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_reduzida = self.logo.subsample(4, 4)  # Reduzir o tamanho 
        self.label_logo = tk.Label(self.root, image=self.logo_reduzida)
        self.label_logo.pack()

        #criar frame para título e subtítulo
        self.frame_title = tk.Frame(self.root)
        self.frame_title.pack()
        # Criar o título
        self.label_title = tk.Label(self.frame_title, text="BYSTree Apples", font=("Roboto", 20))
        self.label_title.pack(side=tk.TOP)
        # Criar o subtítulo
        self.label_subtitle = tk.Label(self.frame_title, text="Manipulando árvores binárias de busca", font=("Roboto", 12))
        self.label_subtitle.pack(side=tk.TOP)


        # Estilo para os botões
        estilo = ttk.Style()
        estilo.configure("MeuEstilo.TButton", background="#0C7686", foreground="#737373", font=("Lato", 12), borderwidth=0)

        # Criar o frame para os botões
        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(pady=20)

        self.btn_create_bst = ttk.Button(self.frame_buttons, text="Criar Árvore BST", command=self.create_bst, style="MeuEstilo.TButton")
        self.btn_create_bst.pack(side=tk.TOP, padx=5, pady=5)

        self.btn_show_info = ttk.Button(self.frame_buttons, text="Mostrar Informações", command=self.show_info, style="MeuEstilo.TButton")
        self.btn_show_info.pack(side=tk.TOP, padx=5, pady=5)

        self.btn_internal_length = ttk.Button(self.frame_buttons, text="Mostrar Comprimento Interno", command=self.show_internal_length, style="MeuEstilo.TButton")
        self.btn_internal_length.pack(side=tk.TOP, padx=5, pady=5)

        self.btn_is_balanced = ttk.Button(self.frame_buttons, text="Verificar se é Balanceada", command=self.is_balanced, style="MeuEstilo.TButton")
        self.btn_is_balanced.pack(side=tk.TOP, padx=5, pady=5)

        self.btn_traversals = ttk.Button(self.frame_buttons, text="Mostrar Travessias", command=self.show_traversals, style="MeuEstilo.TButton")
        self.btn_traversals.pack(side=tk.TOP, padx=5, pady=5)

        self.btn_show_tree = ttk.Button(self.frame_buttons, text="Mostrar Árvore Gráfica", command=self.show_graphical_tree, style="MeuEstilo.TButton")
        self.btn_show_tree.pack(side=tk.TOP, padx=5, pady=5)

    def create_bst(self):
        # Cria uma nova instância da classe BST
        self.bst = BST()
        # Cria uma nova janela para inserção de nomes
        insert_name_window = InsertNameWindow(self.root, self.bst)

    def show_info(self):
        # Implementação para mostrar informações da árvore
        pass

    def show_internal_length(self):
        # Implementação para mostrar o comprimento interno da árvore
        pass

    def is_balanced(self):
        # Implementação para verificar se a árvore é balanceada
        pass

    def show_traversals(self):
        # Implementação para mostrar as travessias da árvore
        pass

    def show_graphical_tree(self):
        # Implementação para mostrar a árvore gráfica
        viz = TreeVisualizer(self.bst)
        viz.main()
        show_tree_window = ShowTreeWindow(self.root, self.bst)

if __name__ == "__main__":
    root = tk.Tk()
    app = BSTApp(root)
    root.mainloop()

