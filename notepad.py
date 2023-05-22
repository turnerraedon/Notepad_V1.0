#import tkinter module 
import tkinter as tk

#create the main window
root = tk.Tk()
root.title("Notepad")

#create textbox
text_box = tk.Text(root)
text_box.pack()

#create a menu bar with File and Edit options
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=lambda: open_file(text_box))
file_menu.add_command(label="Save", command=lambda: save_file(text_box))
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Copy", command=lambda: copy(root))
edit_menu.add_command(label="Cut", command=lambda: cut(root))
edit_menu.add_command(label="Paste", command=lambda: paste(root))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

#add the menu bar to the root window
root.config(menu=menu_bar)

#function to open a file
def open_file(text_box):
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
    if file_path == "": #if no file is selected
        file_path = None
    else:
        root.title(os.path.basename(file_path) + "- Notepad") #update the title of root window
        text_box.delete(1.0,tk.END)
        with open(file_path,"r") as f:
            text_box.insert(1.0,f.read())

#function to save the file       
def save_file(text_box):
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
    if file is None: #if no file is selected
        return
    else:
        data = text_box.get(1.0,tk.END)
        file.write(data)
        file.close()

#function to copy from textbox
def copy(root):
    root.clipboard_clear()
    root.clipboard_append(text_box.selection_get())
    
#function to cut from textbox    
def cut(root):
    root.clipboard_clear()
    data = text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
    root.clipboard_append(data)
    text_box.delete(tk.SEL_FIRST, tk.SEL_LAST)
    
#function to paste into textbox
def paste(root):
    text_box.insert('insert', root.clipboard_get())

#run the main loop
root.mainloop()
