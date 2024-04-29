import tkinter as tk
import tkinter.messagebox as messagebox


def selamla():
    messagebox.showinfo("Senin için bir mesajım var", "Heyy \n Naaberr..")

root = tk.Tk()
root.title("Basit Tkinter Uygulaması")

root.geometry("600x400+500+100") # Genişlik x Yükseklik + X + Y

selamla_buton = tk.Button(root, text="Buton", command=selamla,
                           bg="aqua", fg="red", font=('Helvetica', 15))

selamla_buton.place(x=300 , y=200 ,anchor="center" , width=200, height=55) # butonun konumunu ve boyutunu ayarlar

label = tk.Label(root, text="Asağıdaki butona basma sakın", 
                 font=("Arial", 12), bg="lightblue", fg="black")
label.place(x=300, y=150, anchor="center", width=400, height=50)

root.mainloop()
