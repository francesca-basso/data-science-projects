import numpy as np

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }

for key, value in europe.items() :
    print("The capital of " + key + " is " + value)


#con gli array numpy si itera usando la unzione np.nditer(nome variabile)