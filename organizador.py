import os
import shutil

DIR_ALVO = "./meus_arquivos"

MAPA_EXT = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Codigos": [".py", ".html", ".css", ".js"],
    "Outros": []
}

def setup_dirs():
    if not os.path.exists(DIR_ALVO):
        os.makedirs(DIR_ALVO)
    for cat in MAPA_EXT.keys():
        path_cat = os.path.join(DIR_ALVO, cat)
        if not os.path.exists(path_cat):
            os.makedirs(path_cat)
    print("[INFO] Estrutura de pastas organizadas criada!")

def organizar():
    if not os.path.exists(DIR_ALVO):
        print("[ERRO] Pasta alvo não encontrada.")
        return

    arquivos = os.listdir(DIR_ALVO)
    movidos = 0

    for arq in arquivos:
        src = os.path.join(DIR_ALVO, arq)
        if os.path.isfile(src):
            _, ext = os.path.splitext(arq)
            ext = ext.lower()
            
            dest_cat = "Outros"
            for cat, exts in MAPA_EXT.items():
                if ext in exts:
                    dest_cat = cat
                    break
            
            dest = os.path.join(DIR_ALVO, dest_cat, arq)
            shutil.move(src, dest)
            print(f"[MOVE] '{arq}' -> {dest_cat}/")
            movidos += 1

    print(f"\n[SUCESSO] Organização concluída! Total de arquivos movidos: {movidos}")

if __name__ == "__main__":
    setup_dirs()
    organizar()