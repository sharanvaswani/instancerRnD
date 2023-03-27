node = hou.pwd()
parm = node.parm('inputs')

num = parm.eval()
list = range(0, num)
menu = []

for i in list:
    menu.extend([i, 'Inputs Bundle ' + str(i)])
    
return menu
print menu