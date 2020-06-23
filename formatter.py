"""
SCAN FORMATTER

Tool used to format a .txt file associated with a scan tool.

- Expects a file named "s.txt" to be present in same directory as formatter.py
- Copies txt from s.txt and appends it to the current date and a given repair order number
- Creates scan.txt with the current date, r.o. number, and scan info
- Deletes s.txt when finished to avoid problems with next scan file used


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
from datetime import datetime


# first line to be in new file
today = datetime.now().strftime("%m/%d/%Y")
date_line = "Scan date: " + today

# second line to be added to new file
ro_num = input("Enter Repair Order number:")
ro_line = "RO: " + ro_num

# load and copy to list the contents of s.txt
scan = []
with open("s.txt", "r") as f:
    for line in f:
        scan.append(line)

# representation of new file
new = [date_line + "\n", ro_line + "\n"] + scan
for line in new:
    print(line)

# write to new file
with open("scan.txt", "w") as f:
    for line in new:
        f.write(line)

# delete s.txt to avoid renaming issues with next scan file

# Exit program
time.sleep(3)
print("Exiting...")
time.sleep(2)
