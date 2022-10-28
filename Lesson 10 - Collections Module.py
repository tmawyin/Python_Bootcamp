# Collections Module
import collections as col

# Counter class - counts how many individual items there are
mylist = [1,1,1,2,2,2,2,2,4,4,4,4,4,6,6,6,6,3,3,3,3]
num = col.Counter(mylist)
print(num)

print(f"the most common value pair is: {num.most_common(1)}")


# defaultdict - assigns a default value to non-existent keys of a dict
d = {"a":10}
# d["b"] will show an error instead we can use defaultdict
d = col.defaultdict(lambda: 0)
d["a"] = 10

print(d["b"])


# namedtuple - adds "index position" to a tuple
Dog = col.namedtuple("Dog",["age", "breed", "name"])
sammy = Dog(age=5, breed="Husky",name="Sammy")
print(sammy.age)
print(sammy[0])