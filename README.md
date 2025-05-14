# 🧠 Emoji Translator - Lousa Edition

Este script Python automatiza a tarefa de copiar e renomear arquivos de emoji, combinando nomes em Inglês com suas respectivas traduções em Português (PT-BR), baseado em dois arquivos JSON.

## 📌 Objetivo

Gerar arquivos `.png` com nomes mais amigáveis e compreensíveis para humanos, utilizando tanto a descrição original em inglês quanto a tradução para o português.

Formato final dos arquivos:

```
english_name-portuguese_name.png
```

Exemplo:

```
black_circle-circulo_preto.png
```

---

## 📁 Estrutura Esperada

```
.
├── emoji_map.json              # Lista de emojis com nomes em inglês
├── emoji_map_ptbr.json         # Lista de emojis com nomes em português
├── input/                      # Contém os arquivos PNG (baseados no unicode)
│   └── 1f600.png
├── output/                     # Destino dos arquivos renomeados
└── main.py                     # Script principal
```

---

## ⚙️ Como Funciona

1. Carrega os dados dos arquivos `emoji_map.json` (inglês) e `emoji_map_ptbr.json` (PT-BR).
2. Cria um dicionário que mapeia o unicode para o nome traduzido.
3. Formata os nomes removendo acentos, caracteres especiais e convertendo tudo para lowercase com underscore.
4. Verifica a existência dos arquivos `.png` correspondentes ao unicode.
5. Copia os arquivos da pasta `input/` para `output/`, renomeando no formato `nome_en-nome_ptbr.png`.
6. Evita sobrescritas criando nomes únicos, se necessário.

---

## ▶️ Como Usar

1. Adicione seus arquivos `.json` e as imagens `.png` conforme a estrutura.
2. Execute:

```bash
python main.py
```

3. Confira os arquivos renomeados na pasta `output/`.

---

## 🧾 Exemplo dos Arquivos JSON

### `emoji_map.json`

```json
{
  "emojis": [
    {
      "emoji": "\u26AB",
      "name": "black circle",
      "shortname": ":black_circle:",
      "unicode": "26AB",
      "category": "Symbols",
      "order": 1
    }
  ]
}
```

### `emoji_map_ptbr.json`

```json
{
  "emojis": [
    {
      "unicode": "26AB",
      "name_ptbr": "círculo preto",
      "shortname_ptbr": ":circulo_preto:"
    }
  ]
}
```

---

## 🛠 Requisitos

* Python 3.6 ou superior
* Nenhuma biblioteca externa necessária

---

## 📌 Notas

* Caso o nome em português não seja encontrado, o emoji é ignorado com aviso no terminal.
* Arquivos com nomes duplicados recebem um sufixo incremental (ex: `_1`, `_2`, ...).

---

## 📃 Licença

Este projeto é open source e está sob a licença MIT.

---

Feito com 💻 e carinho para facilitar o uso de emojis em projetos visuais.

GitHub: [https://github.com/EngDiego](https://github.com/EngDiego)
