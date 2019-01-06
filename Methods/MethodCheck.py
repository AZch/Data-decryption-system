from Methods.Method import Method
import time
import random

class MethodCheck(Method):

    def __init__(self, data):
        super().__init__(data=data)
        self.start = 1
        self.end = 90
        pass

    def calc(self):
        time.sleep(random.randint(self.start, self.end))
        return self.resData
        pass

    def exportXMLStr(self):
        resStr = "<MethodCheck>" \
            "<start>" + str(self.start) + "</start>" \
            "<end>" + str(self.end) + "</end>" \
            "</MethodCheck>"
        return resStr