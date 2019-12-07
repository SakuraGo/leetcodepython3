def student_file(name,gender = "男",age = 10,college = "通河三小"): ##默认参数放在最前面
    print("我叫："+name)
    print("今年"+str(age)+"岁")
    print("我是"+gender+"生")
    print("我在"+college+"上学")
student_file("鸡小萌")
print("~~~~~~~~~~~~~~~~~~")
student_file("guoguo")
print("~~~~~~~~~~~~~~~~~~")
##SyntaxError: positional argument follows keyword argument
##不可以混合调用,
# student_file("qq",gender="男",15,college="人民路小学")
student_file("qq",gender="男",age=15,college="人民路小学")