class Abs:
    _context = {}

    def __set(id,val):
        Abs._context[id] = val

    def __get(id):
        return Abs._context.get(id)
    
class truc(Abs):
    def machin(self,val):
        Abs.__set("truc",val)
        self.test = Abs.__get("truc")

    def __str__(self) -> str:
        return "{}".format(self.test )

    
test = truc()
test.machin(456)
print(test)





def vue1():
    print("Vue 1")
    choix = input("Appuyez sur '2' pour passer à la Vue 2 ou 'q' pour quitter : ")
    
    if choix == '2':
        vue2()
    elif choix == 'q':
        print("Programme terminé.")
    else:
        print("Choix invalide.")
        vue1()

def vue2():
    print("Vue 2")
    choix = input("Appuyez sur '1' pour passer à la Vue 1 ou 'q' pour quitter : ")
    
    if choix == '1':
        vue1()
    elif choix == 'q':
        print("Programme terminé.")
    else:
        print("Choix invalide.")
        vue2()

# Démarrer avec la première vue
vue1()
