from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://jhorsax:10287@localhost:3306/dbEssalud")

meta = MetaData()

conn = engine.connect()