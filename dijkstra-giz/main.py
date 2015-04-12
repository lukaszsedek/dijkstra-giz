
#!/usr/bin/python

from optparse import OptionParser
import logging, sys

verbose = True
filename = ""

if __name__ == "__main__":
	# OptParse section
	parser = OptionParser()
	parser.add_option("-f", "--file", dest="filename",
		help="load initial topology from FILE", metavar="FILE")
	parser.add_option("-l", "--log", dest="loglevel", default="INFO",
		help="set logging level LOG, DEBUG", metavar="LEVEL")
	(options, args) = parser.parse_args()
	
	# logging utils section
	permitted_log_levels = {"INFO", "DEBUG"}
	if any(options.loglevel.upper() in item for item in permitted_log_levels):
		logging.basicConfig(level=options.loglevel.upper())
	else:
		logging.basicConfig(level="INFO")

	# filename loading section
	logging.debug("checking filename argument")
	if options.filename:
		logging.debug("options.filename exists: %s", options.filename)
		filename = options.filename
		logging.debug("variable filename sucessfully initialized : %s "
			, filename)
	else:
		logging.error("Filename not found. Program is exiting")
		sys.exit(0)

	# load confif from filename with readonly permissions
	f = open(filename, 'r')
	line_numer = 0
	for line in f:
		logging.debug("Line %s : %s", line_numer, line.rstrip('\n'))
		if line_numer == 0:
			logging.debug("First line")
			splitted_line = line.split()
			logging.debug("Splitted line: %s", splitted_line)

		line_numer = line_numer+1
	logging.debug("closing file...")
	f.close()
