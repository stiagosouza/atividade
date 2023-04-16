import sqlite3
from base import pessoa

banco = sqlite3.connect('veiculo.db')
banco.execute("PRAGMA forengn_keys=on") 
database = banco.cursor()

# Criando lista de objetos Pessoa
Insert = '''INSERT INTO pessoas (cpf, nome, nascimento, oculos) VALUES (:cpf,:nome,:nascimento,:usa_oculos);'''
pessoa1 = pessoa(97716012371, 'Carlos', '1990-05-25', False)
pessoa2 = pessoa(18465243344, 'Marcelo', '1989-01-20', True)
pessoa3 = pessoa(60242054307, 'Matheus', '1995-08-15', True)
pessoa4 = pessoa(37142193310, 'Layla', '1975-11-10', False)
pessoa5 = pessoa(22350270327, 'Debora', '2000-10-21', True)
pessoa6 = pessoa(62173706381, 'Tiago', '1998-07-77', False)
pessoa7 = pessoa(25983324314, 'Lucas', '1988-08-23', True)
pessoa8 = pessoa(49117727359, 'Christopher', '1978-06-28', True)

database.execute(Insert, vars(pessoa1))
database.execute(Insert, vars(pessoa2))
database.execute(Insert, vars(pessoa3))
database.execute(Insert, vars(pessoa4))
database.execute(Insert, vars(pessoa5))
database.execute(Insert, vars(pessoa6))
database.execute(Insert, vars(pessoa7))
database.execute(Insert, vars(pessoa8))


banco.commit()
database.close()
banco.close()