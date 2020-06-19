import psycopg2
import redis
import json
import os
from bottle import Bottle, request

class Envia(Bottle):
	def __init__(self):
		super().__init__()
		self.route('/', method='POST', callback=self.send)
		
#		redis_host = os.getenv('REDIS_HOST', 'fila')
#		self.fila = redis.StrictRedis(host=redis_host, port=6379, db=0)
		#self.fila = redis.StrictRedis(host='fila', port=6379, db=0)
		
		db_name = os.getenv('DB_NAME', 'fake')
		db_user = os.getenv('DB_USER', 'postgres')
		db_host = os.getenv('DB_HOST', 'db')
		dsn = f'dbname={db_name} user={db_user} host={db_host}'
		self.connecta = psycopg2.connect(dsn)
		#DSN = 'dbname=solicitacoes user=postgres host=db'
		#self.connecta = psycopg2.connect(DSN)
    
	def registro_pedido(self, resposta):
		SQL = 'INSERT INTO pedidos (resposta) VALUES (%s)'
		cursosql = self.connecta.cursor()
		cursosql.execute(SQL, (resposta, ))
		self.connecta.commit()
		cursosql.close()
		
		msg = {'resposta': resposta}
#		self.fila.rpush('envia', json.dumps(msg))   
		
		print('Mensagem registrada!')
		
	#@route('/', method='POST')
	def send (self):
		resposta = request.forms.get('resposta')
		if not resposta:
			return "resposta não encontrada"
		self.registro_pedido(resposta)
		return 'Mensagem enviada: Resposta: {}'.format(
			resposta
		)

if __name__ == '__main__':
	envia = Envia()
	envia.run(host='0.0.0.0', port=8080, debug=True)