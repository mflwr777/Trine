import pandas as pd 

a = pd.DataFrame([1,2,3,4,5,5])
b = a.replace(to_replace=(1,2,3),value=('x','y'))

print(a)
print(b)