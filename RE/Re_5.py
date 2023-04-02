class HockeyPlayer:
    def __init__(self,name,last_name,goal=0,assist=0):
        self.name = name
        self.last_name = last_name
        self.goal = goal
        self.assist = assist

    def goals(self,goal=0):
        self.goal = goal

    def all_assist(self,assist = 0):
        self.assist = assist

    def statistics(self):
        print(f'Hockey Player Name {self.name} {self.last_name}')
        print(f"Goal:{self.goal}")
        print(f"Assist:{self.assist}")

ovech = HockeyPlayer("Alexandr","Ovechkin")
ovech.goals(700)
ovech.all_assist(500)
ovech.statistics()