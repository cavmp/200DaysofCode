import collections

print("*****************************")
print("*   Love Match Calculator   *")
print("*****************************")

name1=input("Type a name: ")
name2=input("Type another name: ")

print("\nCalculating...")

thestring = name1 + "love" + name2
d = collections.defaultdict(int)
for c in thestring:
    d[c] += 1
a = list(d.values())
while True:
    print(" ".join(map(str, a)))
    if len(a) == 2:
        break
    b = []
    for x, y in enumerate(a):
        b = b + list(map(int, str(a[len(a) - 1 - x] + y)))
        if x + 1 == int(len(a) / 2):
            if len(a) % 2 != 0:
                b.append(a[len(a) - 2 - x])
            break
    a = b

print("\nLove match % for '" + name1 + "' and '" + name2 + "' is")
print(f'''
						   Love        Love
						 Love Love  Love Love
						Love     Love     Love
						Love              Love
						 Love     {"".join(map(str, a))}%    Love
						  Love          Love
						    Love      Love
						      Love  Love
						         Love
						         ''')
