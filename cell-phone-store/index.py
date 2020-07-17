import tkinter as tk

def makeForm(app, fields, type):
    if type == "submit":
        entries = []
        for field in fields:
            row = tk.Frame(app)
            lab = tk.Label(row, width=15, text=changeLable(field), anchor='e')
            ent = tk.Entry(row, width=40)
            row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
            lab.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            ent.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
            entries.append([field, ent])
        return entries
    elif type == "search":
        row = tk.Frame(app)
        searchBy = tk.StringVar(row)
        searchBy.set(changeLable(fields[0]))  # default value
        choose = []
        for f in fields:
            choose.append(changeLable(f))
        menu = tk.OptionMenu(row, searchBy, *choose)
        menu.config(width=17)
        ent = tk.Entry(row, width=40)
        row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        menu.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        ent.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        return [searchBy, ent]

def changeLable(en):
    if en == "name":
        return ":نام گوشی"
    elif en == "price":
        return ":قیمت"
    elif en == "brand":
        return ":شرکت سازنده"
    elif en == "color":
        return ":رنگ"
    elif en == "size":
        return ":اندازه"
    elif en == "existent":
        return ":وضعیت موجود بودن"

def changeFilter(per):
    if per == ":نام گوشی":
        return "name"
    elif per == ":قیمت":
        return "price"
    elif per == ":وضعیت موجود بودن":
        return "existent"

def show():
    top = tk.Toplevel()
    for product in shop:
        row = tk.Frame(top)
        text = "%s : %s" % (product, shop[product])
        message = tk.Label(row, text=text)
        row.pack(side=tk.TOP, fill=tk.X)
        message.pack(padx=5, pady=5, side=tk.LEFT)


def save(entries):
    top = tk.Toplevel()
    top.title("لیست به روز محصولات فروشگاه")

    if entries[0][1].get() in shop:
        error = tk.Label(top, text=".گوشی مورد نظر در فروشگاه موجود میباشد")
        error.config(bg='red3', fg='white')
        error.pack(padx=3, pady=5, side=tk.TOP, expand=tk.YES)
    else:
        details = {}
        for i in range(1,6):
            if entries[i][0] == "price":
                details[entries[i][0]] = int(entries[i][1].get())
            elif entries[i][0] == "existent":
                details[entries[i][0]] = eval(entries[i][1].get())
            else:
                details[entries[i][0]] = entries[i][1].get()
        shop[entries[0][1].get()] = details

    for product in shop:
        row = tk.Frame(top)
        text = "%s : %s" %(product, shop[product])
        message = tk.Label(row, text=text)
        row.pack(side=tk.TOP, fill=tk.X)
        message.pack(padx=5, pady=5, side=tk.LEFT)
    # print(shop)
    return shop

def search(option):
    filter = changeFilter(option[0].get())
    detail = option[1].get()
    print('%s: "%s"' % (filter, detail))
    flag = False

    top = tk.Toplevel()
    top.title("نتیجه جست و جو در فروشگاه")

    if filter == "name":
        if detail in shop:
            # print('%s: %s' % (detail, shop[detail]))
            row = tk.Frame(top)
            text = "%s : %s" % (detail, shop[detail])
            message = tk.Label(row, text=text)
            row.pack(side=tk.TOP, fill=tk.X)
            message.pack(padx=3, pady=5, side=tk.LEFT, expand=tk.YES)
            flag = True

    elif filter == "price":
        detail = float(detail)
        for product in shop:
            description = shop[product]
            if detail >= description["price"]:
                # print('%s: %s' % (product, shop[product]))
                row = tk.Frame(top)
                text = "%s : %s" % (product, shop[product])
                message = tk.Label(row, text=text)
                row.pack(side=tk.TOP, fill=tk.X)
                message.pack(padx=3, pady=5, side=tk.LEFT, expand=tk.YES)
                flag = True

    elif filter == "existent":
        detail = eval(detail)
        if detail:
            for product in shop:
                description = shop[product]
                if description["existent"]:
                    # print('%s: %s' % (product, shop[product]))
                    row = tk.Frame(top)
                    text = "%s : %s" % (product, shop[product])
                    message = tk.Label(row, text=text)
                    row.pack(side=tk.TOP, fill=tk.X)
                    message.pack(padx=3, pady=5, side=tk.LEFT, expand=tk.YES)
                    flag = True
        else:
            for product in shop:
                description = shop[product]
                if not description["existent"]:
                    # print('%s: %s' % (product, shop[product]))
                    row = tk.Frame(top)
                    text = "%s : %s" % (product, shop[product])
                    message = tk.Label(row, text=text)
                    row.pack(side=tk.TOP, fill=tk.X)
                    message.pack(padx=3, pady=5, side=tk.LEFT, expand=tk.YES)
                    flag = True

    if flag:
        return
    else:
        # print("NOT FOUND!")
        error = tk.Message(top, text=".یافت نشد")
        error.config(bg='red3', fg='white')
        error.pack(padx=3, pady=5, side=tk.TOP, expand=tk.YES)


if __name__ == '__main__':
    app = tk.Tk()
    app.title("فروشگاه موبایل")

    shop = {"A5": {"price": 100, "brand": "Sumsung", "color": "gold", "size": "6.4", "existent": True},
            "S5": {"price": 200, "brand": "Sumsung", "color": "black", "size": "6.4", "existent": False},
            "J5": {"price": 300, "brand": "Sumsung", "color": "white", "size": "6.4", "existent": True},
            "A20": {"price": 500, "brand": "Sumsung", "color": "black", "size": "6.4", "existent": False}}


    # for show the shop
    row0 = tk.Frame(app)
    lab0 = tk.Label(row0, text="مشاهده اجناس فروشگاه")
    lab0.config(bg='RoyalBlue4', fg='white')
    msg = tk.Label(row0, text=".به فروشگاه موبایل خوش آمدید. برای مشاهده اجناس موجود کلیک کنید", width=50)
    row0.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    lab0.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)
    msg.pack(padx=3, pady=5, side=tk.RIGHT, expand=tk.YES,fill=tk.Y)
    r0 = tk.Frame(app)
    b0 = tk.Button(r0, text='فروشگاه', command=(lambda: show()))
    b0.config(bg='RoyalBlue1', width=10)
    r0.pack(side=tk.TOP, fill=tk.X, padx=1, pady=1)
    b0.pack(side=tk.LEFT, padx=5, pady=5)


    # for add new cell phone
    row1 = tk.Frame(app)
    lab1 = tk.Label(row1, text="افزودن گوشی جدید")
    lab1.config(bg='RoyalBlue4', fg='white')
    row1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    lab1.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    fields = ['name', 'price', 'brand', 'color', 'size', 'existent']
    entries = makeForm(app, fields, "submit")
    row1.bind('<Return>', (lambda event, e=entries: save(e)))
    r1 = tk.Frame(app)
    b1 = tk.Button(r1, text='ذخیره', command=(lambda e=entries: save(e)))
    b1.config(bg='RoyalBlue1', width=10)
    r1.pack(side=tk.TOP, fill=tk.X, padx=1, pady=1)
    b1.pack(side=tk.LEFT, padx=5, pady=5)


    # for search in store
    row2 = tk.Frame(app)
    lab2 = tk.Label(row2, text="جست و جوی گوشی")
    lab2.config(bg='RoyalBlue4', fg='white')
    row2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    lab2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    options = ['name', 'price', 'existent']
    searchBy = makeForm(app, options, "search")
    row2.bind('<Return>', (lambda event, e=search: search(e)))
    r2 = tk.Frame(app)
    b2 = tk.Button(r2, text='جست و جو', command=(lambda e=searchBy: search(e)))
    b2.config(bg='RoyalBlue1', width=10)
    r2.pack(side=tk.TOP, fill=tk.X, padx=1, pady=1)
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    app.mainloop()