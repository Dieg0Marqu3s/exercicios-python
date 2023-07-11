from PIL import Image

def encurtar_imagem(caminho_imagem, largura, altura):
    imagem = Image.open(caminho_imagem)
    imagem_redimensionada = imagem.resize((largura, altura), Image.ANTIALIAS)
    imagem_redimensionada.save("imagem_ajustada.jpg") # Salve a imagem com o nome desejado

# Exemplo de uso:
encurtar_imagem("C:/Users/diego.marques/Documents/LOGO MAGNA E-MAIL.jpg", 800, 600)
