This program works as a simple file explorer made with Python that runs 
in the terminal. It supports three commands: C to create a new .dsu file in a 
specified directory, D to delete an existing .dsu file, and R to read and print 
the contents of a .dsu file. The program waits for user input until 
the user enters Q to quit.

The program uses the pathlib library to handle file system operations in a 
cross-platform way, so it works on both Windows and Mac/Linux. 
Also, it uses the shlex library to parse user input, which allows it to correctly 
handle file paths that contain spaces. The program will print ERROR for any 
invalid commands, missing files, wrong file types, or incorrect input formatting.
