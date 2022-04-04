from decimal import Decimal
import logging
items = [{"name":"mleko","quantity":5,"unit":"l","price":3},
        {"name":"kawa","quantity":10,"unit":"kg","price":10},
        {"name":"cukier","quantity":3,"unit":"kg","price":2.5}]
stock = []
def stock(items):
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    for stuff in items:
        name = (stuff["name"])
        quantity = (stuff["quantity"])
        unit = (stuff["unit"])
        price = (stuff["price"])
        print(name+str("\t\t%s" % quantity)+"\t\t%s" % unit+str("\t\t%s" % price))
def add_items(items):
        new_items = {}
        name = str(input("Nazwa:"))
        new_items["name"] = name
        quantity = Decimal(input("Ilość:"))
        new_items["quantity"] = quantity
        unit = str(input("Jednostka:"))
        new_items["unit"] = unit
        price = Decimal(input("Cena:"))
        new_items["price"] = price
        for i in items:
            if i["name"] != new_items["name"]:
                items.append(new_items)
            elif i["name"] == new_items["name"] and i["price"] != new_items["price"]:
                items.append(new_items)
            else:
                i["quantity"]=new_items["quantity"]+i["quantity"]
            break
def sell_items(items):
        sell = {}
        name = str(input("Nazwa:"))
        sell["name"] = name
        quantity2 = Decimal(input("Ilość:"))
        sell["quantity"] = quantity2
        for i in items:
            if i["name"] == sell["name"]:
                i["quantity"]=i["quantity"]-sell["quantity"]
            else:
                break

while True:
    warehouse = input("What you want to do?\n For check the stock write: 'Show'.\n For adding to stock write:'Add'.\n For selling from stock writ:'Sell'.\n For exit write: 'Exit'.\n ...:")
    if warehouse == "Show":
        print(stock(items))
    elif warehouse == "Add":
        pass
        add_items(items)
    elif warehouse == "Sell":
        pass
        sell_items(items)
    elif warehouse == "Exit":
        break
