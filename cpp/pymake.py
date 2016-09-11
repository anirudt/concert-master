import os

g = open("CMakeLists.txt", 'wb')

# First Line
g.write('cmake_minimum_required(VERSION 2.8)\n')
files = [f for f in os.listdir('.') if os.path.isfile(f)]
cpp_file = ""
for e in files:
	if(e.find('.cpp')!=-1):
		cpp_file = e
tmp = ""
#Second Line
tmp = cpp_file[0:-4]

g.write('project( '+tmp+ ' )\n')
g.write('find_package( OpenCV REQUIRED )\n')
g.write('include_directories( ${OpenCV_INCLUDE_DIRS} )\n')
g.write('add_executable( '+tmp + ' ' + cpp_file+' )\n')
g.write('target_link_libraries( '+ tmp + ' ${OpenCV_LIBS} )\n')
