f = open('/tmp/testout', 'r')
total_length = 0
for line in f:
    list = line.split()
    if len(list) == 3:
        seq = int(list[0])
        shot = int(list[1])
        length = int(list[2])
        total_length += length
        print("seq: %d, shot %d: length is %d" % (seq, shot, length))
print("Total length:", total_length)
f.close()