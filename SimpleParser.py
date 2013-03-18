## Small util to interpret data on Friedland Response Alarm

## first column is time, second is 1/0
datafile = open("F:\data\in.csv",'r')

bindata = []

for row in datafile:
    parts = row.strip().replace("'",'').split(',')
    timestring = parts[0]
    if timestring.startswith('Time'):
        continue
    bindata.append(parts[1])

## Find first occurrence of "111" in the data
for i in range(0,len(bindata)-3):
    bits = ''.join(bindata[i:i+3])
    if bits == '111':
        break

## delete the data before "111"
del bindata[0:i]

outdata = []

## Transform data from bit stream to
## 100 = 0
## 110 = 1
## 111 = 3
## 000 = 4
## anything else = -1

for i in range(0,len(bindata)-3,3):
    bits = ''.join(bindata[i:i+3])
    if bits == '100':
        outdata.append(0)
    elif bits == '110':
        outdata.append(1)
    elif bits == '111':
        outdata.append(3)
    elif bits == '000':
        outdata.append(4)
    else:
        outdata.append(-1)

# Concatenate into one big string
datastring = ''.join(str(v) for v in outdata)

# Split the data on 111000 or 3,4
print(datastring.split('34')[1:])