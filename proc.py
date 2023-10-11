import os
from tkinter import filedialog as fd

print("Start")


in_name = fd.askopenfilename()
in_file = open(in_name,'rt')
in_lines = in_file.readlines()
in_file.close()


out_lines = []
out_file = open("output.csv",'a')

for line in in_lines:
  print(line)
  newline = line.replace("\n","").replace("\r","").replace(" ",",").replace(",,",",").replace(",,",",")+"\n"
  if (newline[0] == ",") : newline = newline[1:len(newline)]
  out_lines.append(newline)

out_file.writelines(out_lines)
out_file.close()


print("Done")
