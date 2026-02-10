import pymysql

# 1. On simule MySQLdb
pymysql.install_as_MySQLdb()

# 2. On force la version pour tromper le test de Django
pymysql.version_info = (2, 2, 7, "final", 0)