#write to file without erasing previous contents

def save_to_log(entry, logfile):
	f = open(logfile, 'a') #opens file without erasing previous contents
	f.write(entry+'\n') #appends entry on new line
	f.close() #closes file

save_to_log("Haha get appended", 'exo1')