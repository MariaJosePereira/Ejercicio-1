
# Online Python - IDE, Editor, Compiler, Interpreter
"""Ejercicio 1"""

print("Escuela de Ingeniería de Geología, Minas y Geofísica")
print("******************************************************")


measure=""
days=0
max=[]
min=[]
errors=0
final_data=[]

print(',' not in measure)

while measure!="0,0":
    measure = input("Enter the measure in shape x,y: ")
    if "," in measure:
        measureaux=measure.split(",")
        max_day=measureaux[0]
        min_day=measureaux[1]
        
        if int(max_day)>50 or int(min_day)<0:
            errors+=1
            days+=1
            
        else:
            min.append(min_day)
            max.append(max_day)
            days+=1 
    else: measure = input("Enter the measure in shape x,y: ")

for i in range(len(max)-1):
    final_data.append(f"days{i+1} max_measure: ({max[i]}), min_measure: ({min[i]})")
    
print(final_data,errors)

True or False