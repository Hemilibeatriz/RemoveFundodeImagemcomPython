from rembg import remove
from PIL import Image

caminho_entrada = "foto2.jpeg"
caminho_saida = "foto2_semfundo.png"

entrada = Image.open(caminho_entrada)
saida = remove(entrada)

saida.save(caminho_saida)
