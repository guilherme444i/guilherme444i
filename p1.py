#verificador de Eligibidade em Python

nome=str(input("digite o seu nome:"))
idade=int(input("diga a sua idade:"))
nacionalidade=str(input("Aonde Você Mora?"))
experiencia_anos = int(input("Digite a experiência em anos:"))

if idade >= 18 and experiencia_anos >= 2 and nacionalidade >= "brasil":

    tela = (nome,idade,nacionalidade,experiencia_anos)
    print("você é elegível para o emprego.")
else:
    print("vai assitir o jogo do flamengo pois você não é elegível,para o emprego.")