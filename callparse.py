from Parser.Parser import parser
import sys

#Method passes the argument to parser
def textParser(input_filename, output_filename):
    parser().configparse(input_filename, output_filename)

# Passing the arguments for input and output file
if __name__ == "__main__":   
    textParser(sys.argv[1], sys.argv[2])


    
