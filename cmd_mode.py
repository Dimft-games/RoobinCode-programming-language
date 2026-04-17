import time
vl = []
value_name = ''
vc = ''
print("==ROOBIN-CODE CMD MODE==")
print("enter help to view aviable functions")
while True:  
    s = input("> ")
    if s[0:5] == "write":
         if not s[5:len(s)] in vl:
             print(s[5:len(s)])
         elif s[5:len(s)] in vl:
             print(globals()[s[5:len(s)]])
    elif s[0:3] == "var":
        if not s[3:len(s)] == "vl" or "value_name" or "s" or "vc" or "script":
            globals()[s[3:len(s)]] = 0
            vl.append(s[3:len(s)])
        else:
            print("ERROR! Can't create variable with this name.")
    elif s[0:3] == "set":
        for i in range(len(s)):
            if s[i] == "=":
                value_name = i
                break
        globals()[s[3:value_name]] = s[i+1:len(s)]
    elif s[0:3] == "chr":
        print(chr(int(s[3:len(s)])))
    elif s[0:3] == "chn":
        print(ord(s[4:len(s)]))
    elif s[0:3] == "min":
        for i in range(len(s)):
            if s[i] == "-":
                vc = i
                break
        print(int(s[3:vc]) - int(s[vc + 1:len(s)]))
    elif s[0:4] == "plus":
            for i in range(len(s)):
                if s[i] == "+":
                    vc = i
                    break
            print(int(s[4:vc]) + int(s[vc:len(s)]))
    elif s[0:3] == "mul":
        for i in range(len(s)):
            if s[i] == "*":
                vc = i
                break
        print(int(s[3:vc]) * int(s[vc + 1:len(s)]))
    elif s[0:3] == "div":
        for i in range(len(s)):
            if s[i] == "/":
                vc = i
                break
        if int(s[3:vc]) % int(s[vc + 1:len(s)]) == 0:
            print(int(s[3:vc]) // int(s[vc + 1:len(s)]))
        else:
            print(int(s[3:vc]) / int(s[vc + 1:len(s)]))
    elif s[0:4] == "wait":
        time.sleep(int(s[4:len(s)]))
    elif s == "help":
        print("1.write [text]")
        print("2.var [Variable name] - create variable")
        print("3.set [Variable name]=[text] - edit variable ")
        print("4.min [First number]-[Second number]")
        print("5.plus [First number]+[Second number]")
        print("6.mul [First number]*[Second number] - multiplication")
        print("7.div [First number]/[Second number] - division")
        print("8.wait [seconds]")