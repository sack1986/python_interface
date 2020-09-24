import unittest

if __name__=="__main__":
    myDir="E:\myTestCase"
    discover=unittest.defaultTestLoader.discover(myDir,"tst1.py")
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(discover)