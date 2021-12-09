from tkinter import Tk, Canvas, Label, Button, StringVar, Text
from tkinter.filedialog import askopenfile
import PyPDF2
from PIL import Image, ImageTk

root = Tk()
root.title('Extract PDF - tkinter')

canvas = Canvas(root, width=800, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label['image'] = logo
logo_label.grid(row=0, column=1)

# Instructions
instructions = Label(root, text='Select a PDF file on your computer to  extract all its text', font='Noto_Serif')
instructions.grid(row=1, column=0, columnspan=3)

def open_file():
    browse_text.set('loading...')
    file = askopenfile(parent=root, mode='rb', title='Choose a file', filetypes=[('PDF file', '*.pdf')])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        # print(page_content)

        # Text box
        text_box = Text(root, height=5, width=50, padx=15, pady=15, font='Noto_Serif')
        text_box.insert(1.0, page_content)
        text_box.tag_configure('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(row=3, column=1)
    browse_text.set('Browse')

# Browse Button
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=open_file, font='Noto_Serif', bg='#FF8C00', fg='white', height=1, width=10)
browse_text.set('Browse')
browse_btn.grid(row=2, column=1)

canvas = Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
