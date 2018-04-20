
import pymysql.cursors
import pymysql

def create_connection():
    return pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='EconomieStat',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def get_tuples(fact, year):
    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            # Create a new record
            query = "select p.nom, e.deficit from EconomieStat as e \
                        inner join Pays as p on e.idPays = p.idPays \
                        inner join Date as d on e.idDate = d.idDate \
                        WHERE d.annee = %s;"
            cursor.execute(query, (year,))
            result = [[row['nom'], row['deficit']] for row in cursor]
            return result

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()
