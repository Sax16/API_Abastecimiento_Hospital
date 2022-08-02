from http.client import UnimplementedFileMode
from sqlalchemy import Table, Column, VARCHAR
from config.db import meta, engine

asistentes = Table("tblAsistente", meta,
    Column("asiRUC", VARCHAR(13), primary_key=True),
    Column("asiNombres", VARCHAR(50), nullable=False),
    Column("asiApPaterno", VARCHAR(35), nullable=False),
    Column("asiApMaterno", VARCHAR(35), nullable=False),
    Column("asiGenero", VARCHAR(9), nullable=False),
    Column("asiTelefono", VARCHAR(15), nullable=False),
    Column("asiEmail", VARCHAR(80), nullable=True)
)

meta.create_all(engine)