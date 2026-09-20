# a)
part_a = [
    (a, b, c, d)
    for a in range(1, 11)
    for b in range(1, 11)
    for c in range(1, 11)
    for d in range(1, 11)
    if len({a, b, c, d}) == 4
    and a**2 + b**2 == c**2 + d**2
]


# b) 
strings = ['One', 'SEVEN', 'three', 'two', 'Ten']

part_b = [
    (word.lower(), len(word))
    for word in strings
    if len(word) < 5
]


# c) 

names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']

part_c = [
    f"{first} {middle[0]}. {last}"
    for first, middle, last in (name.split() for name in names)
]


# d)
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

part_d = [
    (w1, w2)
    for w1 in lst1
    for w2 in lst2
    if sorted(w1.lower()) == sorted(w2.lower())
]


# e)
s = ['one', 'two', 'three']

part_e = {
    word: len(word)
    for word in s
}


# f) 

text = "Hello world"

part_f = {
    i: c
    for i, c in enumerate(text)
    if c.lower() in "aeiou"
}



print("a)", part_a)
print("b)", part_b)
print("c)", part_c)
print("d)", part_d)
print("e)", part_e)
print("f)", part_f)
print("Ernest vallebyona: Z23588328 ")