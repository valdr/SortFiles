#Parsing and renaming files
#file format starting with: Episode title - Series title - #99.mp4
import os # so we can deal with files

#!/usr/bin/python

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Input file is "', inputfile)
   print('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
# ----------------------------------------------------------------------
#~ os.chdir(input('please provide the directory: ')) #path where files are
#~ mydir = os.getcwd()
#~ print(mydir)

#~ for f in os.listdir(mydir):
	#~ f_name, f_ext = os.path.splitext(f)
	#~ f_exts = 'dir-'+f_ext.strip()[1:]
	#~ old_path = os.path.join(mydir, f)
	#~ new_path = os.path.join(os.sep, mydir, f_exts, f)
	#~ print('old path', old_path)
	#~ if os.path.isdir(f):
		#~ pass
	#~ elif os.path.isdir(f_exts):
		#~ print(os.path.abspath(f))
		#~ os.rename(old_path, new_path)
		#~ print('new path', new_path)
	#~ else: 
		#~ os.makedirs(f_exts)
		#~ os.rename(old_path, new_path)
		#~ print(f_ext, 'is now a directory')
		
		#~ if os.path.exists('{}'.format(f_ext)):
			#~ print(f_ext, 'exists already')
			#~ os.chdir(f_ext) #path where files are
			#~ mydir = os.getcwd()
		#~ else:
			#~ print('creating directory', f_ext)
			#~ os.makedirs(f_ext)


		#~ f_title, f_series, f_num = f_name.split('-') # f_series also
		#~ f_title = f_title.strip()
		#~ f_series = f_series.strip()
		#~ f_num = f_num.strip()[1:].zfill(2) #
		#~ new_name = '{}-{}-{}{}'.format(f_num, f_series, f_title, f_ext) #  f_series also
		#~ new_name2 = '{}-{}{}'.format(f_num, f_title, f_ext)
		#~ old_name = '{} - {} - {}{}'.format(f_title, f_series, f_num, f_ext) #f_series also
		#~ print('to:', f_name)		

	#~ os.rename(f, new_name2)
	
""" Intermediate steps printed:
	#~ print(f)
	#~ print(os.path.splitext(f))
	#~ print(f_name)
	#~ print(f_name.split('-'))
	#~ print(f_title)
	#~ print(new_name)
	#~ print(new_name2)
	#~ print() """
