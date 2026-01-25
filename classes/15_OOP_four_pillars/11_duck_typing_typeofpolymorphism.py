# duck typing : it is concept where duck type of an object is determined by its behaviour not by its class. its is type of polymorphism.

class inkjectprinter: # machine, hardware
    def printdocument(self,document):
        print("inkjet printer printing :",document)

class leserprinter: # machine, hardware
    def printdocument(self,document):
        print("leser printer printing :",document)

class pdfwriter:  # application, software
    def printdocument(self,document):
        print(f"saving {document} as pdf")


def startprinting(Device):
    obj = Device()
    obj.printdocument("marvallous notes")

def main():
    startprinting(inkjectprinter)
    startprinting(leserprinter)
    startprinting(pdfwriter)

main()