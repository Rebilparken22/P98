with open("file1.txt","r+") as f:
    f_contents = f.read()
with open("file2.txt","r+") as g:
    g_contents = g.read()

def swapfiles():
    f.write(g_contents)
    g.write(f_contents)

swapfiles()
f.close()
g.close()