import os
import sys

if len(sys.argv) != 3:
    print("Arguements not there!!")
    sys.exit(2)

arguement1 = sys.argv[1]
arguement2 = sys.argv[2]


func1 = a.replace("void adjust_channels", "void adjust_channels_asimd", 1)

a1 = funct1.find("printf")
a2 = func1.find(";", a1)
func1 = func1.replace(func1[idx1:idx2], 'printf("SIMD")')

func2 = a.replace("void adjust_channels", "void adjust_channels_sve", 1)

a1 = func2.find("printf")
a2 = func2.find(";", a1)
func2 = func2.replace(func2[a1:a2], 'printf("SVE")')

func3 = a.replace("void adjust_channels", "void adjust_channels_sve2", 1)

a1 = func3.find("printf")
a2 = func3.find(";", a1)
func3 = func3.replace(func3[idx1:idx2], 'printf("SVE2\\n")')

f = open(argument2, "r")
a = f.read()
f.close()
a = str(a)
# here we are opeing the file name funciton1.c and giving the file to w in it and copying the content form the func1 file and then we are closing it
funct1 = open("function1.c", "w")
funct1.write(func1)
funct1.close()
# here we are opeing the file name funciton2.c and giving the file to w in it and copying the content form the func2 file and then we are closing it
funct2 = open("function2.c", "w")
funct2.write(func2)
funct2.close()
# here we are opeing the file name funciton3.c and giving the file to w in it and copying the content form the func3 file and then we are closing it
funct3 = open("function3.c", "w")
funct3.write(func3)
funct3.close()

#ifun.h - header file for ifunc
func1 = func1[func1.find("void adjust_channels") : func1.find("{", func1.find("void adjust_channels"))] + ";"
func2 = func2[func2.find("void adjust_channels") : func2.find("{", func2.find("void adjust_channels"))] + ";"
func3 = func3[func3.find("void adjust_channels") : func3.find("{", func3.find("void adjust_channels"))] + ";\n"
header_string = func1 + '\n\n' + func2 + '\n\n' + func3

header_file = open("ifunc.h", "w")
header_file.write(header_string)
header_file.close()


#ifun.c - tool for auto-vectorization
#reading the template file

template = open("template.txt", "r") 
t = template.read()
template.close()

func_prototype = a[a.find("void adjust_channels") : a.find("{", a.find("void adjust_channels"))]

#filling out the template for ASIMD, SVE, SVE2
t = t.replace("##", func_prototype)

t = t.replace('#sve2', func_prototype.replace("adjust_channels", "*sve2"));
t = t.replace('#sve', func_prototype.replace("adjust_channels", "*sve"));
t = t.replace('#asimd', func_prototype.replace("adjust_channels", "*asimd"));

dTypes = ["unsigned", "char", "int", "float", "double", "long", "short", "*"]
func_prototype = func_prototype[func_prototype.find("adjust_channels"):]

for i in dTypes:
    func_prototype = func_prototype.replace(i, "")

t = t.replace("#fsve2", func_prototype.replace("adjust_channels", "adjust_channels_sve2") + ';')
t = t.replace("#fsve", func_prototype.replace("adjust_channels", "adjust_channels_sve") + ';')
t = t.replace("#fasimd", func_prototype.replace("adjust_channels", "adjust_channels_asimd") + ';')


ifunc = open("ifunc.c", "w")
ifunc.write(t)
ifunc.close()
