#importacion de clase QtWidgets de libreria PyQt5
from PyQt5 import QtWidgets
# Importacion paquete sys
import sys
# Importacion la ventana generada con QtDesigner5 como clase
from interfaz import Ui_ventanaPrincipal

class Ui_ventanaPrincipal(QtWidgets.QMainWindow, Ui_ventanaPrincipal):
    '''
    Clase herada que representa la ventana de interfaz grafica

    Attributos
    ----------
    por defectos el mismo ya que es una clase heredada

    Methodos
    -------
	__init__(self, *args, **kwargs):
		Construye evenetos y acciones de la ventana principal
    
    '''
    def __init__(self, *args, **kwargs):
        '''
		
        Construye la venta dando acciones a elementos.

        Parametros
        ----------
        None

        Returno
        -------
        None
        
        '''
        # Inicializar ventana principal
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # Construir ventana con estructura base
        self.setupUi(self) 


#Correr programa si este es la raiz de ejecucion
if __name__ == "__main__":
    # Evento de cierre de la ventana tomanod ruta de archivo ejecutado con sys
    app = QtWidgets.QApplication(sys.argv)
    # Crear objeto tipo ventana principal a partir de QtWidgets
    ventana = QtWidgets.QMainWindow()
    # Crear objeto ventana de la clase generada
    ventana_principal = Ui_ventanaPrincipal()
    # Instanciar el objecto de la clase generada con el objeto de tipo ventana principal
    ventana_principal.setupUi(ventana)
    # Mostrar ventana principal
    ventana.show()
    # Dar evento de fin de programa al cerrar ventana
    sys.exit(app.exec_())