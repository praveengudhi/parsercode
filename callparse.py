from Parser.Parser import parser
import sys

def textmain(input_filename, output_filename):
    parser().configparse(input_filename, output_filename)
    


if __name__ == "__main__":   
    textmain(sys.argv[1], sys.argv[2])


    
