import hashlib

text="16962shoulashou057116962"
m=hashlib.md5()
m.update(text)
encodeStr=m.hexdigest()
print encodeStr
