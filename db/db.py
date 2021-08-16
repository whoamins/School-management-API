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
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.String),
    sqlalchemy.Column("group", sqlalchemy.String)
)

metadata.create_all(engine)
