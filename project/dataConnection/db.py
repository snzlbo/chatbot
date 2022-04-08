import psycopg2

con = psycopg2.connect(
    host = 'fate',
    database = 'chatbot'

)

con.close()