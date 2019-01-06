import unittest
from Constants import StrRetConts
from FactoryMethods.FactoryMethodCheck import FactoryMethodCheck
from WorkApi import WorkApi
from Data.Data import Data

class TestWorkApi(unittest.TestCase):

    def test_loadData(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.assertEqual(self.workApi.loadData(way=self.wayLoadData), StrRetConts.retGood)

    def test_saveData(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.assertEqual(self.workApi.saveData(data=self.data, way=self.waySaveData), StrRetConts.retGood)

    def test_clearData(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.workApi.clearCurrData()
        self.assertEqual(len(self.workApi.currData), 0)

    def test_goStartMethod(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.workApi.goStartMethod()
        self.assertEqual(self.workApi.startMethod, self.workApi.currMethod)

        self.workApi.goNextMethod()
        self.workApi.goStartMethod()
        self.assertEqual(self.workApi.startMethod, self.workApi.currMethod)

        self.workApi.goPrevMethod()
        self.workApi.goStartMethod()
        self.assertEqual(self.workApi.startMethod, self.workApi.currMethod)

    def test_goPrevMethod(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.assertEqual(self.workApi.goPrevMethod(), StrRetConts.retGood)

    def test_goNextMethod(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.assertEqual(self.workApi.goNextMethod(), StrRetConts.retGood)

    def test_setFactoryCheck(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.workApi.setFactoryCheck()
        self.assertTrue(type(self.workApi.factoryMethods) == FactoryMethodCheck)

    def test_createMethod(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.assertEqual(self.workApi.createMethod(), StrRetConts.retGood)

    def test_calcMethod(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.workApi.calcMethod()
        try:
            self.assertEqual(self.workApi.calcMethod(), self.workApi.currMethod.getResData)
        except:
            self.assertNotEqual(self.workApi.calcMethod(), StrRetConts.retBat)

    def test_delMethod(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.assertEqual(self.workApi.delMethod(), StrRetConts.retGood)

    def test_exportMethod(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.assertEqual(self.workApi.exportMethod(), StrRetConts.retGood)

    def test_saveInputData(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.assertEqual(self.workApi.saveInputData(), StrRetConts.retGood)

    def test_saveResData(self):
        data = Data()
        self.workApi = WorkApi(baseData=data)
        self.wayLoadData = "testLoad.txt"
        self.data = data
        self.waySaveData = "testSave.txt"
        self.assertEqual(self.workApi.saveResData(), StrRetConts.retGood)

if __name__ == '__main__':
    unittest.main()