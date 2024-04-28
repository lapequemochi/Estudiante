
from Curso import Curso
class Estudiante:
    
    __NOTA_PRUEBA_ACADEMICA =  3.25
    __CANDIDATO_BECA=  4.75

    """-------------
    #Atributos 
    ----------"""
def __init__(self):
    
    self.codigo = 0
    self.nombre = ""
    self.apellido = ""
    self.curso1 = "Fisica"
    self.curso2 = "Sistemas"
    self.curso3 = "Biologia"
    self.curso4 = "Matematicas"
    
    """--------
    #Metodos
    ---------"""
def Codigo(self, pCodigo):
    pCodigo = self.codigo
    pCodigo == 1234
    
def darCurso1(self):
    self.curso1.nota >= 0.0
    
def darCurso2(self):
    self.curso2.departamento == "Matematicas"

def Promedio(self, pCreditosTotales, pPromedio):
    pCreditosTotales = self.creditosTotales
    pCreditosTotales = self.curso1.credito + self.curso2.creditos + self.curso3.creditos + self.curso4.creditos
    pPromedio = self.promedio
    pPromedio = self.curso1 * self.creditos + self.curso2 * self.creditos + self.curso3 * self.creditos + self.curso4 * self.creditos
    return pPromedio/pCreditosTotales

def darNombre(self):
    return self.nombre

def pertenecenMismoDespartamento(self):
    if self.curso > 4:
        return self.curso
    else:
        print("No pertenence al mismo curso")

def calcularPromedioEstudiante(self):
    if self.totalNotas > 0:
        return self.totalNotas/ self.cantidadCalificaciones
    else:
        return 0
    
def buscarCurso(self, pCodigoCurso):
    if self.curso.darCodigo() == pCodigoCurso:
        return Curso
    else:
        return self.null
    
def estaEnPrueba(self):
    if self.calcularPromedio() < 3.25:
        return True
    else:
        return False
