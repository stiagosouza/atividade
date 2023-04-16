import sqlite3
from base import Marca

banco = sqlite3.connect('veiculo.db')
banco.execute("PRAGMA forengn_keys=on") 
database = banco.cursor()

#Criando lista de objetos Marca
insertMarca = '''INSERT INTO Marca (nome, sigla) VALUES (:nome,:sigla);'''
mercedesB = Marca ("Mercedes Bens","MB")
database.execute(insertMarca, vars(mercedesB))
mercedesB.id= database.lastrowid

ford = Marca ("Ford ","FD")
database.execute(insertMarca, vars(ford))
ford.id= database.lastrowid



banco.commit()
database.close()
banco.close()