# Pesquisa de Design

## Contextualização

É cada vez mais frequente ver as empresas **aproximando produtos e serviços de seus clientes**, com o auxílio da tecnologia e ferramentas de processos criativos, como o método **Design Centrado no Usuário** (processo de design que tem como foco o usuário e a solução de suas necessidades). As instituições já entenderam que somente dessa forma irão garantir uma melhor experiência para seus usuários. Dessa forma, a **pesquisa de Design é necessária para um projeto**, pois **oferece uma base compartilhada para a tomada de decisões**, fundamentada em evidências, e não suposições sobre determinado assunto. Nesse contexto foi desenvolvida uma **aplicação que auxilia na captura de opiniões dos usuários e as amazena em um banco de dados, permitindo consulta posterior**.

###### Containers necessários

<img width="555" alt="Prancheta 1@2x" src="https://user-images.githubusercontent.com/65691783/85179814-3d16ec00-b258-11ea-9ce5-601629770efb.png">

• *Nginx* é um servidor web de alta performance que entrega o conteúdo estático de um site de forma rápida e fácil de configurar. Oferece recursos de balanceamento de cargas, proxy reverso e streaming, além de gerenciar milhares de conexões simultâneas. O resultado disso é maior velocidade e escalabilidade.

• *Python* é uma linguagem de programação de alto nível. Estruturas desse tipo são, geralmente, classificadas como orientadas a objetos. A orientação a objetos é uma forma de programação que busca o controle e a estabilidade de projetos de grandes proporções.

• *PostgreSQL* é um sistema de banco de dados em código aberto para Windows, Mac e Linux. Ele possui mais de 15 anos de desenvolvimento ativo e uma arquitetura que ganhou uma forte reputação devido a sua estabilidade e integridade de dados.

## Instruções para instalação:

###### 1. Fazer um diretório local chamado *"trabalho_final"*

###### 2. Acessar diretório correspondente
```
cd trabalho_final/
```

###### 3. Criar diretórios da estrutura conforme os comandos abaixo:
```
mkdir app
```
e
```
mkdir nginx
```
e
```
mkdir scripts
```
e
```
mkdir web
```

###### 4. Fazer download do arquivo *"docker-compose"* e inserí-lo dentro da raiz do diretório do projeto, chamado *"trabalho_final"*:


###### 5. Listar diretórios existentes dentro de *"trabalho_final"* e verificar se há "app", "nginx", "scripts", "web" e "docker-compose" com o comando abaixo:
```
ls
```

###### 6. Fazer download dos arquivos *"app.sh"* e *"envia.py"* e inserí-los dentro do diretório chamado *"app"*.

###### 7. Fazer download do arquivo *"default.conf"* e inserí-lo dentro do diretório chamado *"nginx"*.

###### 8. Fazer download dos arquivos *"check.sql"* e *"init.sql"* e inserí-los dentro do diretório chamado *"scripts"*.

###### 9. Fazer download do arquivo *"index.html"* e inserí-lo dentro do diretório chamado *"web"*.

###### 10. Verificar se não há nada rodando do arquivo *"docker-compose"* utilizando o comando abaixo:
```
docker-compose ps 
```
ou
```
docker-compose ps -a
```

###### 11. Se estiver algum componente ativo executar o comando abaixo para desativá-los:
```
docker-compose down
```

###### 12. Ativar o arquivo *"docker-compose"*, deixando-o em background utilizando o comando abaixo:
```
docker-compose up -d
```

###### 13. Executar o comando abaixo para verificar se os serviços estão ativos, identificados pelo status "up" conforme mostra a imagem logo a seguir:
```
docker-compose ps
```
![Captura de Tela (166)](https://user-images.githubusercontent.com/65691783/85180420-d561a080-b259-11ea-97b6-d696ae6c9780.png)

###### 14. Acessar o navegador web e verificar se a aplicação está no *"localhost"*, conforme mostra a imagem abaixo:

![Captura de Tela (167)](https://user-images.githubusercontent.com/65691783/85180617-3f7a4580-b25a-11ea-9ee9-9e78a1ff4442.png)

###### 15. Acessar o navegador web e fazer uma teste de formulário, preenchendo os campos e acionando o botão *"Enviar"*, verificando se a resposta preenchidas aparece na própria página do navegador, conforme mostra a imagem abaixo:

![Captura de Tela (168)](https://user-images.githubusercontent.com/65691783/85180793-b7e10680-b25a-11ea-8e6c-935eb8884926.png)

###### 16. Para verificar se todos os logs do banco de dados estão sendo registrados utilizando o comando abaixo:
```
docker-compose logs -f -t
```

###### 17. Para verificar se as informações inseridas na página web estão registradas na base de dados utilizando o comando abaixo, conforme indica a imagem ilustrativa logo a seguir.
```
docker-compose exec db psql -U postgres -d solicitacoes -c 'select * from pedidos'
```
![Captura de Tela (169)](https://user-images.githubusercontent.com/65691783/85181133-92083180-b25b-11ea-8430-e75bf42803b0.png)
