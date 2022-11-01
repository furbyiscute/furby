import serverrunner
a = serverrunner.send_function("return threading.active_count()")
print(a.return_)