mylist = ["a", "b", "a", "c", "c"]
print(mylist)
mylist = list(dict.fromkeys(mylist))
print(mylist)

def remove_dup(a_list):
    a_list = list(dict.fromkeys(a_list))
    return(a_list)


print(remove_dup(["a", "b", "c", "C", "c" ]))

a = []

if not a:
    print("Empty list")

if len(a) == 0:
    print("Empty list")

x = [1, 2, 3]
x.append([4,5])
print(x)



y = [1, 2, 3,]
y.extend([4, 5])
print(y)



ints = [8, 23, 45, 12, 78]

for idx, val in enumerate(ints):
    print(idx, val)

x = ["foo", "bar", "baz"]

x.index("foo")
print(x.index("foo"))
