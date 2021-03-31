from tkinter import Tk, messagebox, simpledialog

a = Tk()
a.iconbitmap('images/icon.ico')
a.withdraw()

world = {}

data="data/data.txt"

with open(data, "r",  encoding="utf8") as f:
    for line in f:
        line = line.rstrip('\n')
        country, city = line.split('/')
        world[country] = city
f.close()

while True:
    answer=simpledialog.askstring("Страна", "Введите название страны:")
    answer = answer.lower()

    if answer=='стоп' or answer=='stop':
        break
    else:
        country=answer.capitalize()
        if country in world:
            messagebox.showinfo("Ответ", f'{country}: столица этой страны - {world[country]}')
        else:
            ans=simpledialog.askstring("Научите меня",f"Я не знаю, как называется столица страны {country}")
            world[country]=ans
            with open(data,"a",encoding='utf8') as f:
                f.write(f'\n{country}/{ans}')
            f.close()

a.mainloop()
