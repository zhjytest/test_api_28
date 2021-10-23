
# 主要实现的是用户管理的测试用例
from apis.user_manager_api import UserManagerApi
import unittest
from data.user_manager_data import user_manager_data

class TestUserManagerCase(unittest.TestCase):


    user_id = 449


    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManagerApi()



    # 实现添加测试用例

    def test01_add_user(self):
        # 1. 定义数据

        # 2. 调用添加管理员接口
        result = self.user.add_user(user_manager_data['username'],user_manager_data['password'])

        # 获取id值
        if result.get('data').get('id'):
            TestUserManagerCase.user_id = result.get('data').get('id')
        # 3.进行断言
        self.assertEqual(0,result.get('errno'))



    # 实现编辑测试用例
    def test02_edit_user(self):
        # 1.定义数据
        # 2.调用编辑接口
        result = self.user.edit_user(TestUserManagerCase.user_id,user_manager_data['new_user'],user_manager_data['password'])
        # 3.进行断言
        self.assertEqual(0,result.get('errno'))

    # 实现删除测试用例
    def test04_delete_user(self):
        result = self.user.delete_user(TestUserManagerCase.user_id,user_manager_data['new_user'],user_manager_data['password'])
        self.assertEqual(0,result.get('errno'))


    # 实现查询测试用例
    def test03_get_user(self):
        result = self.user.get_user()
        self.assertEqual(0,result.get('errno'))