import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from BST import BST
from ExtraWindows import InsertNameWindow, ShowInfoWindow, ShowLevelOrderWindow, ShowTreeWindow, ShowEmptyTreeWindow, ShowTraversalsWindow
from BSTVizualizer import TreeVisualizer

class BSTApp:
    def __init__(self, root):
        self.bst = None  # Inicialmente, a árvore está vazia
        self.initialize_gui(root)

    def initialize_gui(self, root):
        self.root = root
        self.root.title("BSTree Apples")

        self.root.geometry("800x600")

        # Carregar o ícone da janela principal
        icon = tk.PhotoImage(file='icon-quadrado.gif')
        self.root.iconphoto(True, icon)  # Definir o ícone da janela principal

        # Carregar a imagem
        self.logo = tk.PhotoImage(file="mainwindow.png")
        self.logo_reduzida = self.logo.subsample(4, 4)  # Reduzir o tamanho 
        self.label_logo = tk.Label(self.root, image=self.logo_reduzida)
        self.label_logo.pack()

        #criar frame para título e subtítulo
        self.frame_title = tk.Frame(self.root)
        self.frame_title.pack()
        # Criar o título
        self.label_title = tk.Label(self.frame_title, text="BSTree Apples", font=("Roboto", 20))
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

        self.btn_show_level_order = ttk.Button(self.frame_buttons, text="Mostrar Nível a Nível", command=self.show_LevelOrder, style="MeuEstilo.TButton")
        self.btn_show_level_order.pack(side=tk.TOP, padx=5, pady=5)

        self.btn_show_tree = ttk.Button(self.frame_buttons, text="Mostrar Árvore Gráfica", command=self.show_graphical_tree, style="MeuEstilo.TButton")
        self.btn_show_tree.pack(side=tk.TOP, padx=5, pady=5)

        # Criar o botão para sair do programa
        self.btn_exit = ttk.Button(self.root, text="Sair do Programa", command=self.root.quit, style="MeuEstilo.TButton")
        self.btn_exit.pack(side=tk.RIGHT, padx=10, pady=10)  # Posicionar à direita

    def create_bst(self):
        # Cria uma nova instância da classe BST
        self.bst = BST()

        # Abre uma nova janela para inserção de nomes
        InsertNameWindow(self.root, self.bst)

        # Inicializa a árvore com os valores inseridos pelo usuário
        for name in self.bst.keys:
            self.bst.insert(name)
    
    '''def get_info(self):
        if self.bst is None:
            ShowEmptyTreeWindow(self.root)
            return None
        else:
            size = self.bst.get_size()
            internal_length = self.bst.get_inner_length(self.bst.root)
            balanced = self.bst.is_balanced()

            return size, internal_length, balanced'''


    def show_info(self):
        # Implementação para mostrar informações da árvore
        if self.bst is None:
            ShowEmptyTreeWindow(self.root)
        else:
            #size, internal_length, balanced = self.get_info()
            ShowInfoWindow(self.root, self.bst)


    def show_internal_length(self):
        # Implementação para mostrar o comprimento interno da árvore
        if self.bst is not None:
            internal_length = self.bst.get_inner_length(self.bst.root)

            # Criar um popup para mostrar o comprimento interno
            pop_up = tk.Toplevel(self.root)
            pop_up.title("Comprimento Interno")

            # Criar um label com o comprimento interno
            label = tk.Label(pop_up, text="Comprimento interno: {}".format(internal_length))
            label.pack()

            # Criar um botão para fechar o popup
            btn_close = tk.Button(pop_up, text="Fechar", command=pop_up.destroy)
            btn_close.pack()

        else:
            # Se a árvore não existe, mostrar uma mensagem de erro
            ShowEmptyTreeWindow(self.root)


    def is_balanced(self):
        if self.bst is None:
            ShowEmptyTreeWindow(self.root)
        else:
            balanced = self.bst.is_balanced()
            if balanced:
                result_message = "A árvore está balanceada."
                image = tk.PhotoImage(file="ok.png")
            else:
                result_message = "A árvore não está balanceada."
                image = tk.PhotoImage(file="oknot.png")

            result_dialog = tk.Toplevel(self.root)
            result_dialog.title("Verificação de Balanceamento")

            result_label = tk.Label(result_dialog, image=image)
            result_label.pack()

            result_label = tk.Label(result_dialog, text=result_message, font=("Roboto", 12))
            result_label.pack(padx=20, pady=20)

            return_button = tk.Button(result_dialog, text="Voltar", command=result_dialog.destroy, style="MeuEstilo.TButton")
            return_button.pack(pady=10)


    def show_traversals(self):
        if self.bst is None:
            ShowEmptyTreeWindow(self.root)
        else:
            # Criar uma nova janela para mostrar as travessias
            ShowTraversalsWindow(self.root, self.bst)

    def show_graphical_tree(self):
        # Implementação para mostrar a árvore gráfica
        if self.bst is None:
            ShowEmptyTreeWindow(self.root)
        else:
            viz = TreeVisualizer(self.bst)
            viz.main()
            ShowTreeWindow(self.root, self.bst)

    def show_LevelOrder(self):
        if self.bst is None:
            ShowEmptyTreeWindow(self.root)
        else:
            ShowLevelOrderWindow(self.root, self.bst)

if __name__ == "__main__":
    root = tk.Tk()
    app = BSTApp(root)
    root.mainloop()
