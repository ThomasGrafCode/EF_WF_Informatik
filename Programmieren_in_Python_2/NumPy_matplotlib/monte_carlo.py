import numpy as np
import matplotlib as plt
 
# charakteristische Funktion des Einheitskreises:
# fun_c(x,y) = 1, falls der Punkt (x,y) einen Abstand <= 1
# vom Ursprung (0,0) hat
# fun_c(x,y) = 0, sonst
def fun_c(x,y):
    return(np.sqrt(x**2 + y**2) <= 1)
 
def mc_quad(fun_c,N):
  # Monte-Carlo Methode für die Funktion fun_c auf [0,1]^2
  # mit N sample Punkten
   
  x = np.random.rand(N) # N zufällige Zahlen aus [0,1] für die x-Koordinate
  y = np.random.rand(N) # N zufällige Zahlen aus [0,1] für die y-Koordinate
   
  # jedes der N Zahlenpaare (x,y) definiert einen Punkt im Einheitsquadrat
  # teste für jeden dieser N Punkte, ob er im Einheitskreis liegt (return True)
  # oder nicht (return False)  
  values = fun_c(x,y)
   
  ev = sum(values)/N # Erwartungswert (expectation value = ev)
   
  # Standardabweichung (standard deviation = sd) berechnen
  sd = ( sum(values**2)/N - (sum(values)/N)**2 )**0.5
   
  plt.pyplot.scatter(x,y,c=values,marker = '+',s=1.0)
   
  return ev, sd
   
k = 6
N = 10**np.arange(k)
results = []
for i in range(k):
  results += [mc_quad(fun_c,N[i])]
   
print('Monte-Carlo to compute pi/4=',np.pi/4,':\n', np.array(results))