import tkinter as tk
from tkinter import messagebox

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro App")
        self.root.geometry("600x400")

        # Variáveis para armazenar os dados do cadastro
        self.codigo_var = tk.StringVar()
        self.nome_var = tk.StringVar()
        self.rua_var = tk.StringVar()
        self.bairro_var = tk.StringVar()
        self.cidade_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.cep_var = tk.StringVar()
        self.celular_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.cpf_var = tk.StringVar()
        self.rg_var = tk.StringVar()

        # Criar e posicionar os rótulos e campos de entrada
        tk.Label(root, text="Código:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.codigo_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Nome:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.nome_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Rua:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.rua_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Bairro:").grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.bairro_var).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Cidade:").grid(row=4, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.cidade_var).grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Estado:").grid(row=5, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.estado_var).grid(row=5, column=1, padx=10, pady=5)

        tk.Label(root, text="CEP:").grid(row=6, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.cep_var).grid(row=6, column=1, padx=10, pady=5)

        tk.Label(root, text="Celular:").grid(row=7, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.celular_var).grid(row=7, column=1, padx=10, pady=5)

        tk.Label(root, text="E-mail:").grid(row=8, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.email_var).grid(row=8, column=1, padx=10, pady=5)

        tk.Label(root, text="CPF:").grid(row=9, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.cpf_var).grid(row=9, column=1, padx=10, pady=5)

        tk.Label(root, text="RG:").grid(row=10, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.rg_var).grid(row=10, column=1, padx=10, pady=5)

        # Botões para salvar e consultar cadastros
        tk.Button(root, text="Salvar", command=self.salvar_cadastro).grid(row=11, column=0, pady=10)
        tk.Button(root, text="Consultar", command=self.consultar_cadastros).grid(row=11, column=1, pady=10)

    def salvar_cadastro(self):
        # Obter os valores dos campos de entrada
        codigo = self.codigo_var.get()
        nome = self.nome_var.get()
        rua = self.rua_var.get()
        bairro = self.bairro_var.get()
        cidade = self.cidade_var.get()
        estado = self.estado_var.get()
        cep = self.cep_var.get()
        celular = self.celular_var.get()
        email = self.email_var.get()
        cpf = self.cpf_var.get()
        rg = self.rg_var.get()

        # Validar se todos os campos estão preenchidos
        if not codigo or not nome or not rua or not bairro or not cidade or not estado or not cep or not celular or not email or not cpf or not rg:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        # Salvar os dados no arquivo de texto
        with open("cadastros.txt", "a") as file:
            file.write(f"{codigo}, {nome}, {rua}, {bairro}, {cidade}, {estado}, {cep}, {celular}, {email}, {cpf}, {rg}\n")

        # Limpar os campos de entrada após salvar
        self.codigo_var.set("")
        self.nome_var.set("")
        self.rua_var.set("")
        self.bairro_var.set("")
        self.cidade_var.set("")
        self.estado_var.set("")
        self.cep_var.set("")
        self.celular_var.set("")
        self.email_var.set("")
        self.cpf_var.set("")
        self.rg_var.set("")

        messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso.")

    def consultar_cadastros(self):
        # Abrir o arquivo de texto e exibir os cadastros
        try:
            with open("cadastros.txt", "r") as file:
                cadastros = file.read()

            messagebox.showinfo("Cadastros", cadastros)
        except FileNotFoundError:
            messagebox.showinfo("Aviso", "Nenhum cadastro encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()
