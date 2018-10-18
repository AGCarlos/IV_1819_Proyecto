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
        assert fl.checkUser("fernando","iv") != "None"

    #Check if file is created correctly
    def test_userCreated(self):
        r = redis.Redis()
        fl.createFile("user","passwd","file.png")
        assert str(r.get("user:passwd")) != "b'None'"

    #Check if file is deleted correctly
    def test_userDeleted(self):
        r = redis.Redis()
        fl.createFile("user","passwd","file.png")
        fl.deleteFile("user","passwd")
        assert str(r.get("user:passwd")) == "b'None'"
