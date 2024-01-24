
import matplotlib.pyplot as plt
import numpy as np
#in order for this to work you have to download the library
#everytime you are starting a new project, you create a vitural enviroment and install those in you virtual environment
#Step 1: Create Virtual Enviroment(PC use py)(MAC use python3)
#Step 2: Activate Virtual Enviroment(.\myvenv\Scripts\activate)
#Step 3: Install 3rd party library/module

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")
#once i have checked into repository one on left is what we changed
#one on the right is the new version
