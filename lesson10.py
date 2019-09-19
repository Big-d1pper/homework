class Bird:

    def __init__(self, name="Kesha"):
        self.name = name

    def flight(self):
        print(f"{self.name} Flight now!")

    def walk(self):
        print(f"{self.name} Walk now!")


class Raccoon:

    def make_some_destroy(self):
        # self.steel()
        print("Raccoon make some wierd stuff")

    def steel(self):
        raise NotImplemented


class DanceMixin:

    def dance(self):
        print(f"{self.name} Dance now!!!")


class Cat(Bird, Raccoon, DanceMixin):
    fluffines = 12

    def __init__(self, name="Pushok", color="Ginger"):
        super(Cat, self).__init__(name)
        self.color = color
        self.voice()

    def __hash__(self):
        return len(f"{self.name}{self.color}{self.fluffines}")

    # def __del__(self):
    #     self.sleep()

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}"

    def to_dict(self):
        return {
            'name': self.name,
            'color': self.color
        }

    def _some_method(self):
        pass

    def __private(self):
        pass

    def sleep(self):
        print(f'{self.name}: Cat sleeps!')

    def wake_up(self):
        print("Cat wakes up now!")
        print(self.fluffines)
        self.voice()

    def voice(self):
        print(f"{self.name} Meow!")

    def info(self):
        print(
            self.name,
            self.color,
            sep='\n'
        )

    # def flight(self):
    #     print(f"{self.name} {self.color} Flight now!")
    #
    # def my_flight(self):
    #     super(Cat, self).flight()


my_cat = Cat()
# my_cat.info()
# del my_cat
# my_cat_2 = Cat()
#
# my_mother_friend_cat = Cat(
#     name="Best Cat ever",
#     color="black"
# )

# cats_dict = {my_cat: 'qweqwe', my_mother_friend_cat: 'dsa'}
# print(cats_dict[my_cat_2])

print(my_cat.name)
print(my_cat.color)

# my_cat.flight()
# my_cat.walk()
my_cat.make_some_destroy()
my_cat.flight()
my_cat.dance()

print('*' * 10)
# print(my_mother_friend_cat.name)
# print(my_mother_friend_cat.color)
