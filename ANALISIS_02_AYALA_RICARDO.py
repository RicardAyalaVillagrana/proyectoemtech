# Programar la extración de la información 
import xlrd 

myDataFile = ("synergy_logistics_database.xlsx") 
  
wb = xlrd.open_workbook(myDataFile) 
sheet = wb.sheet_by_index(0) 
export = "export"

sheet.cell_value(0, 0)  
two_d_array = []
export_array = []
final = []
totalSumValue = 0
#Rutas de importacion y exportacion 
class ImportExport:
    bizType = ""
    origin = ""
    destination = ""
    exportCount = 0
    totalBusinessValue = 0
    def __eq__(self, other):
      return self.origin==other.origin and self.destination==other.destination and self.bizType == other.bizType
    def __ne__(self, other):
      return not self.__eq__(other)
    def __hash__(self):
      return hash((self.bizType, self.origin, self.destination))
    def __lt__(self, other):
       return self.exportCount < other.exportCount

#Valor de las rutas de importacion y exportación
i = 1;
while i < sheet.nrows-1: 
  if sheet.cell(i,1).value == "Exports":
    currentEObject = ImportExport()
    currentEObject.bizType = "Exports"
    currentEObject.exportCount = 1
    currentEObject.origin = sheet.cell(i,2).value
    currentEObject.destination = sheet.cell(i,3).value
    currentEObject.totalBusinessValue = sheet.cell(i,9).value
    while sheet.cell(i,2).value == sheet.cell(i+1,2).value and sheet.cell(i,3).value == sheet.cell(i+1,3).value:
      currentEObject.exportCount = currentEObject.exportCount +1
      currentEObject.totalBusinessValue = currentEObject.totalBusinessValue + sheet.cell(i,9).value
      i = i+1 
    two_d_array.append(currentEObject) 
  elif sheet.cell(i,1).value == "Imports" and i < sheet.nrows-4:
    currentIObject = ImportExport()
    currentIObject.bizType = "Imports"
    currentIObject.exportCount = 1
    currentIObject.origin = sheet.cell(i,2).value
    currentIObject.destination = sheet.cell(i,3).value
    currentIObject.totalBusinessValue = sheet.cell(i,9).value
    while sheet.cell(i,2).value == sheet.cell(i+1,2).value and sheet.cell(i,3).value == sheet.cell(i+1,3).value:
      currentIObject.exportCount = currentIObject.exportCount +1
      currentIObject.totalBusinessValue = currentIObject.totalBusinessValue + sheet.cell(i,9).value
      i = i+1 
    two_d_array.append(currentIObject) 
  i+=1

output = set()
newExportCount = 0
newBusinessValue = 0
for k in range(len(two_d_array)):
  l = k+1
  while l < len(two_d_array):
    if two_d_array[k].bizType == two_d_array[l].bizType and two_d_array[k].origin == two_d_array[l].origin and two_d_array[k].destination ==two_d_array[l].destination:
      newExportCount = newExportCount + two_d_array[l].exportCount
      newBusinessValue = newBusinessValue + two_d_array[l].totalBusinessValue
    l+= 1
  two_d_array[k].totalBusinessValue = two_d_array[k].totalBusinessValue + newBusinessValue
  two_d_array[k].exportCount = two_d_array[k].exportCount + newExportCount
  output.add(two_d_array[k])

#for j in range(len(two_d_array)-10):
#  print(two_d_array[j].bizType, two_d_array[j].origin, two_d_array[j].destination, #two_d_array[j].exportCount, two_d_array[j].totalBusinessValue)

for each in output:
  final.append(each)

final.sort()

i = len(final)-1

print("OPCION - 1")
print("Las 10 rutas de importación y exportación más importantes se enumeran a continuación según el valor total y el número total de importaciones / exportaciones.")
print("----------------------------------------------------------------------------------------")

while i > len(final)-11:
  each = final[i]
  print(each.bizType, each.origin, each.destination, each.exportCount, each.totalBusinessValue)
  i-=1;

print("----------------------------------------------------------------------------------------")

print("OPCION - 2")
#Se valoran las rutas mas importantes
i = 1;
airValue = 0
seaValue = 0
roadValue = 0
railValue = 0
airCount = 0
seaCount = 0
roadCount = 0
railCount = 0
while i < sheet.nrows-1: 
  if sheet.cell(i,7).value == "Sea":
    seaValue+= sheet.cell(i,9).value
    seaCount+=1
  if sheet.cell(i,7).value == "Air":
    airValue+= sheet.cell(i,9).value
    airCount+=1
  if sheet.cell(i,7).value == "Road":
    roadValue+= sheet.cell(i,9).value
    roadCount+=1
  if sheet.cell(i,7).value == "Rail":
    railValue+= sheet.cell(i,9).value
    railCount+=1
  i = i+1

seaValuePerTranspot = seaValue/seaCount
airValuePerTranspot = airValue/airCount
roadValuePerTranspot = roadValue/roadCount
railValuePerTranspot = railValue/railCount

if railValuePerTranspot < roadValuePerTranspot and railValuePerTranspot < airValuePerTranspot and railValuePerTranspot > seaValuePerTranspot:
  print("3 rutas importantes son : " +"SEA, AIR, ROAD")

elif roadValuePerTranspot< railValuePerTranspot and roadValuePerTranspot < airValuePerTranspot and roadValuePerTranspot > seaValuePerTranspot:
  print("3 rutas importantes son : " +"RAIL, SEA, AIR")

elif airValuePerTranspot< railValuePerTranspot and airValuePerTranspot < seaValuePerTranspot and airValuePerTranspot > roadValuePerTranspot:
  print("3 rutas importantes son : " +"RAIL, SEA, ROAD")

else:
  print("Las 3 tres rutas mas importantes son : " +"RAIL, AIR, ROAD")

print("----------------------------------------------------------------------------------------") 
print("OPCION - 3")
#Cuantificar el valor total de importaciones y exportaciones
i=1
new_array = []
totalSumValue+= sheet.cell(sheet.nrows-1,9).value #Valor para sumar
while i < sheet.nrows-1: 
  totalSumValue+= sheet.cell(i,9).value
  currentEObject = ImportExport()
  currentEObject.origin = sheet.cell(i,2).value
  currentEObject.totalBusinessValue = sheet.cell(i,9).value
  while sheet.cell(i,2).value == sheet.cell(i+1,2).value and i < sheet.nrows-4:
    totalSumValue+= sheet.cell(i+1,9).value
    currentEObject.totalBusinessValue+= sheet.cell(i+1,9).value
    i+= 1
  new_array.append(currentEObject)
  i+=1

new_set = set() #Eliminar valores duplicados 

i = 0
for i in range(len(new_array)):
  j = i+1
  for j in range(len(new_array)):
    if new_array[i].origin == new_array[j].origin:
      new_array[i].totalBusinessValue+=new_array[j].totalBusinessValue
  new_set.add(new_array[i])

print("El valor total de importación y exportación de la empresa es : ")
print(totalSumValue)
print("Lista de países / Rutas que representan más del 80% del valor total de la empresa : ")

for val in new_set:
  #print(new_array[i].origin, new_array[i].totalBusinessValue)
  if val.totalBusinessValue > totalSumValue * (0.08):
    print(val.origin, val.totalBusinessValue)

print("----------------------------------------------------------------------------------------")
print("Finalizar")