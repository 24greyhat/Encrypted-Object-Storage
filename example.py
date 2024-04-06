from EOS import Eos

x = Eos("example", "123")

x.dump({"dict": {"key":"value"}})
x.dump({"tuple": (1,2,3,4)})
x.dump({"set": {1,2,3,4}})
x.dump({"array": [1,2,3,4]})

print(x.load())
