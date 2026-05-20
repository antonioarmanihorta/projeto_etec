CREATE SCHEMA jogo_ETEC;
use jogo_ETEC ;
SET FOREIGN_KEY_CHECKS = 1 ;
SET SQL_SAFE_UPDATES = 0 ;
SELECT @@default_storage_engine ;

-- USUÁRIOS E PERFIS
-- Usuario - representa alunos e professores, diferenciados pelo campo tipo
CREATE TABLE usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(60) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    tipo ENUM('aluno', 'professor', 'coordenador') NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    data_criacao TIMESTAMP NOT NULL,
    data_alteracao TIMESTAMP,
    data_exclusao TIMESTAMP NULL
);

-- aluno - tipo de usuário que possui informações proprias
CREATE TABLE aluno (
	id_aluno INT PRIMARY KEY,
    FOREIGN KEY (id_aluno) REFERENCES usuario(id),
    id_turma INT,
    FOREIGN KEY (id_turma) REFERENCES turma(id),
    ra VARCHAR(20) NOT NULL
);

-- professor - tipo de usuário que possui informações proprias
CREATE TABLE professor (
	id_professor INT PRIMARY KEY,
    FOREIGN KEY (id_professor) REFERENCES usuario(id)
);

-- coordenador - tipo de usuário que possui informações proprias
CREATE TABLE coordenador (
	id_coordenador INT PRIMARY KEY,
    FOREIGN KEY (id_coordenador) REFERENCES usuario(id)
);

-- turma - tabela que guardará informaçoes da turma 
CREATE TABLE turma  (
    id INT PRIMARY KEY,
    serie VARCHAR(6),
    turma 	varchar(1),
	qtde_aluno SMALLINT,
    semestre_letivo TINYINT,
    ano_letivo YEAR,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_criacao TIMESTAMP NOT NULL,
    data_alteracao TIMESTAMP,
    data_exclusao TIMESTAMP NULL,
    media_acerto DECIMAL(5, 2),
    media_erro DECIMAL(5, 2),
    total_questao SMALLINT
);

-- CONTEÚDO DO JOGO
-- tema - tabela para poder separar os temas de pergunta, como por exemplo "vidraria"
CREATE TABLE tema (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    qtde_acerto INT,
    qtde_erro INT,
	qtde_resposta INT
);


--  Questao - criada pelo professor, com suporte a imagem e nível de dificuldade e com dois possíveis tipos de perguntas
CREATE TABLE questao (
    id INT PRIMARY KEY,
    id_tema INT,
    enunciado TEXT NOT NULL,
    tipo_questao ENUM('multipla_escolha', 'associacao') NOT NULL,
    nivel_dificuldade TINYINT NOT NULL,
    imagem_url VARCHAR(500) NULL,
    descricao_imagem VARCHAR(255) NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    criado_por INT NOT NULL,
    dt_hora_criacao TIMESTAMP NOT NULL,
    dt_hora_atualizacao TIMESTAMP,
    FOREIGN KEY (criado_por) REFERENCES usuario(id),
    FOREIGN KEY (id_tema) REFERENCES tema(id)
);
ALTER TABLE questao ADD CHECK (nivel_dificuldade BETWEEN 1 AND 3);

-- Alternativa - as opções de resposta, cada uma podendo ter sua própria imagem
CREATE TABLE alternativa (
    id INT PRIMARY KEY,
    id_questao INT NOT NULL,
    texto TEXT NOT NULL,
    imagem_url VARCHAR(500) NULL,
    descricao_imagem VARCHAR(255) NULL,
    is_correta BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (id_questao) REFERENCES questao(id)
);

-- Ajuda - dicas vinculadas a uma questão (eliminar alternativa ou texto explicativo por exemplo)
CREATE TABLE ajuda (
    id INT PRIMARY KEY,
    id_questao INT NOT NULL,
    tipo ENUM('eliminar_alternativa', 'dica_textual') NOT NULL,
    conteudo TEXT NOT NULL,  --  o que vai dentro depende do tipo. Para dica_textual é o texto da dica. Para eliminar_alternativa é o id da alternativa errada que deve ser eliminada da tela.
    FOREIGN KEY (id_questao) REFERENCES questao(id)
);

-- SESSÃO DE JOGO
-- Partida — sessão de jogo de um aluno, com pontuação
CREATE TABLE partida (
    id INT PRIMARY KEY,
    id_usuario INT NOT NULL,
    pontuacao INT NOT NULL DEFAULT 0,
    total_questoes TINYINT   NOT NULL DEFAULT 10,
    condicao ENUM('em_andamento', 'concluida', 'abandonada') NOT NULL DEFAULT 'em_andamento',
    iniciada_em TIMESTAMP NOT NULL,
    finalizada_em TIMESTAMP NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

-- Resposta — cada resposta dada durante uma partida, rastreando acerto e uso de ajuda
CREATE TABLE resposta (
    id INT PRIMARY KEY,
    id_partida INT,
    id_questao INT,
    id_alternativa INT,
    correta BOOLEAN,
    ajuda_usada BOOLEAN,
    tempo_resposta TIMESTAMP,
    FOREIGN KEY (id_partida) REFERENCES partida(id),
    FOREIGN KEY (id_questao) REFERENCES questao(id),
    FOREIGN KEY (id_alternativa) REFERENCES alternativa(id)
);

-- Tarefa - tabela criada para a nossa funcionalidade do jogo de criação de tarefas 
CREATE TABLE tarefa (
    id INT PRIMARY KEY,
    id_professor INT,
    titulo VARCHAR(50),
    descricao TEXT,
    nota_maxima DECIMAL(5, 2),
    limite_tentativas TINYINT,
    tempo_limite SMALLINT,
    data_entrega TIMESTAMP,
    disponibilidade ENUM('ativo', 'inativo'),
    data_criacao TIMESTAMP,
    data_alteracao TIMESTAMP,
    data_exclusao TIMESTAMP,
    FOREIGN KEY (id_professor) REFERENCES professor(id_professor)
);

-- turma_tabela - tabela criada pela cardinalidade do relacionamento entre turma e tarefa 
CREATE TABLE turma_tarefa (
	id_turma INT PRIMARY KEY,
    id_tarefa INT PRIMARY KEY,
    FOREIGN KEY (id_turma) REFERENCES turma(id),
    FOREIGN KEY (id_tarefa) REFERENCES tarefa(id)
);

-- Resposta_tarefa - 
CREATE TABLE resposta_tarefa (
        id INT PRIMARY KEY,
    id_aluno INT NOT NULL,
    id_tarefa INT NOT NULL,
    nota DECIMAL(5,2),
    qtd_acerto TINYINT NOT NULL,
    numero_tentativa TINYINT NOT NULL,
    tempo_total SMALLINT NULL,
    data_envio TIMESTAMP NOT NULL,
    status ENUM('em_andamento', 'enviada', 'corrigida') NOT NULL DEFAULT 'em_andamento',
    FOREIGN KEY (id_aluno)  REFERENCES aluno(id_aluno),
    FOREIGN KEY (id_tarefa) REFERENCES tarefa(id)
);