# Object Oriented Programming
# each object has 2 essential parts
# 1-Characteristics they call it (Attribute)   \|/   2-Actions they call it (Methods)
# like name                                    \|/     #like sell item
# address                                      \|/     # take item

# Object VS CLass
# object is specific like shirts(Attribute)  { color : yellow , size : medium , style : short , price : 14}
#                         shirts(Methods)     {change_price}
# and this is known as Class it's like the blue print to get object with attribute and methods
class Shirts:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


polo_shirt = Shirts('gray', "3XL", "LONG Sleeves", 15)
normal_shirt = Shirts('yellow', "2XL", "LONG Shirt", 10)
short_shirt = Shirts('black', "1XL", "short Shirt", 17)

print(polo_shirt.color)
print(polo_shirt.size)
print(polo_shirt.style)
print(polo_shirt.price)

polo_shirt.change_price(10)

print(polo_shirt.price)
print(polo_shirt.discount(0.2))

shirts_list = [polo_shirt, normal_shirt, short_shirt]
shirtZ = [shirt for shirt in shirts_list]
for item in shirtZ:
    print(item.style)
    print(item.size)
