import os
import json
import shutil
import unicodedata
import re


def unicode_to_filename(unicode_str):
    """Converte unicode do JSON para nome de arquivo PNG (formato do repositório)."""
    parts = unicode_str.strip().split()
    filename = "-".join([p.lower() for p in parts]) + ".png"
    return filename


def formatar_nome(nome):
    """Formata o nome: minúsculo, underscore, sem acento, vírgula ou caracteres especiais."""
    nome = nome.lower()  # Converte para minúsculo
    nome = unicodedata.normalize("NFD", nome)  # Normaliza a string (remove acentos)
    nome = nome.encode("ascii", "ignore").decode("utf-8")  # Remove acentos
    nome = nome.replace(" ", "_")  # Substitui espaços por underscores
    nome = nome.replace(",", "_")  # Substitui vírgulas por underscores
    nome = re.sub(
        r"[^a-z0-9_]", "", nome
    )  # Remove qualquer caractere que não seja letra, número ou underscore
    return nome


def carregar_emojis(caminho_json):
    """Carrega emojis de um arquivo JSON."""
    try:
        with open(caminho_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("emojis", [])
    except Exception as e:
        print(f"❌ Erro ao ler {caminho_json}: {e}")
        return []


def criar_dicionario_ptbr(lista_ptbr):
    """Cria um dicionário com unicode como chave (em lowercase) e nome_ptbr como valor."""
    mapa = {}
    for item in lista_ptbr:
        unicode_key = item.get("unicode", "").strip().lower()
        nome_pt = item.get("name_ptbr", "").strip()
        if unicode_key and nome_pt:
            mapa[unicode_key] = nome_pt
    return mapa


def nome_unico(destino_dir, base_name):
    """Garante que o nome final do arquivo seja único, evitando sobrescritas."""
    nome_final = base_name
    contador = 1
    while os.path.exists(os.path.join(destino_dir, nome_final)):
        nome_final = f"{os.path.splitext(base_name)[0]}_{contador}.png"
        contador += 1
    return nome_final


def copiar_emojis(emojis_en, mapa_ptbr, pasta_origem, pasta_destino):
    """Copia e renomeia os arquivos de emoji."""
    os.makedirs(pasta_destino, exist_ok=True)
    total, copiados = 0, 0

    for emoji in emojis_en:
        unicode_str = emoji.get("unicode", "").strip()
        name_en = formatar_nome(emoji.get("name", ""))
        name_ptbr_raw = mapa_ptbr.get(unicode_str.lower())

        if not name_ptbr_raw:
            print(f"⚠️ Sem nome PT-BR para: {unicode_str}")
            continue

        name_ptbr = formatar_nome(name_ptbr_raw)

        nome_completo = f"{name_en}-{name_ptbr}.png"

        nome_arquivo_origem = unicode_to_filename(unicode_str)
        nome_arquivo_destino = nome_unico(pasta_destino, nome_completo)

        origem = os.path.join(pasta_origem, nome_arquivo_origem)
        destino = os.path.join(pasta_destino, nome_arquivo_destino)

        total += 1
        if os.path.exists(origem):
            shutil.copy2(origem, destino)
            print(f"✅ Copiado: {nome_arquivo_origem} → {nome_arquivo_destino}")
            copiados += 1
        else:
            print(f"⚠️ Não encontrado: {nome_arquivo_origem}")

    print(f"\n📦 Resultado: {copiados}/{total} arquivos copiados com sucesso.")


if __name__ == "__main__":
    caminho_json_en = "emoji_map.json"
    caminho_json_ptbr = "emoji_map_ptbr.json"
    pasta_origem = "input"
    pasta_destino = "output"

    print("🚀 Iniciando script...")

    print("📥 Carregando emoji_map.json...")
    lista_en = carregar_emojis(caminho_json_en)

    print("📥 Carregando emoji_map_ptbr.json...")
    lista_ptbr = carregar_emojis(caminho_json_ptbr)

    print("🔄 Criando mapa PT-BR...")
    mapa_ptbr = criar_dicionario_ptbr(lista_ptbr)

    print("🛠️ Iniciando cópia dos emojis...")
    copiar_emojis(lista_en, mapa_ptbr, pasta_origem, pasta_destino)

    print("✅ Finalizado.")
