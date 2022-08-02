from http.client import UnimplementedFileMode
from sqlalchemy import Table, Column, VARCHAR
from config.db import meta, engine

asistente = Table("tblAsistente", meta,
    Column("asiRUC", VARCHAR(13), primary_key=True),
    Column("asiNombres", VARCHAR(50), nullable=True),
    Column("asiApPaterno", VARCHAR(35), nullable=True),
    Column("asiApMaterno", VARCHAR(35), nullable=False),
    Column("asiGenero", VARCHAR(9), nullable=True),
    Column("asiTelefono", VARCHAR(15), nullable=True),
    Column("asiEmail", VARCHAR(80), nullable=False)
)

meta.create_all(engine)