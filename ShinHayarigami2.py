import os,sys,struct

def main(file):
    if not os.path.exists(file):
        print("File not exist")
        return
    data = open(file, 'rb')
    folname = file.rsplit('.', -1)[0]
    os.system("mkdir " + folname)
    data.seek(8, 0)
    filetotal = struct.unpack(">I",data.read(4))[0]
    print("Totaly " + str(filetotal) + " files")
    
    for i in range (filetotal):
        data.seek(16 + i*64, 0)
        filename = cstr(b'' + data.read(48))
        dr1,flength,dr2,fstart = struct.unpack(">4I",data.read(16))
        data.seek(fstart)
        wrfile = open(folname + "/" + filename, 'wb')
        wrfile.write(data.read(flength))
        wrfile.close()
        print("complete " + folname +" "+ str(i+1))
    print("Complete!")

def cstr(s):
    p = "{}s".format(len(s))
    s = struct.unpack(p,s)[0]
    return str(s.replace(b"\x00",b""),encoding = "sjis",errors = "ignore")
    
if __name__ =="__main__":
    if len(sys.argv) < 2 :
        exit()
    files=[]
    files=sys.argv[1:]
    for file in files:
        main(file)
    
