import pyodbc
import DBUtils
from DBUtils.PersistentDB import PersistentDB
import traceback
import sys
import pandas
import datetime


class DBserver():
    def __init__(self, server = 'databse11.database.windows.net', port = '1433',
                 user = 'fcl', password ='Fucl95117', db = 'database1'):
        persist = PersistentDB(creator=pyodbc,
                               DRIVER="{ODBC Driver 17 for SQL Server}",
                               PORT=port,
                               SERVER=server,
                               DATABASE=db,
                               UID=user,
                               PWD=password)

        self.conn = persist.connection()
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


    def df_baseline(self, username, table_name = "baseline"):
        username = "'"+username+"'"
        sql = "select * from "+table_name+ " where username = "+ username
        val = (username,)
        try:
            df =  pandas.read_sql(sql, self.conn)
            return df
        except:
            print("Exception in user code:")
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)
            return False

    def df_simulation_info(self):
        sql = "select * from simulation_info"

        try:
            df = pandas.read_sql(sql, self.conn)
            return df
        except:
            print("Exception in user code:")
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)
            return False



    def query_baseline2(self, username, table_name = "baseline"):
        # username = "'"+username+"'"
        sql = "select * from "+table_name+ " where username = ? and filename = ?"
        val = (username,'test1')
        try:
            self.cursor.execute(sql,val)
            res = self.cursor.fetchall()
            return res
        except:
            print("Exception in user code:")
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)
            return False




    def insert_baseline(self, filename, username, height, path, table_name="baseline"):
    # id filename username height path
        sql1 = "insert into "+table_name+ "(filename, username, height, path) VALUES (?, ?, ?, ?)"
        value1 = (filename, username, height, path)
        #self.cursor.execute(sql1, value1)

        try:
            self.cursor.execute(sql1, filename, username, height, path)
            self.conn.commit()
            sqlq = "select * from "+table_name + " where filename = ? and username = ?"
            valq = (filename, username)
            self.cursor.execute(sqlq, filename, username)

            return self.cursor.fetchone()[0]     # return bid

        except:
            self.conn.rollback()
            print("Exception in user code:")
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)
            print('The baseline name already exists.')
            return False


    # Insert simulation inforation ,return sid
    def insert_simulation_info(self,fname,  bid, height, ceiling_ht, num_floor, path, note, table_name = "simulation_info"):
        # id name bid height ceiling_ht num_floor simu_time path note
        now = datetime.datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        sql1 = "INSERT INTO " + table_name + " (name, bid, height, ceiling_ht, num_floor, simu_time, path, note) " \
                                             "VALUES (?,?,?,?,?,?,?,?)"
        value1 = (fname, bid, height, ceiling_ht, num_floor, formatted_date, path, note)
        try:
            self.cursor.execute(sql1, value1)
            self.conn.commit()

            # Get the id of the latest row
            self.cursor.execute("SELECT @@Identity")
            row = self.cursor.fetchone()
            sid = row[0]
            return sid
        except:
            self.conn.rollback()
            print("Exception in user code:")
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)
            return False


    def insert_simu_results(self,bid, sid, wwr_ratio, total_time, simu_time, kwh, kwh_per_m2, path,
                  table_name="simu_results"):  # fisrt non-defalut argument, then default argument
        # id bid sid wwr_ratio total_time simu_time kwh kwh_per_m2 path

        sql2 = "INSERT INTO " + table_name + " (bid, sid, wwr_ratio, total_time, simu_time, kwh, kwh_per_m2, path) \
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)"
        value = (bid, sid, wwr_ratio, total_time, simu_time, kwh, kwh_per_m2, path)


        try:
            # 执行sql语句
            self.cursor.execute(sql2, value)
            # 提交到数据库执行
            self.conn.commit()
        except:
            # 如果发生错误则回滚
            self.conn.rollback()
            print("Exception in user code:")
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)







class testDBserver():
    def __init__(self):
        self.db = DBserver()

    def test_query_baseline(self):
        res = self.db.query_baseline2("clong")
        print(res)

    def test_ins_baseline(self):
        res= self.db.insert_baseline('ut1_proportional', 'clong', 22.5, 'D:\\ide_mine\\changing\\ut1.idm')
        print(res)

    # test insert_simulation_info
    def testInsertSimulation_info(self):
        #  fname,  bid, height, ceiling_ht, num_floor, path, note
        res = self.db.insert_simulation_info('ut1_proportional',7, 22.5, 3, 5, 'D:\\ide_mine\\changing\\ut1_5floor.idm', 'ut1_5floor')
        print(res)

    def testInsertSimuResults(self):
        # bid, sid, wwr_ratio, total_time, simu_time, kwh, kwh_per_m2, path
        self.db.insert_simu_results(7, 5, 0.1,  167.98, 146.656, 676013, 192.6,
                                           'D:\\ide_mine\\changing\\ut2pro\\ut2proportional_wwr0.1_5floor.html')

        self.db.insert_simu_results(7, 5, 0.2, 173.468, 151.126, 694991, 198,
                                        'D:\\ide_mine\\changing\\ut2pro\\ut2proportional_wwr0.2_5floor.html')
        self.db.insert_simu_results(7, 5, 0.2, 173.468, 151.126, 694991, 198,
                                        'D:\\ide_mine\\changing\\ut2pro\\ut2proportional_wwr0.2_5floor.html')
        self.db.insert_simu_results(7, 5, 0.25, 175.048, 152.507, 706990, 201.4, 'D:\\ide_mine\\changing\\ut2pro\\ut2proportional_wwr0.25_5floor.html')
        self.db.insert_simu_results(7, 5, 0.3, 172.097, 149.659, 719834, 205.1, 'D:\\ide_mine\\changing\\ut2pro\\ut2proportional_wwr0.3_5floor.html')
        self.db.insert_simu_results(7, 5, 0.35, 182.947, 160.413, 734364, 209.2, 'D:\\ide_mine\\changing\\ut2pro\\ut2proportional_wwr0.35_5floor.html')
        self.db.insert_simu_results(7, 5, 0.4, 183.62, 160.134, 749509, 213.5, 'D:\\ide_mine\\changing\\ut2pro\\ut2proportional_wwr0.4_5floor.html')
        self.db.insert_simu_results(7, 5, 0.45, 183.566, 159.298, 764700, 217.9, 'D:\\ide_mine\\changing\\ut2pro\\ut2proportional_wwr0.45_5floor.html')
        self.db.insert_simu_results(7, 5, 0.47, 182.468, 159.625, 770951, 219.6, 'D:\\ide_mine\\changing\\ut2pro\\ut2proportional_wwr0.47_5floor.html')

    def testDf_simulation_info(self):
        res = self.db.df_simulation_info()
        print(res)



if __name__ == '__main__':
    test = testDBserver()
    # test.test_ins_baseline()
    # test.test_query_baseline()
    # test.testInsertSimulation_info()
    test.testInsertSimuResults()
    # test.testDf_simulation_info()