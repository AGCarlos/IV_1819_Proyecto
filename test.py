from fileS import FileDownload
import redis

fl = FileDownload()
class TestClass(object):
    #Check if returns true
    def test_True(self):
        assert fl.devuelveTrue() == True

    #Check checkUser
    def test_checkUser(self):
        assert fl.checkUser("lamslf") == "OK"
        fl.createFile(1,"{'lmao':'lmao'}")
        assert fl.checkUser(1) == "None"
        assert fl.checkUser(True) == "None"
        assert fl.checkUser(1.0) == "None"

    #Check createFile
    def test_userCreated(self):
        r = redis.Redis()
        assert fl.createFile(1,"{'lmao':'lmao'}") == 'OK'
        assert fl.createFile("{'lmao':'lmao'}",1,) == 'None'
        assert fl.createFile("{'lmao':'lmao'}","{'lmao':'lmao'}") == 'None'
        assert fl.createFile(True,"{'lmao':'lmao'}") == 'None'
        assert fl.createFile("{'lmao':'lmao'}",True) == 'None'

    #Check if file is created correctly
    def test_userCreatedCorrect(self):
        r = redis.Redis()
        fl.createFile(1,"{'lmao':'lmao'}")
        assert str(r.get(1)) != "None"
        assert str(r.get("userasdas:psadasasswd")) == 'None'

    #Check deleteFile
    def test_userDeletedCorrect(self):
        r = redis.Redis()
        assert fl.deleteFile(1) == 'OK'
        assert fl.deleteFile("passwd") == 'None'
        assert fl.deleteFile(True) == 'None'

    #Check if file is deleted correctly
    def test_userDeleted(self):
        r = redis.Redis()
        fl.createFile(1,"{'lmao':'lmao'}")
        fl.deleteFile(1)
        assert str(r.get(1)) == "b'None'"
