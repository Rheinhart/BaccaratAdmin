#coding:utf8
"""
@__author__ = 'Thomas'
"""
from BaccaratAdmin.tools.fireflymem.dbpool import dbpool
from BaccaratAdmin.tools.fireflymem.memclient import mclient
from BaccaratAdmin.tools.fireflymem.mmode import MAdmin
from BaccaratAdmin.tools.fireflymem.madminanager import MAdminManager
from BaccaratAdmin.settings import CACHES,DATABASES

class Memmode_Operation:


    def __init__(self):

        self.address = [CACHES['default'].get('LOCATION')]
        self.hostname = [DATABASES['default'].get('HOST')][0]
        mclient.connect(self.address, self.hostname)
        self.user = [DATABASES['default'].get('USER')][0]
        self.password = [DATABASES['default'].get('PASSWORD')][0]
        self.port = int([DATABASES['default'].get('PORT')][0])
        self.dbname = [DATABASES['default'].get('NAME')][0]
        self.charset = "utf8"
        dbpool.initPool(host = self.hostname, user = self.user, passwd = self.password,
                    port = self.port, db = self.dbname, charset = self.charset)


        self.tb_video_admin = MAdmin('t_video', 'videoid', fk="flag")
        MAdminManager().registe(self.tb_video_admin)
        self.tb_table_admin = MAdmin('t_table', 'tableid', fk='videoid')
        MAdminManager().registe(self.tb_table_admin)

    def updateVideoMemToDb(self):
        """Sync Viedeoinfo from Memcache into database!
        """
        obj = self.tb_video_admin.getAllPkByFk(0)
        for id in obj:
            print self.tb_video_admin.getObjData(id)
        obj = self.tb_video_admin.getAllPkByFk(1)
        for id in obj:
            print self.tb_video_admin.getObjData(id)
        self.tb_video_admin.checkAll()
        #MAdminManager().checkAdmins()

    def changeVideotoMem(self,mdata):

        mmode = self.tb_video_admin.getObj(mdata['videoid'])
        if mmode:
            mmode.update_multi(mdata)

    def updateVideoDbtoMem(self):

        self.tb_video_admin.insert()
        MAdminManager().registe(self.tb_video_admin)

    def updateTableMemToDb(self):
        """Sync Tableinfo from Memcache into database!
        """
        self.tb_table_admin.insert()
        obj = self.tb_table_admin.getAllPkByFk(0)
        self.tb_table_admin.checkAll()
        print obj
        for id in obj:
            print self.tb_table_admin.getObjData(id)