import peewee as pw

db = pw.MySQLDatabase(
    "mysql1",
    user="mysql1",
    password="Password123",
    host="localhost",
    port=3306
)

class BaseModel(pw.Model):
    class Meta:
        database = db

class Person(BaseModel):
    name = pw.CharField(max_length=50)
    age = pw.IntegerField()


class PizzaOrder(BaseModel):
    description = pw.CharField(max_length=500)
    price = pw.IntegerField()
