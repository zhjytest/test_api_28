
# 接口自动化

## 1.实现步骤

1. 先实现apis里的内容

    * base ： 就是提供给被测接口的一个基类 
        * get_url() : 主要处理的是url
        * get() : 就是将requests.get()进行重写，让更便捷，更符合需求
        * post() : 就是将requests.post()进行重写，让更便捷，更符合需求
        * get_headers() : 获取请求头中的数据
        * login() : 调用登录接口，保存token值到缓存
        
    * user_manager_api : 主要实现的是用户管理员接口
        * add_user : 添加管理员
        * edit_user : 修改管理员
        * delete_user :删除管理员
        * get_user : 查询管理员
    
2. 实现测试用例