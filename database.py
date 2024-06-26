from sqlalchemy import create_engine, text
from sqlalchemy import URL

url_object = URL.create(
    "mysql", #+pymysql
    username="root",
    host="localhost",
    database="my-training",
)

print(url_object)
engine = create_engine(url_object)
with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())


