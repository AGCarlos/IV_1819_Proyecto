from fileS import FileDownload
import redis

fl = FileDownload()
r = redis.Redis()

class TestClass(object):
    #Check if returns true
    def test_True(self):
        assert fl.devuelveTrue() == True

    #Check checkUser
    def test_checkUser(self):
        fl.createFile("archivo",{'lmao':'lmao1'},r)

        assert fl.checkUser("archivo",r) == "OK"
        assert fl.checkUser(1,r) == "None"
        assert fl.checkUser(True,r) == "None"
        assert fl.checkUser(1.0,r) == "None"

    #Check createFile
    def test_userCreated(self):
        fl.createFile("archivo",{'lmao':'lmao1'},r)
        assert fl.createFile({'lmao':'lmao'},"lmao",r) == 'None'
        assert fl.createFile({'lmao':'lmao'},1,r) == 'None'
        assert fl.createFile(1,{'lmao':'lmao'},r) == 'None'
        assert fl.createFile(True,{'lmao':'lmao'},r) == 'None'
        assert fl.createFile({'lmao':'lmao'},True,r) == 'None'
        assert fl.createFile(1,True,r) == 'None'

    #Check if file is created correctly
    def test_userCreatedCorrect(self):
        fl.createFile("archivo",{'lmao':'lmao1','lmao2':'lmao3'},r)
        assert str(r.hmget("archivo","lmao"))[3:-2] == 'lmao1'
        assert str(r.hmget("archivo","lmao2"))[3:-2] == 'lmao3'
        assert str(r.hmget("archivo","otracosa"))[1:-1] == 'None'

    #Check deleteFile
    def test_userDeletedCorrect(self):
        fl.createFile("archivo",{'lmao':'lmao'},r)
        assert fl.deleteFile("leler8",r) == 'OK'
        assert fl.deleteFile(True,r) == 'None'
        assert fl.deleteFile(1,r) == 'None'
    #Check if file is deleted correctly
    def test_userDeleted(self):
        fl.createFile("archivo",{'lmao':'lmao'},r)
        fl.deleteFile("archivo",r)
        assert str(r.hmget("archivo","lmao"))[1:-1] == "None"
