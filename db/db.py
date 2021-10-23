import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./schoolapi.db"
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


metadata = sqlalchemy.MetaData()

students = sqlalchemy.Table(
    "students",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("age", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("group", sqlalchemy.String, nullable=False)
)

teachers = sqlalchemy.Table(
    "teachers",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER, primary_key=True),
    sqlalchemy.Column("age", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("subject", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("experience", sqlalchemy.INTEGER, nullable=False),
    sqlalchemy.Column("degree", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("salary", sqlalchemy.INTEGER, nullable=False),
)

metadata.create_all(engine)
