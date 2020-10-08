import tkinter

main_window = tkinter.Tk()

print(main_window.__dict__)

label1 = tkinter.Label(main_window, text = "label1")
label1 = tkinter.Label(main_window, text = "label2")

#method positioning
label1.pack()
label2.pack()

main_window.mainloop()