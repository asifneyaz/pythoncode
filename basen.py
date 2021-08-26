import base64
string = "0123456789abcdefghijklmnoppqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
var1 = string.encode('ascii')
print(var1)
var1bytes = base64.b64encode(var1)
print(var1bytes)
decoded = var1bytes.decode('ascii')
print(decoded)

# var3 = var2.decode("ascii")
# print(var3)
