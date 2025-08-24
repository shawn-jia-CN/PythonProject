import sys
NoError = 0
InvaildParameter = -1
NoCapacity = -2
NotFound = -3


ErrorMap = {
    NoError : "No Error",
    InvaildParameter : "Invaild Parameter",
    NoCapacity : "No capacity",
    NotFound : "NotFound"
}

class MyCustomError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class myRerunValue:
    def __init__(self, returnMsg = "", returnCode = NoError):
        self.code = NoError
        self.msg = ""
        if returnCode > NoError:
            raise MyCustomError("errCode should be nagative value or zero")
        else :
            self.code = returnCode
            if returnMsg != "":
                self.msg = returnMsg
            else:
                if self.code in ErrorMap.keys():
                    self.msg = ErrorMap[self.code]
    
    def getErrorCode(self):
        return self.code
    
    def getErrorMsg(self):
        return self.msg

    def success(self):
        return self.code == NoError


def checkAns(ret : myRerunValue) -> bool:
    return ret.success()
