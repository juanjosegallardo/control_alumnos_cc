from google.colab import auth
auth.authenticate_user()
from datetime  import time, datetime
import gspread
from google.auth import default
import pytz
import sys
import re

tz = pytz.timezone('America/Mexico_City')



creds, _ = default()

gc = gspread.authorize(creds)

worksheet = gc.open('Registro de Horas Práctica en CC (respuestas)').sheet1
alumnos = gc.open('Registro de Horas Práctica en CC (respuestas)').worksheet("Alumnos")
horarios = ["7:00:00", "7:50:00" , "8:40:00", "9:30:00", "10:00:00", "10:50:00", "11:40:00",  "12:30:00", "13:20:00", "14:10:00", "15:00:00"]

#print("profesor")
#profesor = input()

print("hora_entrada")

indice = 0
for i in horarios:
  print(indice, " " ,i)
  indice= indice+1

print("Hora entrada: ")
indice_hora_entrada = int(input())
hora_entrada = horarios[indice_hora_entrada]

print("Modulos: ")
modulos= int(input())
hora_salida = horarios[indice_hora_entrada + modulos]

print("Grupo")
grupo = input()

print("Actividad")
actividad = input()

print("Aula")
aula = input()

opciones_si_no = ["No", "si"]

print("Internet 0 No / 1 Si")
indice_internet = input()
internet = opciones_si_no[int(indice_internet)]

no_equipo = 1
equipo =""
while True:

  
  print("No control (Equipo ",no_equipo, "): ")
  matricula = input()



  if(matricula =="X"):
    print("Bye!!!")
    sys.exit()
  

  if(matricula =="C"):
    print("Equipo: ")
    texto_equipo = input()
    no_equipo = int(texto_equipo)
    equipo=""
  else:
    equipo = aula + str(no_equipo)
    
  
  if equipo!="":
    try:
      res =re.findall("[0-9]{14}", matricula)
      cell = alumnos.find(res[0])
      print(res[0])

      nombre= alumnos.cell(cell.row, 2).value
      mexico_now = datetime.now(tz)

    

      worksheet.append_row([
          
          mexico_now.strftime("%d/%m/%Y %H:%M:%S"), #Marca temporal
          nombre ,#Nombre,
          "Alumno", #usuario
          hora_entrada, #Entrada
          hora_salida, #Salida
          grupo , #Grupo"
          equipo, #No Equipo
          actividad, #Actividad
          "No" #Internet 
      ])
      no_equipo = no_equipo+1


    except:
      print("No se encuentra el numero de control")




  
