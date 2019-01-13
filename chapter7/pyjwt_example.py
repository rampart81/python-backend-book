import jwt 

data_to_encode = {'some': 'payload'} 
encryption_secret = 'secrete' 
algorithm = 'HS256' 
encoded = jwt.encode(data_to_encode, encryption_secret, algorithm=algorithm) # >>> 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5N iznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg'
jwt.decode(encoded, encryption_secret, algorithms=[algorithm]) # >>> {'some': 'payload'}
