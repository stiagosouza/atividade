import sqlite3

banco = sqlite3.connect('veiculo.db')
banco.execute("PRAGMA forengn_keys=on") #ativar a veriicação de chaves

# Criando Data Base Veiculo
database = banco.cursor()

database.execute('''
                CREATE TABLE pessoas (
                cpf INTERGER PRIMARY KEY,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                oculos  BOOLEAN NOT NULL);''')
 
database.execute('''CREATE TABLE Marca (
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY (id)
                );''')

database.execute('''CREATE TABLE Veiculo (
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY (placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id)
                );''')


banco.commit()
database.close()
banco.close()