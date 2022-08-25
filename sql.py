import psycopg2 
connection =  psycopg2.connect(
    host = 'localhost',
    port = '1234',
    database = 'postgres', 
    user = 'postgres',
    password = '123'
)
print(f'Вы подключились к базе данных как полбзователь ')
cursor = connection.cursor()
cursor.execute("SELECT * FROM products")
connection.commit()
print('Добро пожаловать мир технологий')
print("Список всех наших товаров")
products = cursor.fetchall()
for i in products:
    print(i[0],i[1],i[2],i[3],i[4])
id = input('Что вы хотите купить ')
cursor.execute(f"SELECT * FROM products WHERE productname = '{id}';")
print(cursor.fetchall())

print("проэкт завершен")