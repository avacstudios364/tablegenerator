from tkinter import *
import math
from tkinter.ttk import *

window=Tk()
window.minsize(200,200)
window.title('Table generator')

titlelabel = Label(window, text = 'Mathematical table generator')
titlelabel.grid(row = 1, column = 1)
captionlabel = Label(window, text = 'Number & range')
captionlabel.grid(row = 2, column = 1)


#combo creation
startNumber = IntVar()
NumberInput = Combobox(window, textvariable = startNumber, width = 7)
NumberInput.grid(row = 2, column = 2)

#adding combobox dropdown list
NumberInput['values'] = tuple(range(101))

#Radiobutton
endVal = IntVar()
r10 = Radiobutton(window, text = '10', variable = endVal, value = 10)
r20 = Radiobutton(window, text = '20', variable = endVal, value = 20)
r30 = Radiobutton(window, text = '30', variable = endVal, value = 30)
r40 = Radiobutton(window, text = '40', variable = endVal, value = 40)
r10.grid(row = 3, column = 4)
r20.grid(row = 4, column = 4)
r30.grid(row = 5, column = 4)
r40.grid(row = 6, column = 4)

def generateTable():
    tables = ''
    for i in range(1,endVal.get()+1):
        tables+=str(startNumber.get())+' x '+str(i)+' = '+str(startNumber.get() * i)+'\n'
    tablelabel.configure(text = tables)

tablelabel = Label(window, anchor = 'center')
tablelabel.grid(row = 10, column = 2)

generatebutton = Button(window, text = 'Generate', command = generateTable)
generatebutton.grid(row = 6, column = 2)


window.mainloop()
