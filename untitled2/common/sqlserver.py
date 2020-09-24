# coding:utf-8

import pymssql
from config import redcfg


class MSSQL():
    def __init__(self, host, user, pwd, db):

        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db


    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def Selsql(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def Exesql(self, sql):
        cur = self.__GetConnect()
        try:
            # 执行sql语句
            cur.execute(sql)
            # 提交到数据库
            self.conn.commit()
        except:
            # 发生错误时回滚
            self.conn.rollback()
            # 关闭数据库连接
            self.conn.close()

    def Ms(self):
        db_host = redcfg.host
        db_user = redcfg.user
        db_pwd = redcfg.pwd
        db_db = redcfg.db
        ms = MSSQL(host=db_host, user=db_user, pwd=db_pwd, db=db_db)
        return ms

#if __name__ == '__main__':


    #ms = MSSQL(host="localhost", user="sa", pwd="xqx1234", db="test_fdczzxt")
    # reslist = ms.Selsql("select * from info")
    # for i in reslist:
    #     print("name=",i[1])
    #
    # newsql = "update webuser set name='%s' where id=1" % u'测试'
    # print(newsql)
    # ms.Exesql(newsql.encode('utf-8'))
