from Package_File import Module_File_01

Module_File_01.FirstFunction()

Module_File_01.SecondFunction()

Module_File_01.ThirdFunction()

# Output:
# This is the first function.
# This is the second function.
# This is the third function.


from Package_File.Module_File_02 import hello_world

hello_world()

from Package_File.Module_File_02 import another_function as secOne

secOne()

# Output:
# Hello, World from Module File 02!
# This is another function in Module File 02.

