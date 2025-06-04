class fruit:
    def __init__(self, name, taste, color, shape , size, origin):
        self.name=name
        self.taste=taste
        self.color=color
        self.shape=shape
        self.size=size
        self.origin=origin
        self.flavour="tropical"
        self.juiciness="succulent"
        self.crunchiness="crispy"
    def display(self):
        print(f"name of fruit is {self.name}")
        print(f"taste of fruit is {self.taste}")
        print(f"color of fruit is {self.color}")
        print(f"shape of fruit is {self.shape}")
        print(f"size of fruit is {self.size}")
        print(f"origin of fruit is {self.origin}")
        print(f"flavour of fruit is {self.flavour}")
        print(f"juiciness of fruit is {self.juiciness}")
        print(f"crunchiness of fruit is {self.crunchiness}")
s1 = fruit("apple", "lucious", "red", "circle", "8.5in", "japan")
s1.juiciness="succulent"
s1.display()