from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('600x400')
root.title('Телефоная Книга')
root.config(bg = 'light grey')
root.resizable(0,0)

FILE_CONTACTS = 'contacts.txt'

DataBase = [
    ['Drew', 'DeLeon', '4567891', 'address4', 'drew@deleon.com']
]
class Phone_Book:
    Label(root, text = 'First Name', font = 'arial 12 bold', bg = 'white', fg = 'black').place(x=30, y=70)
    Entry(root, textvariable = FirstName).place (x=130, y=70)
    Label(root, text = 'Last Name', font = 'arial 12 bold', bg = 'white', fg = 'black').place(x=30, y=120)
    Entry(root, textvariable = LastName).place (x=130, y=120)
    Label(root, text = 'Contact Number', font = 'arial 12 bold', bg = 'white', fg = 'black').place(x=30, y=170)
    Entry(root, textvariable = ContactNumber).place (x=130, y=170)
    Label(root, text = 'Address', font = 'arial 12 bold', bg = 'white', fg = 'black').place(x=30, y=220)
    Entry(root, textvariable = Address).place (x=130, y=220)
    Label(root, text = 'Email', font = 'arial 12 bold', bg = 'white', fg = 'black').place(x=30, y=270)
    Entry(root, textvariable = Email).place(x=130, y=270)

    Button(root, text = 'Add Contact', font = 'arial 12 bold', bg = 'white', command = add).place(x=70,y=330)
    Button(root, text = 'Delete', font = 'arial 12 bold', bg = 'white', command = delete_contact).place(x=290,y=280)
    Button(root, text = 'Exit', font = 'arial 12 bold', bg = 'red', command = exit).place(x=500,y=350)
    Button(root, text = 'Sort', font = 'arial 12 bold', bg = 'white', command = sort).place(x=450,y=300)


    def load_contacts(self):
        """Загрузить контакты из файла"""
        try:
            with open('contacts.txt', 'r') as file:
                for line in file:
                    contact_data = line.strip().split(':')
                    if len(contact_data) == 5:
                        select.insert(END,
                                f"{contact_data[0]} {contact_data[1]}")
        except FileNotFoundError:
            print(f"файл не найден, проверьте наличие файла -{FILE_CONTACTS}")
            pass
    
    def save_contact(contact):
        """Сохранить контакт в файл"""
        try:
            with open(FILE_CONTACTS, 'a') as file:
                file .write(f"{contact['firstname']};{contact['lastname']};{contact['email']};"
                f"{contact['phone_number']};{contact['address']}\n")
        except FileNotFoundError:
            print(f"файл не найден, проверьте наличие файла - {FILE_CONTACTS}")
            pass          

    def add_contact():
        """Добавить новый контакт"""
        contact = {
            'firstname':FirstName.get(),
            'lastname':LastName.get(),
            'email':Email.get(),
            'Contact_Number':Contact_Number.get(),
            'address':Address.get(),
        }
        save_contact(contact)
        select.insert(END, f"{contact['firstname']} {contact['lastname']}")
        messagebox.showinfo("Успех!", "Контакт добавлен успешно!")

    def delete_contact_from_file(first_name, last_name, contact_number):
        """Удалить файл из контакта"""
        contacts = []
        with open(FILE_CONTACTS, 'r') as file:
            for line in file:
                contact_data = line.strip().split(';')
                if contact_data[0] == first_name and contact_data[2]==contact_number:
                    continue
                contacts.append(line)
        with open(FILE_CONTACTS, 'w') as file:
            file.writelines

    def delete_contact():
        """Удалить контакт"""
        selection = select.curselection()
        if not selection:
            messagebox.showerror("Ошибка", "Не выбран не один контакт.")
            return
        index = selection[0]
        contact = select.get(index)
        answer = messagebox.askyesno("Подтверждение",f"Точно хотите удалить контакту?'{contact}'")

        if answer:
            select.delete(index)
            delete_contact_from_file(contact.split(' ')[0], contact.split(' ')[1])
            messagebox.showinfo("Успех!", "Контакт успешно удалён!")

    def exit():
        root.destroy()

    def selected():
        return int(select.curselection()[0])

    def add():
        DataBase.append([FirstName.get(),LastName.get(),ContactNumber.get(), 
        Address.get(), Email.get()])
        print('Contact added')
        selectset()
        print(f"Contact added.")

    def sort():
        pass

    def delete():
        del DataBase[selected()]
        selectset()
    
    def selectset():
        pass

FirstName = StringVar()
LastName = StringVar()
ContactNumber = StringVar()
Address = StringVar()
Email = StringVar()

frame = Frame(root)
frame.pack (side = RIGHT)

scroll = Scrollbar(frame, orient = VERTICAL)
select = Listbox(frame,yscrollcommand = scroll.set,height =15,)
scroll.config(command = select.yview)
scroll.pack(side = RIGHT, fill = Y)
select.pack(side = LEFT, fill = BOTH, expand = 1)

Label(root, text = 'First Name', font = 'arial 12 bold', bg = 'white', fg = 'black').place(x=30, y=70)
Entry(root, textvariable = FirstName).place (x=130, y=70)
Label(root, text = 'Last Name', font = 'arial 12 bold', bg = 'white', fg = 'black').place(x=30, y=120)
Entry(root, textvariable = LastName).place (x=130, y=120)
Label(root, text = 'Contact Number', font = 'arial 12 bold', bg = 'white', fg = 'black').place(x=30, y=170)
Entry(root, textvariable = ContactNumber).place (x=130, y=170)
Label(root, text = 'Address', font = 'arial 12 bold', bg = 'white', fg = 'black').place(x=30, y=220)
Entry(root, textvariable = Address).place (x=130, y=220)
Label(root, text = 'Email', font = 'arial 12 bold', bg = 'white', fg = 'black').place(x=30, y=270)
Entry(root, textvariable = Email).place(x=130, y=270)

Button(root, text = 'Add Contact', font = 'arial 12 bold', bg = 'white', command = add).place(x=70,y=330)
Button(root, text = 'Delete', font = 'arial 12 bold', bg = 'white', command = delete_contact).place(x=290,y=280)
Button(root, text = 'Exit', font = 'arial 12 bold', bg = 'red', command = exit).place(x=500,y=350)
Button(root, text = 'Sort', font = 'arial 12 bold', bg = 'white', command = sort).place(x=450,y=300)

root.mainloop()