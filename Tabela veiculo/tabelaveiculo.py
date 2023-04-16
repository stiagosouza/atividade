import sqlite3
from base import Veiculo
from tabelaMarca import mercedesB,ford,chevrolet
banco = sqlite3.connect('veiculo.db')
banco.execute("PRAGMA forengn_keys=on") 
database = banco.cursor()

#Criando lista de objetos Veiculo
insertVeiculo = '''INSERT INTO Veiculo (placa, ano, cor, motor, proprietario, marca) VALUES
            (:placa, :ano, :cor, :motor, :proprietario, :marca);'''
veiculo1 = Veiculo("FOZ-4190","2001", "Prata", 1.0, 12345678900, mercedesB.id)
veiculo2 = Veiculo("HOP-7238","2002", "Preto", 1.4, 97716012371, ford.id)
veiculo3 = Veiculo("HYD-4652","2022", "Branco", 2.0, 22350270327, ford.id)
veiculo4 = Veiculo("HVF-9165","2019", "Azul", 2.0, 25983324314, mercedesB.id)

database.execute(insertVeiculo, vars(veiculo1))
database.execute(insertVeiculo, vars(veiculo2))
database.execute(insertVeiculo, vars(veiculo3))
database.execute(insertVeiculo, vars(veiculo4))
