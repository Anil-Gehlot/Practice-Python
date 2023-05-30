'''
It is very common requirement to perform operations for directories like:

1. To know current working directory
2. To create a new directory
3. To remove an existing directory
4. To rename a directory
5. To list contents of the directory
etc...

To perform these operations,Python provides inbuilt module os,which contains several
functions to perform directory related operations.

'''

# Q1: To Know Current Working Directory.
import os
cwd = os.getcwd()
print(cwd)
print('----------------------------------------')

# '''
# OUTPUT:
# C:\Users\anilg\OneDrive\Desktop\practice-python\All_practice_program\39_File Handling
# '''

# Q2. To create a sub directory in the current working directory:

import os
os.mkdir('anil')
print("anil directory created in cwd")
print('----------------------------------------')


# Q3. To create a sub directory in anil directory:
import os
os.mkdir('anil/prabhas')
print("prabhas created inside anil")

''' Note: For creating a subdirectory, A directory must be created before. '''
print('----------------------------------------')


# Q4. To create multiple directories like sub1 in that sub2 in that sub3:

import os
os.makedirs('sub1/sub2/sub3 and sub4')
print("All the directories successfully created")
print('----------------------------------------')


# Q5. To remove a directory:

import os

# it will raise an Error, because anil is not empty.
# if we are deleting directory using 'rmdir' it must be empty.
# os.rmdir('anil')

# firstly we will remove, 'prabhas' inside anil.
os.rmdir('anil/prabhas')
print('prabhas removed successfully')
os.rmdir('anil')
print('anil is removed successfully')
print('----------------------------------------')


# Q6. To remove multiple directories in the path:

import os
os.removedirs('sub1/sub2/sub3 and sub4')
print('All the directories are removed succesfully')
print('----------------------------------------')


# Q7. To rename a directory:

import os

# firstly creating a directory.
os.mkdir('happy')
print('happy is created happily')

# now renaming it.
os.rename('happy','sad')
print('happy is now sad')
print('----------------------------------------')


# Q8. To know contents of directory:

'''
os module provides listdir() to list out the contents of the specified directory. It won't
display the contents of sub directory
'''

import os 
content = os.listdir(".")   # here '.' means current working directory(CWD).
print('content of current working directory\n')
print(content)

print()

print('content of sad\n')
print(os.listdir('sad'))

'''
OUTPUT:

content of current working directory

['01_about_file_handling.py', '02_Various_properties_of_File_Object.py', '03_Writing_data_to_text_files.py',
 '04_Reading_Character_Data_from_text_files.py', '05_with_statement.py', '06_seek()_and_tell().py
 ', '07_How_to_check_a_particular_file_exists_or_not.py', 
 '08_print_the_number_of_lines,_words_and_characters_present_in_the_given_file.py', '09_Handling_Binary_data.py',
'10_Handling_CSV_files.py', '11_Zipping_of_files.py', '12_unzipping_of_files.py', '13_working_with_directories.py',
 'abc.txt', 'abcd.txt', 'abcde.txt', 'demo.py', 'emp.csv', 'new.txt', 'newpic.jpg', 'newzip.zip', 'prabhas.png', 'sad']

content of sad
 
[]
'''

"""

*** The above program display contents of current working directory but not contents of sub
directories.
If we want the contents of a directory including sub directories then we should go for
walk() function.

"""
print('----------------------------------------')


# Q9. To know contents of directory including sub directories:

'''
We have to use walk() function

os.walk(path,topdown=True,onerror=None,followlinks=False)

 It returns an Iterator object whose contents can be displayed by using for loop

path-->Directory path. cwd means .
topdown=True --->Travel from top to bottom
onerror=None --->on error detected which function has to execute.
followlinks=True -->To visit directories pointed by symbolic links.



*** Note: To display contents of particular directory,we have to provide that directory name
as argument to walk() function.

os.walk("directoryname")
'''

# : To display all contents of Current working directory including sub directories:

import os
for dirpath, dirnames, filenames in os.walk('.'):
    print("Current Directory Path:",dirpath)
    print("Directories:",dirnames)
    print("Files:",filenames)
    print() 

'''
Current Directory Path: .
Directories: ['sad']
Files: ['01_about_file_handling.py', '02_Various_properties_of_File_Object.py', '03_Writing_data_to_text_files.py',
'04_Reading_Character_Data_from_text_files.py', '05_with_statement.py', '06_seek()_and_tell().py', '07_How_to_check_a_particular_file_exists_or_not.py',
'08_print_the_number_of_lines,_words_and_characters_present_in_the_given_file.py', '09_Handling_Binary_data.py', '10_Handling_CSV_files.py', '11_Zipping_of_files.py',
 '12_unzipping_of_files.py', '13_working_with_directories.py', 'abc.txt', 'abcd.txt', 'abcde.txt', 'demo.py', 'emp.csv', 'new.txt', 'newpic.jpg', 'newzip.zip', 'prabhas.png']

Current Directory Path: .\sad
Directories: []
Files: []
'''
print('----------------------------------------')




'''

Q. What is the difference between listdir() and walk() functions?

ANS:    In the case of listdir(), we will get contents of specified directory but not sub directory
        contents. 
                    But in the case of walk() function we will get contents of specified directory and
                    its sub directories also.
'''

print('----------------------------------------')
