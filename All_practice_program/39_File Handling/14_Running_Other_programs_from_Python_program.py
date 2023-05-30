'''

os module contains system() function to run programs and commands.
The argument is any command which is executing from DOS.

SYNTAX: os.system("commad string")

'''

import os

os.system('dir *.py') 
'''
OUTPUT:

 Volume in drive C is Acer
 Volume Serial Number is E826-0C68

 Directory of C:\Users\anilg\OneDrive\Desktop\practice-python\All_practice_program\39_File Handling

28-05-2023  11:38             2,340 01_about_file_handling.py
28-05-2023  11:45               912 02_Various_properties_of_File_Object.py
28-05-2023  11:53             1,087 03_Writing_data_to_text_files.py
28-05-2023  15:05             1,778 04_Reading_Character_Data_from_text_files.py
28-05-2023  15:18               626 05_with_statement.py  
28-05-2023  17:14             1,535 06_seek()_and_tell().py
28-05-2023  17:17               856 07_How_to_check_a_particular_file_exists_or_not.py
29-05-2023  07:55               573 08_print_the_number_of_lines,_words_and_characters_present_in_the_given_file.py 
29-05-2023  13:04               351 09_Handling_Binary_data.py
29-05-2023  08:44             1,749 10_Handling_CSV_files.py
29-05-2023  17:14               896 11_Zipping_of_files.py
29-05-2023  17:14               617 12_unzipping_of_files.py
29-05-2023  18:00             5,750 13_working_with_directories.py
29-05-2023  21:18               238 14_Running_Other_programs_from_Python_program.py
29-05-2023  19:12                32 mo.py
              15 File(s)         19,340 bytes
               0 Dir(s)  33,667,497,984 bytes free 

'''

os.system('notepad') # it will open notepad

os.system('py 02_Various_properties_of_File_Object.py') # it will execute this program.

'''
we can execute any command by os.system(), which can be executed by cmd.
'''