class Personagem:
    def __init__(self, nome, descricao, link_imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.link_imagem = link_imagem
        self.programa = programa
        self.animador = animador

    @classmethod
    def criar_personagem(cls):
        nome = input("Qual nome do personagem?")
        descricao = input("Digite a descrição do seu personagem:")
        link_imagem = input("Digite o link para a imagem do personagem:")
        programa = input("Digite o programa do seu personagem:")
        animador = input(
            "Digite o nome do animador responsável pelo personagem:")
        return cls(nome, descricao, link_imagem, programa, animador)

    def visualizar_personagens(self, personagens):
        for i, personagem in enumerate(personagens):
            print(f"personagem {i+1}")
            print(f"nome: {personagem.nome}")
            print(f"descrição: {personagem.descricao}")
            print(f"link para imagem: {personagem.link_imagem}")
            print(f"programa: {personagem.programa}")
            print(f"animador: {personagem.animador}")
            print("")


personagens = []

while True:
    print("1 - Criar personagem")
    print("2 - Visualizar personagens")
    print("3 - Sair")
    opcao = input("Digite a opção desejada:")
    if opcao == "1":
        personagem = Personagem.criar_personagem()
        personagens.append(personagem)
    elif opcao == "2":
        if len(personagens) > 0:
            personagem.visualizar_personagens(personagens)
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
