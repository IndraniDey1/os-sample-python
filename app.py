# Sample -- create a file and and some text into it
f= open("exec-test.txt","x+")

for i in range(10):
     f.write("This is line %d\r\n" % (i+1))

f.close() 
