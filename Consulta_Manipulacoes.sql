-- SQLite

-- SELECT *FROM Marca,pessoas,Veiculo; -- Sleciona tudo da tabela marca, pessoas e Veiculo

-- DELETE FROM Marca WHERE nome = 'Mercedes Bens'; -- Deleta da tabela Marca, apenas as colunas tem a palavra informada 
-- ALTER TABLE veiculo ADD motor REAL; -- Insere uma coluna  na tabela
-- DROP DATABASE veiculo; -- Exclui toda a base de dados sem a possibilidade de reverção
-- UPDATE pessoas SET oculos = False WHERE cpf = 62173706381; --Alterar a informa da tabela desejada por outra
--delete from pessoas WHERE oculos = 1; -- Deleta uma linha da tabela no qual contem o Id informado
--DROP TABLE Marca;-- Deleta uma linha da tabela no qual contem o Id informado
-- SELECT Veiculo.placa,Veiculo.ano,Veiculo.cor,Veiculo.motor,Veiculo.proprietario,Marca.nome FROM Veiculo
-- JOIN Marca ON Marca.id = Veiculo.marca; --Selecionar as informaçoes da tabela veiculos, onde terar relacionamento com a tabela marca