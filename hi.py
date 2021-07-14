print("hello world")
print("hi")
import subprocess as sb
x = sb.getoutput('kubectl get pods')
print(x)
