import oracledb as ora

## db 접속정보(민감)
def connections():
    conn = ora.connect(user="ora_user",password="1111",
                       dsn="localhost:1521/xe")
    return conn
