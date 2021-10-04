#exercice de TD   #EVITER LES ACCENTS DANS LES NOMS DES FONCTIONS ET DES VARIABLES

#question 1
print("\n") ; print("question 1") ; print("\n")

import random

class Proie:
    
    def __init__(self):
        self.age = random.randint(1,2000) # gérère un entier aléatoire entre 1 et 2000
        self.signal_reproduction = False
        self.cycle_reproduction  = 100

    def afficher(self):
        print ("age=",self.age,"\n","signal_reproduction=",self.signal_reproduction,"\n","cycle_reproduction=",self.cycle_reproduction,"\n")

    def etape_suivante(self):
        self.age = self.age + 1

        if (self.age)%(self.cycle_reproduction) == 0:
            self.signal_reproduction = True

RIP=Proie()
RIP.afficher()




#question 2
print("\n") ; print("question 2") ; print("\n")

class Predateur(Proie):

    def __init__(self):
        Proie.__init__(self) # il faut appeller le constructeur de la classe Proie pour l'héritage, la fonction __init__
        self.niveau_famine = random.randint(1,16)
        self.seuil_famine  = 21
    def afficher(self):
        #print ("age=",self.age,"\n","signal_reproduction=",self.signal_reproduction,"\n","self.cycle_reproduction=",self.cycle_reproduction)
        Proie.afficher(self) #pour appeler la fonction afficher de la classe Proie
        print("niveau_famine",self.niveau_famine,"\n","seuil_famine=",self.seuil_famine,"\n")
    def etape_suivante(self):
        Proie.etape_suivante(self) ##pour appeler la fonction etape_suivante de la classe Proie #mettre self dedand !!!
        self.niveau_famine = self.niveau_famine + 2

RIP=Predateur()
RIP.afficher()        



#question 3
print("\n") ; print("question 3") ; print("\n")

Proi=Proie()
Pred=Predateur()
print("l'age de Proie est ",Proi.age)
print("l'age de Prédateur est ",Pred.age,"\n")



#question 4
#print("\n") ; print("question 4") ; print("\n")

class Population:
    def __init__(self , nombre_proies , nombre_predateurs):
        
        self.liste_predateurs = [0]*(nombre_predateurs)  # []*3 == []
        self.liste_proies     = [0]*(nombre_proies)
        self.temps_simulation = 200 #j'utilise 200 au lieu de 2000 parce que dand la pratique, une durée de simulation de 2000 demande beaucoup de temps à la machine
        self.liste_nombre_proies     = [0]*(self.temps_simulation)
        self.liste_nombre_predateurs = [0]*(self.temps_simulation)
        self.coefficient_predation = 1 #on pourra varier par la suite
        self.liste_temps      = [i for i in range(self.temps_simulation)]  #[0,1,2,3,4,5,6,.......,1998,1999]
        
        for i in range(len(self.liste_predateurs)) :
            self.liste_predateurs[i] = Predateur()

        for i in range(len(self.liste_proies)):
            self.liste_proies[i] = Proie()

    def afficher(self):
        print("liste_predateurs=",self.liste_predateurs)
        print("liste_proies="    ,self.liste_proies)
        print("temps_simulation=",self.temps_simulation)
        print("coefficient_predation=",self.coefficient_predation)
        print("liste_temps="      ,self.liste_temps)
        print("liste_nombre_proies="    ,self.liste_nombre_proies)
        print("liste_nombre_predateurs=",self.liste_nombre_predateurs)
        print("\n")




#question 6
print("\n") ; print("question 1") ; print("\n")

def rencontre (self):
    for index_proie in range (len(self.liste_proies)): #parcours indexé de la liste des proies
        une_proie   = self.liste_proies[index_proie] 

        for un_predateur in self.liste_predateurs: # parcours indexé de la liste des predateurs

             if (un_predateur).niveau_famine != 0: #si le predateurs sent la famine
                V = (self.coefficient_predation) * (un_predateur.niveau_famine) * len(self.liste_proies)

                if random.randint(1,1500) < V : #sous cette question, la rencontre se fait et dans le cas où il y a rencontre, il n'y aura plus d'autres rencontres entre proies et prédateurs
                    #print("rencontre")
                    del((self.liste_proies)[index_proie]) #j'enlève cette proie de la liste des proies
                    un_predateur.niveau_famine = 0        #je ramène le niveau de famine de ce predateur à 0
                    return                                # il n'y aura plus de rencontre
            
        
            
        
                    

#question 7
print("\n") ; print("question 1") ; print("\n")

def reproduction(self):
    for elt in self.liste_proies : #je parcoure la liste des proies
        if elt.signal_reproduction == True : #si une proie est prête à se reproduire, je crée trois petits proies que j'ajoute à la liste des proies
            for i in range (3):
                elt.signal_reproduction == False #je met le signal de reproduction à False
                #print("reproduction proie")
                Nouveau = Proie()               #une nouvelle proie
                Nouveau.age                 = 0 #l'âge du nouveau né est de 0
                Nouveau.cycle_reproduction  = elt.cycle_reproduction #il a le même cycle de reproduction que sa mère
                Nouveau.signal_reproduction = False #je met son signal de reproduction à False
                (self.liste_proies).append(Nouveau) #je l'ajoute à la liste des proies
            break
                
    for elt in self.liste_predateurs : #je fais le même programme pour les prédateurs prêts à se reproduire en ajoutant le niveau de famine et le seuil de famine du noveau-né
        if elt.signal_reproduction == True :
            for i in range(3):
                elt.signal_reproduction == False
                #print("reproduction predateur")
                Nouveau = Predateur()
                Nouveau.age                 = 0
                Nouveau.cycle_reproduction  = elt.cycle_reproduction
                Nouveau.signal_reproduction = False #il s'est déja reproduit
                Nouveau.niveau_famine = 0  #je met le niveau de famine du nouveau-né à 0
                Nouveau.seuil_famine = elt.seuil_famine #il a le même seuil de famine que sa mère
                (self.liste_predateurs).append(Nouveau)
            break

        

def Etape_suivante(self): #cette fonction permet d'enlever ceux dont l'âge est maximal et d'appliquer la méthode etape-suivante des classes Proie et Predateurs

    for elt in self.liste_proies : #je parcoure la liste des proies

        if elt.age == 2000 : #l'âge maximal est de 2000 puisque les ages sont choisis entre 0 et 2000
            (self.liste_proies).remove(elt) #suppression de ceux dont l'age est maximal
        elt.etape_suivante()

    for elt in self.liste_predateurs :#je parcoure la liste des predateurs

        if elt.age == 2000 :
            (self.liste_predateurs).remove(elt) #suppression de ceux dont l'age est maximal
            #print("mort naturelle")
        elt.etape_suivante()

#question 8
print("\n") ; print("question 8") ; print("\n")

def mort_par_famine(self): #cette fonction permet de supprimer les prédateurs qui meurent par famine

    for elt in self.liste_predateurs :#je parcoure la liste des predateurs

        if  elt.niveau_famine > elt.seuil_famine: #pour ceux dont le niveau de famine dépasse le seuil maximal, je les enlève de la liste des predateurs
            #print("mort par famine")
            (self.liste_predateurs).remove(elt)
            break


    
        
def simulation(self):
    temps = 0 #instant initial
    Y_nb_proies = [0]*self.temps_simulation #cette liste prends pour chaque instant entre 0 et 2000(temps de simulation), la valeur du nombre de proies donc = [nombre_proies(t) pour t entre 0 et 2000]
    Y_nb_predateurs = [0]*self.temps_simulation # [nombre_predateurs(t) pour t entre 0 et 2000]

    while len(self.liste_predateurs) != 0 and len(self.liste_proies) != 0 and temps < self.temps_simulation -1 : #tant qu'il y a des proies et des predateurs, je passe au jour suivant
        Continuer = int(input("\n \n Continuer cette série ? Ecrivez 1 si oui et 0 sinon: "))
        if Continuer == 0:
            print("You end it")
            return
        rencontre(self)       #cette fonction simule une rencontre éventuelle entre une proie et un prédateur
        reproduction(self)    #cette fonction simule la reproduction éventuelle d'une proie ou d'un predateur
        mort_par_famine(self) #cette fonction simule la mort de certains predateurs par famine
        Etape_suivante(self)  #cette fonction incremente l'age de tout le monde, actualise les signaux de reproduction des proies et des predateurs, augmente le niveau de famine des predateurs et élimine les proies ou predateurs dont l'age est maximal
        temps += 1 #on passe au jour suivant
        Y_nb_proies[temps] = len(self.liste_proies) #on enregiste la valeur nombre de proies en ce moment
        Y_nb_predateurs[temps] = len(self.liste_predateurs) #on enregiste la valeur nombre de predateurs en ce moment
        print ("on est au temps t={} \n le nombre de proies est {} \n le nombre de predateurs est{} \n".format(temps,len(self.liste_proies),len(self.liste_predateurs)) ) #un affichage pour afficher ces valeurs

    print("une race est vidée ou bien on est en fi de simulation") # si on est en fin de boucle, c'est que la condition n'est plus valide
    print("Cette simulation a pris {} jours".format(temps),"\n \n") #je donne le temps total de la simulation
    


#cette portion de code permet de tester la fonction définie precedemment pour une nombre de proie = nombre de prédateurs de l'ordre de 1,11,21,31,..,101
for j in range(10):

    Continuer = int(input("\n \n Voulez vous passer à une série avec un nombre_proie==nombre_predateurs=={} ? Ecrivez 1 si oui et 0 sinon: ".format(10*j+1)))
    print("\n \n \n \n pour une population de {} dans les deux clans".format(10*j+1))
    if Continuer == 0 :
        print("You end it")
        break
    Village = Population(10*j+1,1+10*j)
    simulation(Village)
            


#question 9
print("\n") ; print("question 9") ; print("\n")

import numpy as np
import matplotlib.pyplot as plt
def afficher(self):
    self.temps_simulation = 200 #une durée de simulation=2000 demande beaucoup de temps à la machine
    temps = 0
    X_temps = np.array(self.liste_temps)
    Y_nb_proies = [0]*self.temps_simulation
    Y_nb_predateurs = [0]*self.temps_simulation

    while len(self.liste_predateurs) != 0 and len(self.liste_proies) != 0 and temps < self.temps_simulation -1 :
        rencontre(self)
        reproduction(self)
        mort_par_famine(self)
        Etape_suivante(self)
        temps += 1
        Y_nb_proies[temps] = len(self.liste_proies)
        Y_nb_predateurs[temps] = len(self.liste_predateurs)
    Y_nb_proie = np.array(Y_nb_proies)
    Y_nb_predateur = np.array(Y_nb_predateurs)

    plt.plot(X_temps , Y_nb_proie , label = "nombre de proies")
    plt.plot(X_temps , Y_nb_predateur , label = "nombre de predateurs")
    plt.plot(X_temps , Y_nb_proie - Y_nb_predateur , label = "nombre de proies - nombre de predateurs")
    plt.legend() #pour faire afficher le label de chaque courbe
    plt.show()
    




#question 10
print("\n") ; print("question 10") ; print("\n")


print("varions nombre de proies et de predateurs")
for i in range(1,3):
    self = Population(200*i,50*i)
    for j in range (5):
        afficher(self)
#constat: Pour de mêmes valeurs initiales, on a généralement: nombre_proies - nombre_predateurs est presque constant dans chaque expérience mais cette constante dépend de l'expérence (autour de 150)
# nombre_proies - nombre - nombre_predateurs monte quand les populations augmentent
# quand les populations sont grzndes, nombre_proies - nombre - nombre_predateurs decroit en fonction du temps


print("varions coefficient predation")
self = Population(200,50)
for j in range (1,6):
    self.coefficient_predation = j
    afficher(self)
# nombre_proie - nombre_predateurs est constant et la constante varie peu
# le nombre de proies tués augmente quand le coefficient de predation augmente (linéaire dont l'ordonnee à l'origine est croissante en fct du coef de predation)


print("varions seuil famine")
self = Population(200,50)
for j in range (1,6):
    for un_predateur in self.liste_predateurs:
        un_predateur.seuil_famine = 10*j
    afficher(self)
# quand seuil_famine est faible(20==famine_moyenne), le nombre de prédateurs passe rapidement à 0 (t=200) (ils meurent par famine); Au meme moment, le nombre de proies ne fait que monter
# quand seuil_famine est élevé, le comportement est normal: nombre_proies - nombre_predateurs est presque constante

print(" varions cycle_reproduction predateur")       
self = Population(200,50)
for j in range (1,6):
    for un_predateur in self.liste_predateurs:
        un_predateur.cycle_reproduction = 50*j
    afficher(self)
#Contrairement au résultat théorique selon lequel l'augmentation du cycle de reproduction des predateurs auraient un impact sur l'évolution du nombre de proies,
#on constate que nombre_proies - nombre_predateurs est presque constant dans le temps; ce qui montre une correlation entre les variables nombre_proies et nombre_predateurs    


print("varions cycle_reproduction proie")
self = Population(200,50)
for j in range (1,6):
    for une_proie in self.liste_proies:
        une_proie.cycle_reproduction = 50*j
    afficher(self)
#De même,
#Contrairement au résultat théorique selon lequel l'augmentation du cycle de reproduction des proient auraient un impact sur l'évolution du nombre de proies,
#on constate que nombre_proies - nombre_predateurs est presque constant dans le temps; ce qui montre encore un fois une correlation entre les variables nombre_proies et nombre_predateurs    
