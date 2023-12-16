endereco = "Rua são marcelo 5000, casa 4, Morro são bento, Santos, SP, 11081-110"

import re # Regular Expression -- RegEx


padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") # para opcional usar ? ou {0,1}. também posso usar {a-z}
busca = padrao.search(endereco) # Match ou None, Match pode retornar o indice de onde a string foi encontrada.

if busca:
    cep = busca.group()
    print(cep)

