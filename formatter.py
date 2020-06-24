"""
SCAN FORMATTER

Script used to format a .txt file associated with an diagnostic scan tool

- Expects a file named "s.txt" to be present in same directory as formatter.py
- If no file named "s.txt" is present then a "No codes" text will be added in place of scan info
- Copies txt from s.txt and appends it to the current date and a given repair order number
- Creates scan.txt in same directory with the current date, r.o. number, and scan info
- Deletes s.txt when finished to avoid naming issues with next scan file used


MIT License

Copyright (c) 2020 Tim Seymore

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import time
import os
from datetime import datetime


# date line to be in new file
today = datetime.now().strftime("%m/%d/%Y")
date_line = "Scan date: " + today + "\n"

# ro number line to be added to new file
ro_num = input("Enter Repair Order number: ")
ro_line = "RO: " + ro_num + "\n\n"

# load and copy to list the contents of s.txt
scan_file = "s.txt"
new_data = [date_line, ro_line]
try:
    with open(scan_file, "r") as f:
        for line in f:
            new_data.append(line)
    os.remove(scan_file)
except FileNotFoundError:
    new_data.append("Passed: No codes found")

# write data to new file (will overwrite any existing file)
# print out data to console in file format
print("\n===== New File Output =====\n")
with open("scan.txt", "w") as f:
    for line in new_data:
        f.write(line)
        print(line, end="")
print()

# wait 5 seconds to review and then exit program
time.sleep(3)
print("\nExiting...")
time.sleep(2)
