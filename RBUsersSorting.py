
#Working with csv files )
import csv
import os
dir = 'C:\\Users\\nugaevrk\\workspace\\Files'
file = 'users.csv'
file2 = 'usersresult.csv'

f = open(os.path.join(dir, file),"r")
csv_f = csv.reader(f)

samacc = []
emails = []
for i in csv_f:
    samacc.append (i[11])
    emails.append (i[9])

with open((os.path.join(dir,file2)), 'w', newline='') as fp:
    a = csv.writer(fp)
    a.writerow(samacc)




f.close()
