#Employee Access Management
it = {101, 102, 103, 104, 105}
hr = {104, 105, 106, 107}

print("Common Employees:", it.intersection(hr))
print("Only IT:", it.difference(hr))
print("Only HR:", hr.difference(it))
print("Total Employees:", it.union(hr))
print("Employees in Only One Department:", it.symmetric_difference(hr))