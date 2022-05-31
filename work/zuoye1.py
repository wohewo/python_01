# ## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示

# user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},
#              {'role':'user','account':'dev','password':'123456','dept':'dev'}]
#
# users = ['admin','dev']
#
# user_name = input("请输入用户名:")
# user_pass = input("请输入密码:")
# if user_name in users and user_pass == "123456":
#     print({'code':0,'message':'登录成功'})
# elif user_name  == " " or user_pass == " ":
#     print({'code':1,'message':'登录失败,用户名或密码不能为空'})
# elif user_name not in users or user_pass != '123456':
#     print({'code':1,'message':'登录失败,请检查您的用户名或密码是否填写正确'})
# else:
#     print({'code':1,'message':'登录失败,请检查您的用户名或密码是否填写正确'})

user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'123456','dept':'dev'}]

result = {"code":0,"message":""}

def login(username,password):


    if username is None or username == "":
        result.update({"code":1,"message":"用户名不能为空"})
        return result

    if password is None or password == "":
        result.update({"code":1,"message":"密码不能为空"})
        return result


    for user_info in user_list:
        if username == user_info.get('account') and password == user_info.get('password'):

            result.update({"message":"登录成功","user_list":user_list})
            return result

    result.update({"code":1,"message":"请检查用户名或密码是否匹配"})
    return result




if __name__ == '__main__':
    username = input("请输入用户名:")
    password = input("请输入密码:")

    print(login(username,password))






## 需求-迭代2：用户查询功能:
# 1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
# 2. 若输入的用户名正确，返回登录用户的信息，password字段不显示  。
# 3. 若输入的用户名不正确 ，给出无查询结果的提示
# 4. 查询支持模糊查询。
#
#
#
# ## 需求-迭代3：用户新增功能:
# 1. 将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
# 2. 需要对文件的读写进行异常捕获
# 3. 用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
# 4. 同时进行查询时，也能查询出该用户 。


