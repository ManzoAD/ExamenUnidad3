from crudmysql import MySQL
from env import variables
import json
def datosAlumno():
    dicci_estu={}
    print("<----- Datos estudiantes ----->")
    nc= input("Ingresa NC°: ")
    objEstu = MySQL(variables)
    objEstu.myConexionSQL()
    consulta_estudiante=f"Select nombre from estudiantes where ctrl='{nc}';"
    consulta_materias=f"Select materia , calificacion from kardex where ctrl = '{nc}';"
    nom_estu= objEstu.consulta(consulta_estudiante)
    mate_estu= objEstu.consulta(consulta_materias)
    objEstu.desconectar_mysql()
    if nom_estu:
        dicci_estu["nombre"]= nom_estu[0][0]
        if mate_estu:
            listaMat=[]
            for i in mate_estu:
                dicci_mat={}
                dicci_mat["materia"]=i[0]
                dicci_mat["calificacion"]=str(i[1])
                listaMat.append(dicci_mat)

            dicci_estu["materias"]=listaMat
        else:
            dicci_estu["nombre"]= nom_estu[0][0]
            dicci_estu["materias"]=""
    else:
        dicci_estu["nombre"]="estudiante no encontrado"
        dicci_estu["materias"]=""
    return json.dumps(dicci_estu)

print(datosAlumno())
