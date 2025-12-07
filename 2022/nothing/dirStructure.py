#create a node class for a tree
#maybe create a tree class, then a sub-class for folders, and files?

class node():
    
    def __init__(self,name,type="file",parent=None,size=0):
        self.name = name
        self.type = type
        self.parent = parent
        self.size = size
        self.child = []

    def __repr__(self):
        parent = ""
        if self.parent:
            parent = self.parent.name
        
        return "name:\t%s\ntype:\t%s\nparent:\t%s\nsize:\t%s" % (self.name,self.type,parent,self.size)

    def addChild(self,child):
        self.child.append(child)

    def getSize(self):
        #print("name: %s\t\tsize: %s" % (self.name,self.size))
        if self.type == "file":
            return self.size
        elif self.type == "dir":
            if not self.size:
                for child in self.child:
                    self.size += child.getSize()
            return self.size


dirList = []

dirList.append(node("/","dir"))
dirList.append(node("tmp","dir",dirList[0]))
dirList.append(node("tmp1.py","file",dirList[-1],1234))
dirList.append(node("tmp2.py","file",dirList[1],1234))
dirList.append(node("tmp2","dir",dirList[1]))
dirList.append(node("file1.txt","file",dirList[4],5678))
dirList.append(node("file1.txt","file",dirList[0],7890))

'''
print(dirList[1].getSize())
for child in [x for x in dirList if x.parent == dirList[1]]:
    dirList[1].addChild(child)
print(dirList[1].getSize())
'''

for item in dirList:
    if item.type == "dir":
        for child in [x for x in dirList if x.parent == item]:
            item.addChild(child)

for item in dirList:
    item.getSize()
    print(item,"\n")


            