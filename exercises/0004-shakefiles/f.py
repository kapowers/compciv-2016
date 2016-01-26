import os
fname = os.path.join('tempdata', 'tragedies', 'romeoandjuliet')
txtfile = open(fname, 'r')
line_num = 0

for n in range(4766 - 5): 
    line_num += 1
    txtfile.readline()

for line in txtfile:
    line_num += 1
    the_line = str(line_num) + ": " + line.strip()
    print(the_line) 
    
txtfile.close()