class Cat:
    def __init__(self, name, age, weight, breed ):
        self.Name = name
        self.Age = age
        self.Weight = weight
        self.Breed = breed

    def ShowInfo(self):
        print(f"Name: {self.Name}\n"
              f"Age: {self.Age}\n"
              f"Weight: {self.Weight} kg\n"
              f"Breed: {self.Breed}\n")