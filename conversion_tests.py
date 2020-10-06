import converter

def testRunner():
    testConvertMPGtoKPL()
    testconvertMItoKM()
    testconvertGALtoL()
    testconvertCMtoIN()
    testconvertFTtoMI()


def testConvertMPGtoKPL():
    assert round(converter.convertMPGtoKPL(5),5) == 2.12572

def testconvertMItoKM():
    assert round(converter.convertMItoKM(2), 3) == 3.219

def testconvertGALtoL():
    assert round(converter.convertGALtoL(4),4) == 15.1416

def testconvertCMtoIN():
    assert round(converter.convertCMtoIN(8),4) == 3.1496

def testconvertFTtoMI():
    assert round (converter.convertFTtoMI(1000),6) == 0.189394


testRunner()
print ("all tests passed")