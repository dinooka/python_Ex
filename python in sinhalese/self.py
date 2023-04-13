class Cricketer:
    ground = "Melbourne Cricket Ground"

    def set_ground(self,ground):
        self.ground = ground

    def announce(self,date):
        msg = f"The match will be played in {self.ground} on {date}."
        print(msg)

batsmen = Cricketer()
batsmen.set_ground("Lords")
batsmen.announce("March 14")

batsmen2 = Cricketer()
# batsmen2.set_ground("Lords")
batsmen2.announce("March 16")