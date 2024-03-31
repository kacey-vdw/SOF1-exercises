# take two strings containing names of two files, read one file and 
# copy contents to other file in uppercase

def to_upper_case(input_file, output_file):
	f_input = open(input_file, 'r') #opens input file in read mode
	contents = f_input.read() #copies contents of input file to variable
	f_input.close() #closes file

	f_output = open(output_file, 'w') #opens output file in write mode
	f_output.write(contents.upper()) #writes contents in uppercase to output file
	f_output.close() #closes file

to_upper_case("exo1", "exo2")
