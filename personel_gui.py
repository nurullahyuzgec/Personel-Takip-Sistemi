import os 
import json
import tkinter as tk
from tkinter import ttk

entry_username = None
entry_password = None
login_button = None
data_file = 'personel.json'
admin_user = 'admin'
admin_pass = 'admin'

if not os.path.exists(data_file):
    with open(data_file, "w") as f:
        json.dump([], f)

def login_design():
    global entry_username
    global entry_password
    global login_buton
    window = tk.Tk()
    window.title('Personel Yonetim Sistemi V1')
    window.geometry('500x250')
    window.configure(bg='#f4f6f9')

    # label olusumu
    style = ttk.Style()
    style.configure("TButton",
                    font=("Segoe UI", 12, "bold"),
                    padding=10,
                    relief="flat",
                    background="#5c6bc0",
                    foreground="white")
    style.map("TButton", background=[("active", "#3f51b5")])
    style.configure("TEntry",
                    font=("Segoe UI", 12),
                    padding=5,
                    relief="solid",
                    borderwidth=2)
    style.configure("TLabel",
                    font=("Segoe UI", 14),
                    background="white",
                    foreground="#333")

    label_username = ttk.Label(window, text="Username :")
    label_username.place(x=50, y=50)
    entry_username = ttk.Entry(window, width=25)
    entry_username.place(x=160, y=50)

    label_password = ttk.Label(window, text="Password :")
    label_password.place(x=58, y=100)
    entry_password = ttk.Entry(window, width=25, show="*")
    entry_password.place(x=160, y=100)

    login_buton = ttk.Button(window, text="Login", command=login)
    login_buton.place(x=200, y=170)

    window.mainloop()

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == admin_user and password == admin_pass:
        personel_yonetimi()
    else:
        pass

def personel_yonetimi():
    global entry_pname
    global entry_psurname
    global entry_pdepart
    global entry_ptarih

    personel_window = tk.Toplevel()
    personel_window.title('Admin') # giris yapan yetkisine gore bu title sekillendirilecek.
    personel_window.geometry('450x400')
    personel_window.configure(bg='#e3f2fd')

    # add personel

    style = ttk.Style()
    style.configure("TButton",
                    font=("Segoe UI", 12, "bold"),
                    padding=10,
                    relief="flat",
                    background="#5c6bc0",
                    foreground="white")
    style.map("TButton", background=[("active", "#3f51b5")])
    style.configure("TEntry",
                    font=("Segoe UI", 12),
                    padding=5,
                    relief="solid",
                    borderwidth=2)
    style.configure("TLabel",
                    font=("Segoe UI", 14),
                    background="white",
                    foreground="#333")

    label_pname = ttk.Label(personel_window, text="Personel Adi :")
    label_pname.place(x=49, y=50)
    entry_pname = ttk.Entry(personel_window, width=19)
    entry_pname.place(x=250, y=50)

    label_psurname = ttk.Label(personel_window, text="Personel Soyadi :")
    label_psurname.place(x=49, y=100)
    entry_psurname = ttk.Entry(personel_window, width=19)
    entry_psurname.place(x=250, y=100)

    label_pdepart = ttk.Label(personel_window, text='Personel Departmani : ')
    label_pdepart.place(x=49, y=150)
    entry_pdepart = ttk.Entry(personel_window, width=19)
    entry_pdepart.place(x=250, y=150)

    label_ptarih = ttk.Label(personel_window, text='Tarih (YYYY-MM-DD) :')
    label_ptarih.place(x=49, y=200)
    entry_ptarih = ttk.Entry(personel_window, width=19)
    entry_ptarih.place(x=250, y=200)

    add_personel = ttk.Button(personel_window, text="EKLE", command=add_user, width=40)
    add_personel.place(x=49, y=250)

    list_personal_bt = ttk.Button(personel_window, text='Listele', command=list_user, width=40)
    list_personal_bt.place(x=49, y=320)

def load_data():
    with open(data_file, "r") as f:
        return json.load(f)

def save_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=4)

def add_user():
    personel_name = entry_pname.get()
    personel_surname = entry_psurname.get()
    personel_depart = entry_pdepart.get()
    personel_date = entry_ptarih.get()

    new_personel = {
        'ad': personel_name,
        'soyad': personel_surname,
        'departman': personel_depart,
        'tarih': personel_date
    }

    data = load_data()

    # Aynı personel olup olmadığını kontrol et
    for personal in data:
        if personal['ad'].lower() == personel_name.lower() and personal['soyad'].lower() == personel_surname.lower():
            show_warning_message("Bu personel zaten mevcut!")
            return  

    data.append(new_personel)
    save_data(data)

    success = tk.Toplevel()
    success.geometry('250x80')
    success.configure(bg='white')
    label = ttk.Label(success, text='Başarıyla Eklendi.', font=("Arial", 12))
    label.pack(pady=20)

def show_warning_message(message):
    warning_window = tk.Toplevel()
    warning_window.title("Uyarı")
    warning_window.geometry("250x100")
    warning_window.configure(bg='#f8d7da')

    label = ttk.Label(warning_window, text=message, font=("Arial", 12), foreground="red", background="#f8d7da")
    label.pack(pady=20)

    ok_button = ttk.Button(warning_window, text="Tamam", command=warning_window.destroy, width=10)
    ok_button.place(x=70, y=50)

def list_user():
    list_personal = tk.Toplevel()
    list_personal.title('Personel Listesi')
    list_personal.geometry('800x400')
    list_personal.configure(bg='white')

    search_label = ttk.Label(list_personal, text="Personel Ara:", font=("Arial", 20))
    search_label.place(x=20, y=20)

    search_entry = ttk.Entry(list_personal, font=("Arial", 12), width=50)
    search_entry.place(x=200, y=20)

    def search_personnel():
        search_query = search_entry.get().lower()

        with open(data_file, 'r') as f:
            data = json.load(f)

        filtered_data = [personal for personal in data if search_query in personal['ad'].lower() or search_query in personal['soyad'].lower()]

        for widget in list_personal.winfo_children():
            widget.place_forget()

        search_label.place(x=20, y=20)
        search_entry.place(x=120, y=20)

        if filtered_data:
            for i, personal in enumerate(filtered_data, start=1):
                label_pname = ttk.Label(list_personal, text=f"{i} - Personel Adı: {personal['ad']}", font=("Arial", 12,'bold'))
                label_pname.place(x=49, y=100 + (i - 1) * 100)

                label_sname = ttk.Label(list_personal, text=f"Personel Soyadı: {personal['soyad']}", font=("Arial", 12,'bold'))
                label_sname.place(x=49, y=150 + (i - 1) * 100)

                label_dp = ttk.Label(list_personal, text=f"Personel Departman: {personal['departman']}", font=("Arial", 12,'bold'))
                label_dp.place(x=49, y=200 + (i - 1) * 100)

                label_date = ttk.Label(list_personal, text=f"Personel Tarih: {personal['tarih']}", font=("Arial", 12,'bold'))
                label_date.place(x=49, y=250 + (i - 1) * 100)
        else:
            no_results_label = ttk.Label(list_personal, text="Hiçbir sonuç bulunamadı.", font=("Arial", 12), foreground="red")
            no_results_label.place(x=120, y=100)

    search_button = ttk.Button(list_personal, text="Ara", command=search_personnel)
    search_button.place(x=670, y=15)

    list_personal.mainloop()

login_design()
