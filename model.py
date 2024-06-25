from sqlalchemy.orm import declarative_base, sessionmaker

fake = Faker()

# ბაზის მონაცემები
HOST = "localhost"
PORT = 5432
DATABASE = "it_step_new"
USER = "postgres"
PASSWORD = "Dori1313"

engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

Base = declarative_base()




class User(Base):