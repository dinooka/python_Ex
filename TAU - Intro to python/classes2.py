class Person:
    def __init__(self,fname,lname,health,status):
        self.fname = fname
        self.lname = lname
        self.health = health
        self.status = status

    def intro(self):
        print("Hi!, I'm {} {}".format(self.fname,self.lname))

    def status_change(self):       
        if self.health == 100:
            print("{} is fully healthy!".format(self.fname))
        elif self.health == 85:
            print("{} feels tired.".format(self.fname))
        elif self.health == 75:
            print("{} feels unwell.".format(self.fname))
        elif self.health <= 50:
            print("{} goes to the doctor.".format(self.fname))
        else:
            print("{} is unconscious.".format(self.fname))

Anna = Person("Anna","Kornikova",85,True)
Roger = Person("Roger","Federer",41,True)
Rafael = Person("Rafael","Nadal",20,False)

print("{} is my friend? {}".format(Anna.fname,Anna.status))
print("{} is my friend? {}".format(Roger.fname,Roger.status))
print("{} is my friend? {}".format(Rafael.fname,Rafael.status))

Anna.intro()
Anna.status_change()


class Enemy(Person):
    def __init__(self, weapon,fname, lname, health, status):
        super().__init__(fname, lname, health, status)
        self.weapon = weapon

    # polymorphism(method over riding)
    def intro(self):
        print("You are my mortal enemy!!!")

    def hurt(self,other):
        if self.weapon == 'rock':
            other.health -=10
        elif self.weapon == 'stick':
            other.health -=5
        print(other.health)

    def insult(self,other):
        if other.health <= 80:
            print("{}, you are tired & weak.".format(other.fname))
    
    def steal(self,other):
        print("ha ha ha, {} I have your stuff!".format(other.fname))
        if other.status == True:
            other.status == False

Alex = Enemy('rock','Alex','Krycheck',75,status=False)
Lena = Enemy('stick','Lena','Headingly',55,status=True)

# Alex.hurt(Anna)
# Alex.insult(Anna)
# Alex.steal(Anna)

# Anna.steal(Alex)

Alex.intro()

        