<p align="center">
  <img src="img/redis.png"/>
</p>

# Redison : Redis + Json : Shared objects in memory using redis and json files

## Getting Started

## numpy

```bash
from redison import RedisObject
import numpy as np

array = np.random.rand(10)  # Set the object in python stack
print(array) # Retrieve the object from the stack
array = RedisObject(array)  # Set the object in redis
print(array.get())  # Retrieve the object from the redis database

```

## multiproc
Processus 1

```bash
from redison import RedisObject
import numpy as np

while True:
    # Push array1
    RedisObject(id="array1", data=np.random.rand(10))
    
    # Pull array2
    array2 = RedisObject(id="array2")
    
    # Wait for array1 to be set in redis by proc2
    print(array2.get(blocking=True)) 

```
Processus 2


```bash
from redison import RedisObject
import numpy as np

while True:
    # Push array2
    RedisObject(id="array2", data=np.random.rand(10))
    
    # Pull array1
    array1 = RedisObject(id="array1")
    
    # Wait for array1 to be set in redis by proc1
    print(array1.get(blocking=True)) 

```

## multiproc remote
Processus 1

```bash
from redison import RedisObject
import numpy as np

while True:
    # Create array2
    array1 = np.random.rand(10)
    
    # Push array2 
    RedisObject(id="array1",
                data=array1,
                host="10.1.0.2")
   
    # Pull array1
    array2 = RedisObject(id="array2", 
                         host="10.2.0.2")
   
    # Wait for array1 to be set on the remote machine 2
    print(array2.get(blocking=True)) 
```
Processus 2

```bash
from redison import RedisObject
import numpy as np

while True:
    # Create array2
    array2 = np.random.rand(10)
    
    # Push array2 
    RedisObject(id="array2",
                data=array2,
                host="10.2.0.2")
   
    # Pull array1
    array1 = RedisObject(id="array1", 
                         host="10.1.0.2")
   
    # Wait for array1 to be set on the remote machine 1
    print(array1.get(blocking=True)) 

```

## Contributions

Email me at j.cadic@9dw-lab.com for any questions.
