def quit():
    exit()

def creatNewFile(f):
    file = open(f, "w")
    file.close()
    return file

def editFile(f, value):
    file = open(f, "w")
    edit = file.write(value)
    return edit