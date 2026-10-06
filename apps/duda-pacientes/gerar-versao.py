#!/usr/bin/env python3
"""Gera a versão do gerenciador para outra profissional, a partir do index.html da Duda.

Uso: python3 gerar-versao.py <chave> "<Título da página>" [saída]
Gera o index.html (abre direto no navegador do computador) e o publicar-no-claude.html
(para publicar como página do claude.ai, com sincronização na conta).
Ex.:  python3 gerar-versao.py marina "Consultório da Marina"

Troca só o bloco APP (sem plataformas pré-cadastradas, chave própria de armazenamento)
e o <title>. Todo o resto do código é o mesmo, então melhorias feitas no index.html
chegam às outras versões ao rodar o script de novo.
"""
import os
import re
import sys

if len(sys.argv) < 3 or not re.fullmatch(r'[a-z0-9-]+', sys.argv[1]):
    sys.exit(__doc__)
chave, titulo = sys.argv[1], sys.argv[2]
aqui = os.path.dirname(os.path.abspath(__file__))
saida = sys.argv[3] if len(sys.argv) > 3 else os.path.join(aqui, '..', f'consultorio-{chave}', 'index.html')

src = open(os.path.join(aqui, 'index.html'), encoding='utf-8').read()
ini, fim = src.index('const APP = {'), src.index('\n};\n', src.index('const APP = {')) + 3
bloco = f"""const APP = {{
  chave: '{chave}',  // prefixo do armazenamento no navegador; cada versão tem o seu
  plataformasPadrao: [],  // plataformas que já vêm cadastradas (nenhuma nesta versão)
}};"""
out = src[:ini] + bloco + src[fim:]
out, n = re.subn(r'<title>[^<]*</title>', f'<title>{titulo}</title>', out, count=1)
assert n == 1, '<title> não encontrado'

os.makedirs(os.path.dirname(os.path.abspath(saida)), exist_ok=True)
open(saida, 'w', encoding='utf-8').write(out)
print(f'Gerado: {os.path.normpath(saida)}')

# versão para publicar como página do claude.ai: sem <!doctype>/<html>/<head>/<body> (o claude.ai põe os seus)
head = out[out.index('<head>') + 6:out.index('</head>')]
head = re.sub(r'\s*<meta[^>]*>', '', head).strip()
body = out[out.index('<body>') + 6:out.rindex('</body>')].strip()
pub = os.path.join(os.path.dirname(os.path.abspath(saida)), 'publicar-no-claude.html')
open(pub, 'w', encoding='utf-8').write(head + '\n' + body + '\n')
print(f'Gerado: {os.path.normpath(pub)}')
