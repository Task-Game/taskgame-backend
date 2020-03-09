create database taskGame;
use taskGame;

-- CREATE TABLE Frequencia(
--   idFrequencia INTEGER NOT NULL AUTO_INCREMENT,
--   descricao INTEGER,
--   PRIMARY KEY(idFrequencia)
-- );

-- CREATE TABLE Itens(
--   idItem INTEGER NOT NULL AUTO_INCREMENT,
--   Loja_idLoja INTEGER NOT NULL
--   nome VARCHAR(50),
--   descricao VARCHAR(50),
--   valor INTEGER,
--   PRIMARY KEY(idItens),
--   FOREIGN KEY (Loja_idLoja) REFERENCES Loja(idLoja)
-- );

-- CREATE TABLE Metas(
--   idMetas INTEGER NOT NULL AUTO_INCREMENT,
--   Tarefa_idTarefa INTEGER NOT NULL,
--   Descricao VARCHAR(50),
--   Feito TINYINT,
--   PRIMARY KEY(idMetas),
--   FOREIGN KEY (Tarefa_idTarefa) REFERENCES Tarefa(idTarefa)
-- );

CREATE TABLE Raridade(
  idRaridade INTEGER NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(15),
  recompensa INTEGER,
  PRIMARY KEY(idRaridade)
);

CREATE TABLE TipoUsuario(
  idTipoUsuario INTEGER NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(15),
  PRIMARY KEY(idTipoUsuario)
);

CREATE TABLE Loja(
  idLoja INTEGER NOT NULL AUTO_INCREMENT,
  dataAbertura DATETIME,
  dataFechamento DATETIME,
  PRIMARY KEY(idLoja)
);

CREATE TABLE Tarefa(
  idTarefa INTEGER NOT NULL AUTO_INCREMENT,
  Projeto_idProjeto INTEGER NOT NULL,
  Raridade_idRaridade INTEGER NOT NULL,
  Frequencia_idFrequencia INTEGER NOT NULL,
  nome VARCHAR(25),
  descricao VARCHAR(100),
  prazo DATE,
  alarme DATETIME,
  recompensa INTEGER,
  Feito TINYINT,
  PRIMARY KEY(idTarefas), 
  FOREIGN KEY (Projeto_idProjeto) REFERENCES Projeto(idProjeto),
  FOREIGN KEY (Raridade_idRaridade) REFERENCES Raridade(idRaridade),
  FOREIGN KEY (Frequencia_idFrequencia) REFERENCES Frequencia(idFrequencia)
);

CREATE TABLE Projeto(
  idProjeto INTEGER NOT NULL AUTO_INCREMENT,
  Loja_idLoja INTEGER NOT NULL,
  titulo VARCHAR(25),
  acesso VARCHAR(8),
  descricao VARCHAR(100),
  prazo DATE,
  PRIMARY KEY(idProjeto),
  FOREIGN KEY (Loja_idLoja) REFERENCES Loja(idLoja)
);

CREATE TABLE Usuario(
  idUsuario INTEGER NOT NULL AUTO_INCREMENT,
  TipoUsuario_idTipoUsuario INTEGER NOT NULL,
  nome VARCHAR(100),
  email VARCHAR(60),
  dataNascimento DATE,
  senha VARCHAR(255),
  pontos INTEGER,
  PRIMARY KEY(idUsuario),
  FOREIGN KEY (TipoUsuario_idTipoUsuario) REFERENCES TipoUsuario(idTipoUsuario)
);

CREATE TABLE Usuario_Projeto(
  idUsuarioProjeto INTEGER NOT NULL,
  Usuario_idUsuario INTEGER NOT NULL,
  Projeto_idProjeto INTEGER NOT NULL,
  PRIMARY KEY(idUsuarioProjeto),
  FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuario(idUsuario),
  FOREIGN KEY (Projeto_idProjeto) REFERENCES Projeto(idProjeto)

);

CREATE TABLE Usuario_Tarefas(
  idUsuarioTarefa INTEGER NOT NULL,
  Usuario_idUsuario INTEGER NOT NULL,
  Tarefas_idTarefas INTEGER NOT NULL,
  PRIMARY KEY(idUsuarioTarefa),
  FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuario(idUsuario),
  FOREIGN KEY (Tarefas_idTarefas) REFERENCES Tarefas(idTarefas)
);

