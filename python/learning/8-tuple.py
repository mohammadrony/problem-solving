print('---------------------------------')

tpl1 = (1,2,3,4,5,6,7)
tpl2 = ('ctags', 'grep','bash','sed', 'awk','make')
print(tpl1[0:2])
print(tpl2[len(tpl2)-1])
print(min(tpl1))
print(tpl1[len(tpl1)-1])

print('---------------------------------')

pair1 = (10,20)
pair2 = (12,18)
if (pair1 > pair2):
    print("pair1 is bigger")
else:
    print("pair2 is bigger")

print('---------------------------------')

student = ("name", 20)
(std_name, std_id) = student
print(std_name)
print(std_id)

print('---------------------------------')

obj1 = {
    'age':20,
    'group':'one'
}

obj2 = obj1.items()
print(obj2)

print('---------------------------------')
