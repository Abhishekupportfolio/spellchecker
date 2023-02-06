from tkinter import*
from textblob import TextBlob

def check_spelling():
    a=TextBlob(textbox_check.get())


    spell = Label(window, text="Correct Spelling:", font=("poppins", 20), bg="#dae6f6", fg="#364971")
    spell.place(x=100 ,y=250)


    correct_text = Label(window, text=str(a.correct()).capitalize(), font=("Arial", 20), bg="#dae6f6", fg="#364971")
    correct_text.place(x=350, y=250)








window=Tk()
window.title("My spelling checker")
window.geometry("700x400")
window.config(background="#dae6f6")

text_heading=Label(window,text="Spelling checker App",font=("poppins",20),bg="#dae6f6", fg="#364971")
text_heading.pack(pady=(50,0))



textbox_check=Entry(window,justify="center",width=30,font=("poppins",25),bg="white")

textbox_check.pack(pady=30)
textbox_check.focus()


check_button=Button(window,text="Check!!",font=("arial",20,"bold"),fg="white",bg="red", command=check_spelling)
check_button.pack()



window.mainloop()





