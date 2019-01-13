import hashlib

m = hashlib.sha256()
m.update(b"test password")
m.hexdigest()  # >>> '0b47c69b1033498d5f33f5f7d97bb6a3126134751629f4d0185c115db44c094e'
