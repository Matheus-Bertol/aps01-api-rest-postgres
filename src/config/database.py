from contextlib import contextmanager
from sqlmodel import SQLModel, Session, create_engine


# sqlite_filename = "database.db"
# connect_args = {"check_same_thread": False}
# db_url = f"sqlite:///{sqlite_filename}"

PG_USERNAME = "root"
PG_PASSWORD = "postgres"
PG_HOST = "localhost"
PG_PORT = 5432
PG_DATABASE = "oficina"

connect_args = {}
db_url = f"postgresql://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"


engine = create_engine(db_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_engine():
    return engine

@contextmanager
def get_session():
    yield Session(engine)