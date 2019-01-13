import bcrypt 

bcrypt.hashpw(b"secrete password", bcrypt.gensalt()) # >>> b'$2b$12$.XIJKgAepSrI5ghrJUaJa.ogLHJHLyY8ikIC.7gDoUMkaMfzNhGo6'
bcrypt.hashpw(b"secrete password", bcrypt.gensalt()).hex() # >>> '243262243132242e6b426f39757a69666e344f563852694a43666b5165445469397448446c4d366635613542396847366d5132446d62744b70357353'
