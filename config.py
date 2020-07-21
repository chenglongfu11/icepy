#Configuration file
"""
    TO RUN : add your own IDA ICE application path, building path and mysql host
"""




class ICE(object):
  ice_path = "D:\\idaice\\bin\\"
  building_path = None

  # Mysql config info
  MYSQL_HOST = 'localhost'
  MYSQL_DBNAME = 'wwr'
  MYSQL_USER = 'root'
  MYSQL_PASSWD = 'password'

  MYSQL_PORT = 3306

  @classmethod  # 不需要实例化
  def setice(cls, ice_path):
    if cls.ice_path == ice_path:
        pass
    else:
        cls.ice_path = ice_path

  @classmethod
  def setfile(cls, building_path):
  # BUILDING_PATH = "d:\\ide_mine\\changing\\ut1_7floorwithWin.idm"
    if cls.building_path == None:
      cls.building_path = building_path
    elif cls.ice_path == building_path:
      pass

  @classmethod
  def setmysql(cls, host, port, dbname, user, password):
      cls.MYSQL_HOST = host
      cls.MYSQL_PORT = port
      cls.MYSQL_DBNAME = dbname
      cls.MYSQL_USER = user
      cls.MYSQL_PASSWD = password



# APP_PATH = "D:\\idaice\\bin\\"
# #
# #
# BUILDING_PATH = "d:\\ide_mine\\changing\\ut1_7floorwithWin.idm"
# BUILDING_PATH = [b"d:\\ide_mine\\changing\\ut1.idm", b"d:\\ide_mine\\changing\\ut1_7floor.idm", b"d:\\ide_mine\\changing\\ut1_7floorwithWin.idm"]


#Mysql config info
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'testdb'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'password'

MYSQL_PORT = 3306