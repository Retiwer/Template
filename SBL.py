# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:17:39 2017

@author: carlo
"""

import Lib
import Imports
import SBLF
import TT




#----------------------------------INICIO---------------------------------#
#--------------------- Ventana de Interfaz Principal ---------------------#
#-------------------------------------------------------------------------#

top = Tkinter.Tk()
top.minsize(305, 150)
top.geometry( "305x180" )
top.wm_title("Principal")

B_0 = Tkinter.Button(top, text ="Open File"         ,  command = Search_File)
B_1 = Tkinter.Button(top, text ="Select Sheet"      ,  command = Acquire_Sheets)
B_2 = Tkinter.Button(top, text ="Select Variable"   ,  command = Create_Window)
B_3 = Tkinter.Button(top, text ="Create Table"      ,  command = Table)
B_4 = Tkinter.Button(top, text ="Run"               ,  command = Process)
B_5 = Tkinter.Button(top, text ="Create Graph"      ,  command = Dummy)

M_B = [B_0, B_1, B_2, B_3, B_4, B_5]
K = 0

for i in M_B:
    i.pack()
    i.place(x = 0, y = K * 30, height = 30, width = 100)
    K = K + 1
#----------------------------------FINAL----------------------------------#
#--------------------- Ventana de Interfaz Principal ---------------------#
#-------------------------------------------------------------------------#

#
#Inicializaciones
#

Flag_00 = 0
Var_0   = StringVar(top)

#
#Inicializaciones
#

top.mainloop()