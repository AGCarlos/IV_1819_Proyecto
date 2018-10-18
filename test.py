from fileS import FileDownload
import redis

fl = FileDownload()
class TestClass(object):
    #Check if returns true
    def test_True(self):
        assert fl.devuelveTrue() == True

    #Check checkUser
    def test_checkUser(self):
        assert fl.checkUser("lamslf","asdasds") == "None"
        fl.createFile("fernando","iv","file.png")
        assert fl.checkUser("fernando","iv") != "None"
        assert fl.checkUser(1,4) == "None"
        assert fl.checkUser(0.0,0.0) == "None"
        assert fl.checkUser(True,False) == "None"

    #Check createFile
    def test_userCreated(self):
        r = redis.Redis()
        assert fl.createFile("user","passwd",1) == 'None'
        assert fl.createFile("user",1,"file.png") == 'None'
        assert fl.createFile(1,"passwd","file.png") == 'None'
        assert fl.createFile(1,1,1) == 'None'
        assert fl.createFile("user","passwd",True) == 'None'

    #Check if file is created correctly
    def test_userCreatedCorrect(self):
        r = redis.Redis()
        fl.createFile("user","passwd","file.png")
        assert str(r.get("user:passwd")) != "None"
        assert str(r.get("userasdas:psadasasswd")) == 'None'

    #Check deleteFile
    def test_userDeletedCorrect(self):
        r = redis.Redis()
        assert fl.deleteFile("user",1) == 'None'
        assert fl.deleteFile(1,"passwd") == 'None'
        assert fl.deleteFile(1,1) == 'None'
        assert fl.deleteFile("user",True) == 'None'

    #Check if file is deleted correctly
    def test_userDeleted(self):
        r = redis.Redis()
        fl.createFile("user","passwd","file.png")
        fl.deleteFile("user","passwd")
        assert str(r.get("user:passwd")) == "b'None'"
