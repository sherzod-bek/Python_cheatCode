

# F string (min - > python 3.6)
name = "Sher"
name2 = "Zod"
print(f'Hello {name} va {name2} = {1,2,3}')


# -----------------------------------------------------------------

# Unpacking
tup = (1, 2, 3, 4, 5)
lst = [1, 2, 3, 4, 5]
string = "hello"

dic = {"a":1, "b":2}
dicA, dicB = dic.values()

a, b, c, d, e = lst  # a=lst[0], b=lst[1], c=lst[2] etc.
print(a,b,c,d,e)

# -----------------------------------------------------------------
# Multiple Assignment
width, height = 400, 500

# old solution
# temp = width
# width = height
# height = temp

# easy solution
width, height = height, width
print(width, height)
# -----------------------------------------------------------------
# Coprehensions (filling easy)

# old
# x =[]
# for i in range(1000):
#     x.append(0)
x = [0 for i in range(100)]
y = [i for i in range(100)]
z = [i for i in range(20) if i % 2 == 0]
d = [i*j for i in range(5) for j in range(5)]
print(d)
# -----------------------------------------------------------------
# Inline/Ternary Condition

# old
# if 2>3:
#     x=1
# else:
#     x = 1

x = 1 if 2>3 else 0

print(x)
# -----------------------------------------------------------------