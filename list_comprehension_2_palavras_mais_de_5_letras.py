"""
Dada uma lista de palavras, crie uma nova lista que contenha apenas as palavras
que têm mais de 5 letras e, ao mesmo tempo, estejam em letras maiúsculas.

palavras = ["Python", "programacao", "Geek", "Universidade", "codigo", "Lista",
 "comprehension"]

Dica: Você pode usar o método upper() para converter uma palavra para maiúsculas e a
função len() para verificar o comprimento da palavra.

Experimente resolver e, se precisar de ajuda, estarei por aqui!
"""

palavras = ["Python", "programacao", "Geek", "Universidade", "codigo", "Lista",
 "comprehension"]

letras = [pal.upper() for pal in palavras if len(pal) > 5 ]

print(letras)