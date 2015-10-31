#coding:utf8
"""
@__author__ = 'Thomas'
"""
from BaccaratAdmin.tools.fireflymem.dbpool import dbpool
from BaccaratAdmin.tools.fireflymem.memclient import mclient
from BaccaratAdmin.tools.fireflymem.mmode import MAdmin
from BaccaratAdmin.tools.fireflymem.madminanager import MAdminManager
from BaccaratAdmin.settings import CACHES

address = [CACHES['default'].get('LOCATION')]
hostname = 'localhost'
mclient.connect(address, hostname)
user = 'root'
password = '123456'
port = 3306
dbname = 'bjl'
charset = "utf8"
dbpool.initPool(host = hostname, user = user, passwd = password,
                    port = port, db = dbname, charset = charset)

def updateVideoMemToDb():
    """Sync Viedeoinfo from Memcache into database!
    """
    tb_video_admin = MAdmin('t_video', 'videoid', fk="flag")
    obj = tb_video_admin.getAllPkByFk(0)
    for id in obj:
        print tb_video_admin.getObjData(id)
    obj = tb_video_admin.getAllPkByFk(1)
    for id in obj:
        print tb_video_admin.getObjData(id)
    tb_video_admin.checkAll()
    #MAdminManager().checkAdmins()

def changeVideotoMem(mdata):
    tb_video_admin = MAdmin('t_video', 'videoid', fk='flag')
    MAdminManager().registe(tb_video_admin)
    mmode = tb_video_admin.getObj(mdata['videoid'])
    if mmode:
        mmode.update_multi(mdata)

def updateVideoDbtoMem():
    tb_video_admin = MAdmin('t_video', 'videoid', fk="flag")
    tb_video_admin.insert()
    MAdminManager().registe(tb_video_admin)

def updateTableMemToDb():
    """Sync Tableinfo from Memcache into database!
    """
    tb_table_admin = MAdmin('t_table', 'tableid', fk='videoid')
    tb_table_admin.insert()
    MAdminManager().registe(tb_table_admin)
    obj = tb_table_admin.getAllPkByFk(0)
    tb_table_admin.checkAll()
    print obj
    for id in obj:
        print tb_table_admin.getObjData(id)