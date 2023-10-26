import random
import string

worker_id =  ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
print("worker_id: ", worker_id)

print("hello, world!")
