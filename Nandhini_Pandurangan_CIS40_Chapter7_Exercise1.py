# CIS40: Summer 2020: Chapter 7 Exercise 1: Nandhini Pandurangan
# This program reads a backend error log file and reports its statistics
# The number of lines, the number of errors, and the error lines are written
# to a file and is also printed to the console

def make_report():
    """
    Reads the file, counts the # of lines, counts the # of errors and the lines they occur on
    Prints the results to the console and also writes a report on reportError.txt
    """

    flag = True # controls user input on the filename
    while flag:
        try:
            file_name = input("Please enter the name of the backend error log file name: ").strip()
            file = open(file_name, 'r')  # open the file for reading
            flag = False

        except IOError:  # if file does not exist:
            print("\nUnable to open file for reading. Please enter the name of an existing "
                  "backend error log file name.\n")

    error_count = 0
    line_count = 0
    error_list = []

    # reading through the file line by line
    for line in file:
        line = line.strip()  # removing leading and trailing whitespace

        # counting lines which are not empty
        if line != "":
            line_count += 1

            # checking to see if an "error" exists
            lower_line = line.lower()
            if 'error' in lower_line:
                error_list.append(line)
                error_count += 1

    # writing to the report file
    report = open("reportError.txt", 'w')
    line_report = "The number of lines in the backend error log file " + file_name + " are " + str(line_count) + "\n"
    report.write(line_report)

    error_report = "The number of errors in the backend error log file are " + str(error_count) + "\n"
    report.write(error_report)
    report.write('\n')

    report.write("The following lines contain errors: \n")
    for error_line in error_list:
        report.write(error_line + "\n")  # writing to the file

    # printing the results to the console
    print()
    print(line_report)
    print(error_report)
    print("The following lines contain errors: ")
    [print(error_line) for error_line in error_list]

    file.close()
    report.close()


# calling the function make_report()
make_report()

"""
Output: 

Please enter the name of the backend error log file name: ErrorLog.txt

The number of lines in the backend error log file ErrorLog.txt are 108

The number of errors in the backend error log file are 5

The following lines contain errors: 
[Sun Mar  7 21:16:17 2018] [error] [client 24.70.56.49] File does not exist: /home/httpd/twiki/view/Main/WebHome
[Mon Mar  8 07:27:36 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/_vti_bin/owssvr.dll
[Mon Mar  8 07:27:37 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/MSOffice/cltreq.asp
[Thu Mar 11 02:27:34 2018] [error] [client 200.174.151.3] File does not exist: /usr/local/mailman/archives/public/cipg/2018-november.txt
[Thu Mar 11 07:39:29 2018] [error] [client 140.113.179.131] File does not exist: /usr/local/apache/htdocs/M83A
"""