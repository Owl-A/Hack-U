import Tkinter, time

to = Tkinter.Tk()
to.geometry('{}x{}'.format(100, 100))
time.sleep(2)
to.geometry('{}x{}'.format(200, 200))
to.mainloop()