import re

valor = "8714-5814 dsa"

contatos = re.match("(\+?\d\d)?\s?(\d\d)?\s?(\d?\s?[0-9]{4}-?[0-9]{4})", valor)
print(contatos.group())