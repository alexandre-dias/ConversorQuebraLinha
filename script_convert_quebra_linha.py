data_file = open('main.txt','r').read().splitlines()

# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


for file in data_file:

    with open(file,'ab') as add_line_ending:
        add_line_ending.write(b'\r\n')
    
    with open(file, 'rb') as open_file:
        content = open_file.read()
		
    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

    with open(file, 'wb') as open_file:
        open_file.write(content)