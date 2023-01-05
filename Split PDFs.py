import customtkinter
import time
from tkinter import messagebox
from PyPDF2 import PdfReader, PdfWriter


TEXT_EPLANATION1 = "Split the PDF to couples"
TEXT_EPLANATION2 = "Enter the path of the PDF file(PDF only)"
TEXT_EPLANATION3 = "Choose the path where the PDF files will be saved in"
ERROR = "Please reenter a valid PDF file and a valid folder path"
TITLE = "Split PDFs"
PATH_LABEL = "Path selected: "
OPEN_FILE_TEXT = "Choose PDF file"
WHERE_TO_SAVE = "Choose folder"
START = "Start!"

path_selected = "Not Selected"
folder_selected = "Not Selected"

def open_pdf_file():
    global path_selected

    path_selected = customtkinter.filedialog.askopenfilename(title=OPEN_FILE_TEXT, initialdir='/',  filetypes=[('pdf file', '*.pdf')])
    label_path = customtkinter.CTkLabel(master=frame, text=PATH_LABEL + path_selected, font=("Calibri", 10))
    label_path.place(relx=0.5, rely=0.47, anchor='center')


def select_folder():
    global folder_selected

    folder_selected = customtkinter.filedialog.askdirectory()
    label_folder = customtkinter.CTkLabel(master=frame, text=PATH_LABEL + folder_selected, font=("Calibri", 10))
    label_folder.place(relx=0.5, rely=0.74, anchor='center')

def make_diplomot():
    global path_selected
    global folder_selected
    
    if ":" not in path_selected:
        messagebox.showwarning(title="Warning", message=ERROR)
        folder_selected = "Not Selected"
        return
    
    elif ":" not in folder_selected:
        messagebox.showwarning(title="Warning", message=ERROR)
        path_selected = "Not Selected"
        return

    i = 0
    j = 1
    counter = 1

    pdf_file = open(path_selected, 'rb')
    pdf_reader = PdfReader(pdf_file)

    for page in range(len(pdf_reader.pages)//2):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[i])
        pdf_writer.add_page(pdf_reader.pages[j])
        split_file = open(folder_selected + f"/PDF_{counter}.pdf", 'wb')
        pdf_writer.write(split_file)
        split_file.close()

        i += 2
        j += 2
        counter += 1

    pdf_file.close()
    time.sleep(3)
    exit()

customtkinter.set_appearance_mode("white")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("700x350")
root.resizable(width=False, height=False)
root.title(TITLE)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

label_title = customtkinter.CTkLabel(master=frame, text=TEXT_EPLANATION1, font=("Calibri", 26))
label_title.place(relx=0.5, rely=0.1, anchor='center')

label_first_file = customtkinter.CTkLabel(master=frame, text=TEXT_EPLANATION2, font=("Calibri", 16))
label_first_file.place(relx=0.5, rely=0.3, anchor='center')

open_button_first = customtkinter.CTkButton(root, text=OPEN_FILE_TEXT, command=open_pdf_file)
open_button_first.place(relx=0.5, rely=0.4, anchor='center')

label_path = customtkinter.CTkLabel(master=frame, text=PATH_LABEL+path_selected, font=("Calibri", 10))
label_path.place(relx=0.5, rely=0.47, anchor='center')

label_second_file = customtkinter.CTkLabel(master=frame, text=TEXT_EPLANATION3, font=("Calibri", 16))
label_second_file.place(relx=0.5, rely=0.55, anchor='center')

open_button_second = customtkinter.CTkButton(root, text=WHERE_TO_SAVE, command=select_folder)
open_button_second.place(relx=0.5, rely=0.65, anchor='center')

label_folder = customtkinter.CTkLabel(master=frame, text=PATH_LABEL+folder_selected, font=("Calibri", 10))
label_folder.place(relx=0.5, rely=0.74, anchor='center')

start_button_second = customtkinter.CTkButton(root, text=START, fg_color='green', command=make_diplomot)
start_button_second.place(relx=0.5, rely=0.9, anchor='center')


root.mainloop()
