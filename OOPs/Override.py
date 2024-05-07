class demo:
    def hello(self):
        return "Hello, World!"

class newdemo(demo):
    def hello(self):
        return "I am Overriding Method"

demo = demo()
new = newdemo()

print(demo.hello())
print(new.hello())
