CREATE DATABASE solicitacoes;
\c solicitacoes

CREATE TABLE pedidos (
	id serial not NULL,
	data TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP,
	resposta VARCHAR(250) not NULL
);