from Parser import parser

##
##class textparse(object):
##    def __init__(self):
##        print("init")
##    def textmain(self):
##        self.parser().configparse("config.ini","config.json")
##
##
##if __name__ == '__main__':
##    textparse = textparse()
##    textparse.textmain()


def textmain():
    parser().configparse("config.ini","config.json")
    
textmain()

