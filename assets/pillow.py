import os
from PIL import Image

PASTA_ORIGEM = "assets/portraits-sem_pillow"
PASTA_AJUSTADA = "assets/portraits"
os.makedirs(PASTA_AJUSTADA, exist_ok=True)

# Dicionário de ajustes manuais (deslocamento X e Y em pixels)
# Valores negativos em Y movem o personagem para cima, positivos para baixo.
# A resolução original de cada imagem não é alterada.
AJUSTES_ESPECIFICOS = {
    "Eshmel": (30, 0), 
    "Cai": (30,10),
    "Tialla": (0,20),
    "Peter": (-10,20),
    "Ultand":(0,20),
    "Bertrand":(15,0),
    "Gaitz":(15,20),
    "Jester": (-50, 10),   
    "Goliath": (-10, 10),   
    "Dante": (0, 30),   
    "Dietrich": (-100, 10),
    "Fabio":(-10,10),
    "Esmeralda":(-15,20),
    "Mikaela":(0,30),
    "Orchel":(0,40),
    "Diego":(-50,-10),
    "Loretta":(0,20),
    "Seteth":(0,30),
    "Ninae":(0,0),
    "Theodora":(30,10),
    "Bonaventure":(-40,10),
    "Tobias":(-20,30),
    "Lilian":(0,30),
    "Lysander":(-50,30),
    "Talimun":(-10,30),
    "Ursula":(-5,20),
    "Ludia":(-10,30),
    "Simon":(30,20),
    "Fianna":(-10,30),
    "Leda":(-10,30),
    "Buccar":(-10,10),
    "Sirocco":(0,0),
    "Olympia":(-20,20),
    "Mu":(-10,30),
    "Anatolia":(-20,30),
    "Sha_Lan":(-10,30),
    "Nezha":(0,30),
    "Dadao":(-10,30),
    "Halvin":(0,40),
    "Hong_Hua":(20,40),
    "Troy":(-50,30),
    "Guzran":(-20,40),
    "Yang_Jie":(20,40),
    "Io":(-10,40),
    "Peppe":(0,40),
    "Noctula":(0,30),
    "Sofia":(-10,20),
    "Catania":(-20,20),
    "Nydine":(30,10),
    "Zarcone":(0,20),
    "Jasmine":(0,30),
    "Alexandra":(0,30),
    "Nuzzuo":(-20,30),
    "Benditz":(-10,30),
    "Centurio":(-20,40),
    "Aswan":(0,40),
    "Nathan":(-20,30),
    "Creek":(0,30),
    "Kiroc":(50,20),
    "Klapka":(30,30),
    "Tahonia":(-20,30),
}

for filename in os.listdir(PASTA_ORIGEM):
    if filename.endswith(".png"):
        char_name = os.path.splitext(filename)[0]
        caminho_img = os.path.join(PASTA_ORIGEM, filename)
        
        try:
            with Image.open(caminho_img) as img:
                largura, altura = img.size
                
                # Cria um canvas vazio com EXATAMENTE a mesma resolução original da imagem
                canvas = Image.new("RGBA", (largura, altura), (0, 0, 0, 0))
                
                x, y = 0, 0
                
                # Aplica o ajuste de posição se o personagem estiver na lista
                if char_name in AJUSTES_ESPECIFICOS:
                    offset_x, offset_y = AJUSTES_ESPECIFICOS[char_name]
                    x += offset_x
                    y += offset_y
                
                # Cola a imagem original no canvas mantendo suas dimensões originais intactas
                canvas.paste(img, (x, y), img if img.mode == 'RGBA' else None)
                
                # Salva na pasta ajustada mantendo a resolução exata
                caminho_destino = os.path.join(PASTA_AJUSTADA, filename)
                canvas.save(caminho_destino, "PNG")
                print(f"[OK] {filename} mantido em {largura}x{altura}")
                
        except Exception as e:
            print(f"[ERRO] Falha em {filename}: {e}")

print("\nProcesso concluído! As resoluções originais foram preservadas e os deslocamentos aplicados.")

from PySide6.scripts.pyside_tool import rcc; 
import sys; 

sys.argv=['rcc', 'assets/portraits.qrc', '-o', 'portraits_rc.py']; 

rcc()