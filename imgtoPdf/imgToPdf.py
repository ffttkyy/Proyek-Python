import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

#function to convert images to pdf
def images_to_pdf(images, pdf_name):
    try:
        #create a new pdf file
        pdf = Image.open(images[0])
        pdf.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
        messagebox.showinfo("Bagoodss", "Photo suksees convert ke pdf")
    except Exception as e:
        messagebox.showerror("Errrooorrrrrr wooiii, gagal kan jadinyaa")

#function to select images
def select_images():
    images = filedialog.askopenfilenames(title="Pilih Photo", filetypes=(("File Photo", "*.jpg;*.jpeg;*.png"),("All files", "*.*")), initialdir = "C:/")
    return images
#function to select pdf and path
def select_pdf():
    pdf = filedialog.askopenfilename(title="Save PDF As", defaultextension=".pdf", initialdir = "C:/", filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))
    return pdf
#Create GUI
root = tk.Tk()
root.title("Convert Images to PDF")
select_images_btn = tk.Button(root, text="Select Images", command=select_images)
select_pdf_btn = tk.Button(root, text="Pilih PDF", command=select_pdf)
convert_btn = tk.Button(root, text="Convert", command=lambda: images_to_pdf(select_images(), select_pdf()))
select_images_btn.pack()
select_pdf_btn.pack()
convert_btn.pack()
root.mainloop()
