#Software License Management
photoshop = {101, 102, 103, 104}
vscode = {103, 104, 105}
autocad = {104, 105, 106}

print("All Three:", photoshop & vscode & autocad)
print("Photoshop Only:", photoshop - (vscode | autocad))
print("AutoCAD Not Photoshop:", autocad - photoshop)
print("Total Employees:", photoshop | vscode | autocad)
print("At Least One License:", photoshop.union(vscode).union(autocad))