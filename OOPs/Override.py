class demo:
    def hello(self):
        print("Hello, World!")

class newdemo(demo):
    def hello(self):
        print("I am Overriding Method")

demo = demo()
new = newdemo()

print(demo.hello())
print(new.hello())
