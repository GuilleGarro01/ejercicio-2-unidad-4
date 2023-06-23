from tkinter import *
from tkinter import ttk, font

class Calcula():
    __ventana=None
    __precioBase=None
    __precioiva=None

    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry('400x400')
        self.__ventana.title('Cálculo de IVA') #Nombre-titulo de la ventana
        self.__ventana.configure(bg='white')
        self.iva=StringVar()
        opts= {'ipadx': 500, 'ipady':10} 
        
        '''las propiedades 'padx' y 'pady'
        se utilizan para añadir espacio extra externo
        horizontal y/o vertical a los widgets para
        separarlos entre sí y de los bordes de la
        ventana. Hay otras equivalentes que añaden
        espacio extra interno: 'ipadx' y 'ipady':'''
        
              
        ttk.Label(self.__ventana,text='Calculo de IVA', background='yellow').place(width=400,height=40)
        style= ttk.Style()
        style.configure("Red.TButton",background="red")
        
        ttk.Button(self.__ventana,text='Salir',style="Red.TButton",command=self.__ventana.destroy).place(x=260, y=330)
        style1= ttk.Style()
        style1.configure("Green.TButton",background="green")
        ttk.Button(self.__ventana,text="Calcular",style="Green.TButton",command=self.calcular).place(x=70, y=330)
        
        ttk.Label(self.__ventana, text='Precio sin IVA ').place(x=100,y=140)
        self.__precioBase=DoubleVar()
        self.__precioiva=DoubleVar()
        ttk.Entry(self.__ventana,textvariable=self.__precioBase).place(x=250,y=140)
        
        seleccionar=ttk.LabelFrame(self.__ventana,text='Seleccion el IVA del producto').place(x=100,y=200)
        ttk.Radiobutton(seleccionar,text="IVA 21%", value=21, variable=self.iva).place(x=100,y=220)
        ttk.Radiobutton(seleccionar,text="IVA 10,5%", value=10.5, variable=self.iva).place(x=100,y=240)
        ttk.Label(self.__ventana,text="Precio con IVA: ").place(x=100, y=270)
        ttk.Label(self.__ventana,textvariable=self.__precioiva).place(x=190, y=270)
        
        self.__ventana.mainloop()

        
    def calcular(self):
        valor=float(self.__precioBase.get())
        iva=float(self.iva.get())
        valor*=iva/100
        self.__precioiva.set(valor+self.__precioBase.get())
              
        
def testAPP():
    mi_app=Calcula()
    return 0
if __name__=='__main__':
    mi_app=Calcula()
    