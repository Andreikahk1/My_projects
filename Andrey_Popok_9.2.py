class PizzaError(Exception):
    def __init__(self,pizza = 'unknown', message = ''):
        Exception.__init__(self,pizza,message)
        self.pizza = pizza

class TooMuchCheese(PizzaError):
    def __init__(self, pizza = 'unknown', cheese = '>100', message = ''):
        PizzaError.__init__(self,pizza,message)
        self.cheese = cheese

class Pizza:
    def __init__(self):
        pass
    
    def make_pizza(self,pizza,cheese):
        if pizza not in ['margherita','capricciosa','calzone']:
            raise PizzaError
        if cheese > 100:
            raise TooMuchCheese
        print(pizza,"pizza is ready!")

def main():
    pizza_obj = Pizza()
    for (pz,ch) in [('calzone',0),('margherita',110),('mafia',20)]:
        try:
            pizza_obj.make_pizza(pz,ch)
        except TooMuchCheese as tmce:
            print(tmce,':',tmce.cheese)
        except PizzaError as pe:
            print(pe,':',pe.pizza)

main()
