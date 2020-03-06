create database taskGame;
use taskGame;

CREATE TABLE Frequencia(
  idFrequencia INTEGER NOT NULL AUTO_INCREMENT,
  descricao INTEGER,
  PRIMARY KEY(idFrequencia)
);

CREATE TABLE Itens(
  idItens INTEGER NOT NULL AUTO_INCREMENT,
  nome VARCHAR(50),
  descricao VARCHAR(50),
  valor INTEGER,
  PRIMARY KEY(idItens)
);

CREATE TABLE Metas(
  idMetas INTEGER NOT NULL AUTO_INCREMENT,
  Descricao VARCHAR(50),
  Feito BOOL,
  PRIMARY KEY(idMetas)
);

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
  Itens_idItens INTEGER NOT NULL,
  titulo VARCHAR(25),
  dataAbertura DATETIME,
  dataFechamento DATETIME,
  PRIMARY KEY(idLoja),
  FOREIGN KEY (Itens_idItens) REFERENCES Itens(idItens)
);

CREATE TABLE Tarefas(
  idTarefas INTEGER NOT NULL AUTO_INCREMENT,
  Metas_idMetas INTEGER NOT NULL,
  Raridade_idRaridade INTEGER NOT NULL,
  Frequencia_idFrequencia INTEGER NOT NULL,
  nome VARCHAR(25),
  descricao VARCHAR(100),
  prazo DATE,
  alarme DATETIME,
  PRIMARY KEY(idTarefas), 
  FOREIGN KEY (metas_idMetas) REFERENCES Metas(idMetas),
  FOREIGN KEY (Raridade_idRaridade) REFERENCES Raridade(idRaridade),
  FOREIGN KEY (Frequencia_idFrequencia) REFERENCES Frequencia(idFrequencia)
);

CREATE TABLE Projetos(
  idProjeto INTEGER NOT NULL AUTO_INCREMENT,
  Terefas_idTarefa INTEGER NOT NULL,
  Loja_idLoja INTEGER NOT NULL,
  titulo VARCHAR(25),
  acesso VARCHAR(8),
  descricao VARCHAR(100),
  prazo DATE,
  PRIMARY KEY(idProjeto),
  FOREIGN KEY (Terefas_idTarefa) REFERENCES Tarefas(idTarefas),
  FOREIGN KEY (Loja_idLoja) REFERENCES Loja(idLoja)
);

CREATE TABLE Usuarios(
  idUsuario INTEGER NOT NULL AUTO_INCREMENT,
  TipoUsuario_idTipoUsuario INTEGER NOT NULL,
  nome VARCHAR(100),
  email VARCHAR(60),
  dataNascimento DATE,
  senha VARCHAR(16),
  pontos INTEGER,
  PRIMARY KEY(idUsuario),
  FOREIGN KEY (TipoUsuario_idTipoUsuario) REFERENCES TipoUsuario(idTipoUsuario)
);

CREATE TABLE Usuario_Projeto(
  idUsuarioProjeto INTEGER NOT NULL,
  Usuario_idUsuario INTEGER NOT NULL,
  Projeto_idProjeto INTEGER NOT NULL,
  PRIMARY KEY(idUsuarioProjeto),
  FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuarios(idUsuario),
  FOREIGN KEY (Projeto_idProjeto) REFERENCES Projetos(idProjeto)

);

CREATE TABLE Usuario_Tarefas(
  idUsuarioTarefa INTEGER NOT NULL,
  Usuario_idUsuario INTEGER NOT NULL,
  Tarefas_idTarefas INTEGER NOT NULL,
  PRIMARY KEY(idUsuarioTarefa),
  FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuarios(idUsuario),
  FOREIGN KEY (Tarefas_idTarefas) REFERENCES Tarefas(idTarefas)
);

