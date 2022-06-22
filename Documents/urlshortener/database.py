from peewee import *

database = MySQLDatabase(
    'fastapidb', user='root', password='messi',
    host='localhost', port=3306
)

class Url(Model):
    full_url = CharField(max_length=100)
    short_url = CharField(max_length=100)

    def __str__(self):
        return self.url
    
    class Meta:
        database = database
        table_name = 'tier_table2'