from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:1316@localhost:3306/cinema')

conn = engine.connect()
response = conn.execute('SELECT * FROM filmes;')

for row in response:
    print(row)