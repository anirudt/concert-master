# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/anirudt/Projects/small_projects/concert-master/cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/anirudt/Projects/small_projects/concert-master/cpp

# Include any dependencies generated for this target.
include CMakeFiles/finger.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/finger.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/finger.dir/flags.make

CMakeFiles/finger.dir/finger.cpp.o: CMakeFiles/finger.dir/flags.make
CMakeFiles/finger.dir/finger.cpp.o: finger.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/anirudt/Projects/small_projects/concert-master/cpp/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/finger.dir/finger.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/finger.dir/finger.cpp.o -c /home/anirudt/Projects/small_projects/concert-master/cpp/finger.cpp

CMakeFiles/finger.dir/finger.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/finger.dir/finger.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/anirudt/Projects/small_projects/concert-master/cpp/finger.cpp > CMakeFiles/finger.dir/finger.cpp.i

CMakeFiles/finger.dir/finger.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/finger.dir/finger.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/anirudt/Projects/small_projects/concert-master/cpp/finger.cpp -o CMakeFiles/finger.dir/finger.cpp.s

CMakeFiles/finger.dir/finger.cpp.o.requires:
.PHONY : CMakeFiles/finger.dir/finger.cpp.o.requires

CMakeFiles/finger.dir/finger.cpp.o.provides: CMakeFiles/finger.dir/finger.cpp.o.requires
	$(MAKE) -f CMakeFiles/finger.dir/build.make CMakeFiles/finger.dir/finger.cpp.o.provides.build
.PHONY : CMakeFiles/finger.dir/finger.cpp.o.provides

CMakeFiles/finger.dir/finger.cpp.o.provides.build: CMakeFiles/finger.dir/finger.cpp.o

# Object files for target finger
finger_OBJECTS = \
"CMakeFiles/finger.dir/finger.cpp.o"

# External object files for target finger
finger_EXTERNAL_OBJECTS =

finger: CMakeFiles/finger.dir/finger.cpp.o
finger: CMakeFiles/finger.dir/build.make
finger: /usr/local/lib/libopencv_videostab.so.3.0.0
finger: /usr/local/lib/libopencv_videoio.so.3.0.0
finger: /usr/local/lib/libopencv_video.so.3.0.0
finger: /usr/local/lib/libopencv_superres.so.3.0.0
finger: /usr/local/lib/libopencv_stitching.so.3.0.0
finger: /usr/local/lib/libopencv_shape.so.3.0.0
finger: /usr/local/lib/libopencv_photo.so.3.0.0
finger: /usr/local/lib/libopencv_objdetect.so.3.0.0
finger: /usr/local/lib/libopencv_ml.so.3.0.0
finger: /usr/local/lib/libopencv_imgproc.so.3.0.0
finger: /usr/local/lib/libopencv_imgcodecs.so.3.0.0
finger: /usr/local/lib/libopencv_highgui.so.3.0.0
finger: /usr/local/lib/libopencv_hal.a
finger: /usr/local/lib/libopencv_flann.so.3.0.0
finger: /usr/local/lib/libopencv_features2d.so.3.0.0
finger: /usr/local/lib/libopencv_core.so.3.0.0
finger: /usr/local/lib/libopencv_calib3d.so.3.0.0
finger: /usr/local/lib/libopencv_features2d.so.3.0.0
finger: /usr/local/lib/libopencv_ml.so.3.0.0
finger: /usr/local/lib/libopencv_highgui.so.3.0.0
finger: /usr/local/lib/libopencv_videoio.so.3.0.0
finger: /usr/local/lib/libopencv_imgcodecs.so.3.0.0
finger: /usr/local/lib/libopencv_flann.so.3.0.0
finger: /usr/local/lib/libopencv_video.so.3.0.0
finger: /usr/local/lib/libopencv_imgproc.so.3.0.0
finger: /usr/local/lib/libopencv_core.so.3.0.0
finger: /usr/local/lib/libopencv_hal.a
finger: /usr/local/share/OpenCV/3rdparty/lib/libippicv.a
finger: CMakeFiles/finger.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable finger"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/finger.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/finger.dir/build: finger
.PHONY : CMakeFiles/finger.dir/build

CMakeFiles/finger.dir/requires: CMakeFiles/finger.dir/finger.cpp.o.requires
.PHONY : CMakeFiles/finger.dir/requires

CMakeFiles/finger.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/finger.dir/cmake_clean.cmake
.PHONY : CMakeFiles/finger.dir/clean

CMakeFiles/finger.dir/depend:
	cd /home/anirudt/Projects/small_projects/concert-master/cpp && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/anirudt/Projects/small_projects/concert-master/cpp /home/anirudt/Projects/small_projects/concert-master/cpp /home/anirudt/Projects/small_projects/concert-master/cpp /home/anirudt/Projects/small_projects/concert-master/cpp /home/anirudt/Projects/small_projects/concert-master/cpp/CMakeFiles/finger.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/finger.dir/depend

