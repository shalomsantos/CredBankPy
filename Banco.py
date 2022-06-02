
import os
import time
import sqlite3
from os import curdir

class ErroInicializacao(Exception): pass
class ErroCpfExiste(Exception): pass
class ErroCpfInvalido(Exception): pass
class ErroUsuarioExiste(Exception): pass

class ConexaoDB:

	# Construtor
	def __init__(self, filename):

		# Fallback nome padrao caso instanciado sem nome como argumento
		self.dbname = "database.db"
		if (filename != None):
			self.dbname = filename

		banco_existe = os.path.exists(self.dbname)

		# Conecta
		self.conn = sqlite3.connect(self.dbname)
		print("ConexaoDB: conectado com %s" % (self.dbname))

		# Checa se o arquivo fisico do banco existe
		if (banco_existe == False):
			# Senao, recria
			print("Recriando banco de dados...")
			self.__recriar_schema()
		else:
			# Checa se o banco e compativel com a aplicacao
			print("Verificando o banco de dados...")

			try:
				self.__verifica_schema()
			except Exception as e:
				print(f"Erro ao carregar banco de dados: {e}")

	# Destrutor
	def __del__(self):
		try:
			self.conn.close()
			print("ConexaoDB: %s fechado" % (self.dbname))
		except:
			pass

	# Checa se o banco e compativel com a aplicacao
	def __verifica_schema(self):
		cursor = self.conn.execute("SELECT * FROM sqlite_master WHERE type='table';")
		rows = cursor.fetchall()

		if (rows[0][1] != 'credbankpy'):
			raise ErroInicializacao("Banco de dados incompativel com a aplicacao!")	

	# Recria tabelas
	def __recriar_schema(self):
		c = self.conn.cursor()

		try:
			c.execute("BEGIN TRANSACTION;")

			# Habilita suporte a chave estrangeira
			c.execute("PRAGMA foreign_keys = ON;")

			# Identificador do banco
			c.execute("CREATE TABLE credbankpy (versao TEXT);")
			c.execute("INSERT INTO credbankpy VALUES('0.1');")

			# tabela cadastro
			# id (PK)  -> chave primaria identificador do usuario
			# cpf      -> 000.000.000-00 (char[11], unico)
			# nome     -> nome completo
			# datanasc -> data nascimento (string: dd-mm-aaaa)
			# email    -> usuario@email.com
			# telefone -> +55 11 9 9999 9999 (string)
			c.execute('''CREATE TABLE usuarios (
		                  id INTEGER PRIMARY KEY AUTOINCREMENT,
		                  cpf CHAR(11) UNIQUE NOT NULL,
		                  nome TEXT NOT NULL,
		                  datanasc TEXT NOT NULL,
		                  email TEXT NOT NULL,
		                  telefone TEXT);''')

			# tabela logins
			# id_usuario_fk  -> ID mestre do usuario
			# username -> autenticacao usuario
			# password -> senha plaintext
			# status   -> status usuario (ativo, inativo)
			c.execute('''CREATE TABLE logins (
		                  id_login INTEGER PRIMARY KEY AUTOINCREMENT,
		                  id_usuario_fk INTEGER NOT NULL,
		                  username TEXT UNIQUE NOT NULL, 
		                  password TEXT,
		                  status INTEGER,
		                  FOREIGN KEY(id_usuario_fk) REFERENCES usuarios(id));''')

			# tabela conta
			# numconta (PK) -> 00000-0
			# id_usuario_fk -> id usuario dono
			# balanco       -> decimal, balanco parcial da conta
			# timestamp     -> data/hora da ultima atualizacao de balanco (unix time)
			# tipo          -> tipo de conta (ENUM)
			c.execute('''CREATE TABLE contas (
		                  numconta INT PRIMARY KEY,
		                  id_usuario_fk INT,
		                  balanco REAL,
		                  timestamp INT,
		                  tipo INT);''')

			# Tabela transacao
			#  - id_tx (PK)       -> ID da transacao
			#  - tipo_tx          -> Tipo de transacao (ENUM, saque, dep, transf)
			#  - conta_origem_fk  -> num da conta origem
			#  - conta_destino_fk -> num da conta destino
			#  - identificador    -> string que identifica operacao
			#  - timestamp        -> hora da operacao (unix time)
			c.execute('''CREATE TABLE transacoes (
		                  id INT PRIMARY KEY,
		                  tipo_tx INT,
		                  conta_origem_fk INT,
		                  conta_destino_fk INT,
		                  identificador TEXT,
		                  timestamp INT);''')

			c.execute("COMMIT;")

			self.conn.commit()
		except Exception as e:
			c.execute("ROLLBACK;")
			self.conn.commit()
			print(f"Erro ao criar banco de dados: {e}")
			pass

		print("Banco de dados \"%s\" recriado" % (self.dbname))

	# Retorna CPF convertido sem caracteres separadores, None se invalido.
	def __converte_cpf(self, cpf_string):
		# Remove espacos
		cpf = cpf_string.strip()

		# Checa se conversao eh necessaria
		if (len(cpf) == 11 and cpf.isdecimal() == True):
			return cpf

		# Formato precisa ter exatamente 14 chars
		if (len(cpf) != 14):
			return None

		# Separa digitos
		# TODO: check for Nones
		base_dig = cpf.split('-')
		base   = base_dig[0].split('.')
		digito = base_dig[1]

		# Valida estrutura
		if (len(base) != 3):
			return None

		# Valida numeros
		if (len(base[0]) != 3 or base[0].isdecimal() == False):
			return None

		if (len(base[1]) != 3 or base[1].isdecimal() == False):
			return None

		if (len(base[2]) != 3 or base[2].isdecimal() == False):
			return None

		if (len(digito)  != 2 or digito.isdecimal()  == False):
			return None

		return (base[0]+base[1]+base[2]+digito)

	# Retorna ID chave primaria de um fetchall() list
	# [(3,)] -> 3
	def __get_id(self, result):
		if (type(result) is not list):
			return None

		if (len(result) == 0):
			return None

		return result[0][0]

	# Trasforma lista de resultados em lista de dicts
	def __gera_dicts(self, nome_tabela, lista):
		return None

	# Retorna ID dado o CPF do usuario
	def busca_usuario_cpf(self, cpf):
		_cpf = self.__converte_cpf(cpf)

		if (_cpf == None):
			return None

		c = self.conn.execute(f"SELECT id FROM usuarios WHERE cpf = '{_cpf}';")
		rows = c.fetchall()

		return self.__get_id(rows)

	# Retorna um dict com o cadastro do usuario
	# retorna cadastro do usuario a partir do ID do usuario
	def consulta_dados_usuario(self, user_id):
		# Printa os nomes das colunas
		print(self.conn.execute("PRAGMA table_info(usuarios);").fetchall())

#		c = self.conn.execute(f"SELECT c.* FROM usuarios u INNER JOIN cadastro c ON u.id=c.id_fk WHERE id={int(user_id)};")
		c = self.conn.execute(f"SELECT * FROM usuarios WHERE id={int(user_id)};")
		self.conn.commit()
		rows = c.fetchall()

		# Sem resultados
		if (len(rows) == 0):
			return None

		# TODO: retornar dict
		return rows[0]

	# Cria novo cadastro/usuario
	# Em sucesso retorna ID, falha retorna None
	def criar_usuario(self, cpf, nome, datanasc, email, telefone, usuario, senha):
		# Valida/converte entradas
		_cpf = self.__converte_cpf(cpf)

		if (_cpf == None):
			raise ErroCpfInvalido("Formato de CPF invalido")

		# Cria novo cadastro na tabela usuarios
		c = self.conn.cursor()
		user_id  = None
		login_id = None

		# Verifica se ja existe cadastro para CPF
		key = self.__get_id(c.execute(f"SELECT id FROM usuarios WHERE cpf = '{_cpf}';").fetchall())

		if(key != None):
			raise ErroCpfExiste("CPF ja cadastrado na aplicacao")

		# Verifica se username ja existe
		key = self.__get_id(c.execute(f"SELECT id_usuario_fk FROM logins WHERE username = '{usuario}' and status = 1;"))

		if (key != None):
			raise ErroUsuarioExiste("Usuario nao disponivel")

		# Inicia transacao
		try:
			c.execute("BEGIN TRANSACTION;")

			# Insere usuario
			c.execute(f"INSERT INTO usuarios VALUES (NULL, '{_cpf}', '{nome}', '{datanasc}', '{email}', '{telefone}');")

			# Salva o ID da ultima insercao
			user_id = self.__get_id(c.execute("SELECT last_insert_rowid();").fetchall())

			# Insere login, relacionando o ID do usuario
			c.execute(f"INSERT INTO logins VALUES (NULL, '{user_id}', '{usuario}', '{senha}', 1);")

			c.execute("COMMIT;")
			self.conn.commit()

		except:
			c.execute("ROLLBACK;")
			self.conn.commit()
			user_id = None
			pass

		return user_id

	# Retorna ID do usuario caso login/senha estejam corretos
	def valida_login(self, user, passw):
		# TODO: SQL injection possivel aqui :^)
		c = self.conn.execute(f"SELECT id_usuario_fk FROM logins WHERE username = '{user}' AND password = '{passw}';")
		ids = c.fetchall()

		if(len(ids) == 0):
			return None

		return int(ids[0][0])

	# Modifica os dados de autenticacao do usuario
	def altera_login(self, user_id, username, password):
		c = self.conn.cursor()
		try:
			c.execute("BEGIN TRANSACTION;")
			e.execute(f"UPDATE logins SET username='{username}', password='{password}' WHERE id={user_id};")
			c.execute("COMMIT;")
			return True

		except Exception as e:
			c.execute("ROLLBACK;")
			print(f"altera_login erro: {e}")
			pass

		return False

# === TESTE TESTE TESTE ===
#banco = ConexaoDB("test.db")
#
#cadastro_adm = {
#		'cpf'      : '123.456.789-01',
#		'nome'     : 'Admin da Coisa Toda',
#		'datanasc' : '01-01-1970',
#		'email'    : 'admin@credbankpy.com',
#		'telefone' : '+5585987654321',
#		'usuario'  : 'admin',
#		'senha'    : 'password' }
#
#try:
#	# teste com dict
#	a = banco.criar_usuario(**cadastro_adm)
#
#	# teste normal
#	b = banco.criar_usuario(cpf='000.000.000-00', nome='Usuario', datanasc='01-10-1990', email='usuario@gmail.com', telefone='+5585900000001', usuario='user', senha='teste')
#	c = banco.criar_usuario(cpf='11122233344', nome='Usuario2', datanasc='01-10-1992', email='usuari2@gmail.com', telefone='+5585900000002', usuario='user2', senha='teste2')
##	d = banco.criar_usuario(cpf='11122233344', nome='Usuario3', datanasc='01-10-1991', email='usuari3@gmail.com', telefone='+5585900000003', usuario='user3', senha='teste3')
#except Exception as e:
#	print(f"Erro: {e}")
#	pass
#
#print("Busca:", banco.busca_usuario_cpf("111.222.333-44"))
#print("Busca:", banco.busca_usuario_cpf("00000000000"))
#
#print(banco.valida_login('admin', 'password'))
#print(banco.valida_login('user',  'errada'))
#print(banco.valida_login('user',  'teste'))
#
#print(banco.consulta_dados_usuario(1))



