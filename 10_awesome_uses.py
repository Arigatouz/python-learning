# fString
name = "Ali"
# message = "hello", name
# message = "hello " + name
message = f"hello {name} "

print(type(message))
print(message)


# unpacking

tup = (1, 2, 3, 4, 5)
a, b, c, d, e = tup
print(a, b, c, d, e)

lst = [1, 2, 3, 4, 5]
a, b, c, d, e = lst
print(a, b, c, d, e)

string = "Hello"
a, b, c, d, e = string
print(a, b, c, d, e)

dic = {"aa": 1, "bb": 2, "cc": 3, "dd": 4, "ee": 5}
a, b, c, d, e = dic.values()
a_, b_, c_, d_, e_ = dic.keys()
print(a, b, c, d, e)
print(a_, b_, c_, d_, e_)


# multiple Assignment

width, height = 400, 300
print(f"Width is {width}, and height is { height}")
# this is value swap if you ever needed it
width, height = height, width
print(f"Width is {width}, and height is { height}")


# Comprehensions

# create one type of collection in one line

x = [i for i in range(50) if i % 2 == 0]
print(x)

me = "Hello"
word = (i for i in f"{me}")
print(word)  # don't worry about the out put of this just know its a object generator
print(list(word))
