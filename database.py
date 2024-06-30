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

def getAllJobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        return result.all()
        

def loadJob(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), parameters=dict(val=id))
        row = result.all()

        if len(row) > 0:
            print("IT's entered while the fuckn length is : ", len(row))
            return row[0]
        else:
            return None
        
def addJob(id,job,location,salary):
    with engine.connect() as conn:

        query = text("INSERT INTO jobs VALUES(:Id,:Job,:Location,:Salary)")
        conn.execute(query, parameters=dict(Id=id, Job=job, Location=location, Salary=salary))
        conn.commit()
              
        


