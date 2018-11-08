from fileS import FileDownload
import redis

fl = FileDownload()
class TestClass(object):
    #Check if returns true
    def test_True(self):
        assert fl.devuelveTrue() == True

    #Check checkUser
    def test_checkUser(self):
        fl.createFile("archivo",{'lmao':'lmao1'})
        r = redis.Redis()

        assert fl.checkUser("archivo") == "OK"
        assert fl.checkUser(1) == "None"
        assert fl.checkUser(True) == "None"
        assert fl.checkUser(1.0) == "None"

    #Check createFile
    def test_userCreated(self):
        r = redis.Redis()
        fl.createFile("archivo",{'lmao':'lmao1'})
        assert fl.createFile({'lmao':'lmao'},"lmao") == 'None'
        assert fl.createFile({'lmao':'lmao'},1) == 'None'
        assert fl.createFile(1,{'lmao':'lmao'}) == 'None'
        assert fl.createFile(True,{'lmao':'lmao'}) == 'None'
        assert fl.createFile({'lmao':'lmao'},True) == 'None'
        assert fl.createFile(1,True) == 'None'

    #Check if file is created correctly
    def test_userCreatedCorrect(self):
        r = redis.Redis()
        fl.createFile("archivo",{'lmao':'lmao1','lmao2':'lmao3'})
        assert str(r.hmget("archivo","lmao"))[3:-2] == 'lmao1'
        assert str(r.hmget("archivo","lmao2"))[3:-2] == 'lmao3'
        assert str(r.hmget("archivo","otracosa"))[1:-1] == 'None'

    #Check deleteFile
    def test_userDeletedCorrect(self):
        r = redis.Redis()
        fl.createFile("archivo",{'lmao':'lmao'})
        assert fl.deleteFile("leler8") == 'OK'
        assert fl.deleteFile(True) == 'None'
        assert fl.deleteFile(1) == 'None'
    #Check if file is deleted correctly
    def test_userDeleted(self):
        r = redis.Redis()
        fl.createFile("archivo",{'lmao':'lmao'})
        fl.deleteFile("archivo")
        assert str(r.get("archivo")) == "None"
