import duration as duration
import imageio.v2
import imageio.v2 as ima

import imageio
filenames =["1s.png","2s.png","3s.png","4s.png","5s.png","6s.png","7s.png","8s.png","9s.png","10s.png","11s.png","12s.png","13s.png","14s.png","1s.png","2s.png","3s.png","4s.png","5s.png","6s.png","7s.png","8s.png","9s.png","10s.png","11s.png","12s.png","13s.png","14s.png","1s.png","2s.png","3s.png","4s.png","5s.png","6s.png","7s.png","8s.png","9s.png","10s.png","11s.png","12s.png","13s.png","14s.png"]
images =[]
for i in filenames:
    images.append(ima.imread(i))

ima.mimsave("sponge.gif",images,duration=0.5)

