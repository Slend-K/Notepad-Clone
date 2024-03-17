import tkinter as Tk
from tkinter.filedialog import asksaveasfile, askopenfile

def savefile():
    filetypes = [('Text Document', '*.txt'),
             ('All Files', '*.*')] 
    file = asksaveasfile(filetypes = filetypes, defaultextension = filetypes)

    if file:
        try:
            txt_to_write = text_box.get("1.0", "end-1c")
            file.write(txt_to_write)
            file.close()
            successwindow = Tk.Tk();                successwindow.geometry("1000x40");                successwindow.title("Notepad: File saved successfully");                successwindow.resizable(True, False);                successtext = Tk.Label(successwindow, text=f"File saved successfully!\nPath: {file.name}");                successtext.pack();                successwindow.mainloop() # FUN FACT: Python does use semicolons! They're used to represent a line break :)
        except Exception as e:
            print(f"Error whilst saving file:\n{str(e)}")                                                                                                                                                                                                                                                                                                                                                 # They can be used like this to avoid wasting lines. Wow.
            failwindow = Tk.Tk();                failwindow.geometry("500x40");                failwindow.title("Notepad: Error saving file");                failwindow.resizable(True, True);                failwindow.maxsize(500,500);                failtext = Tk.Label(failwindow, text=f"An error occurred whilst trying to save the file!\nError: {str(e)}");                failtext.pack();                failwindow.mainloop() # FUN FACT: Python does use semicolons! They're used to represent a line break :)

def openfile():
    file = askopenfile(mode ='r', filetypes =[('Text Documents', '*.txt'),
        ('All Files', '*.*')])
    if file is not None:
        content = file.read()
    
    text_box.delete("1.0", Tk.END)
    text_box.insert(Tk.END, content)


window = Tk.Tk()
window.geometry("500x300")
window.minsize(250,50)
window.title("Notepad")
scrollbar = Tk.Scrollbar(window) # This needs fixing; it doesn't work. Not massively important though because the scroll wheel/two fingers on touchpad still works fine.
scrollbar.pack(side=Tk.RIGHT, fill=Tk.Y)

text_box = Tk.Text(window)


save_button = Tk.Button(window, text="Save", command=lambda:savefile())
save_button.pack(side=Tk.TOP) # Whilst not important, work on getting all these buttons on the top left like in the real notepad.exe
open_button = Tk.Button(window, text="Open", command=lambda:openfile())
open_button.pack(side=Tk.TOP)

text_box.pack(fill=Tk.BOTH, expand=True) # At the bottom so everything is placed above it.

# Everything above this, of course.
window.mainloop()