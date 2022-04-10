import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123) #imposta il "seme" casuale, in modo che le simulazioni siano riproducibili

#print(np.random.rand()) #printa un numero casuale, se non viene specificato alcun seed printa un numero compreso tra 0 e 1

#print(np.random.randint(1,7)) #riproduce il comportamento di un dado, printa un numero casuale tra 1 e 6
#print(np.random.randint(1,7))

dice = np.random.randint(1,7)
step = 50
all_walks = []

for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        if dice <= 2 :
            step = max(0, step - 1)
        elif dice >= 3 and dice <= 5 :
            step = step + 1
        else :
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

np_aw_t = np.transpose(np.array(all_walks))
ends = np_aw_t[-1, :]
plt.hist(ends)
plt.show()