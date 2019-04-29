#  -*-  coding:utf-8 -*-
import unittest
import time
from selenium import webdriver

class test_daishen(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_Change_card(self):
        #测试H5登录
        self.driver.get("http://h5.super.com/login")
        self.driver.set_window_size(480, 800)
        #用账号、密码进行登录
        element = self.driver.find_element_by_xpath
        phone_numb = element("//*[@id='tab1']/div/div[1]/div[2]/p/input")
        phone_numb.send_keys("13070123277")
        #请输入密码
        user_password = element("//*[@id='tab1']/div/div[2]/div[2]/p/input")
        user_password.send_keys("a111111")
        #点击登录按钮
        element("//*[@id='showModel']").click()
        time.sleep(2)
        #点击借钱按钮
        element("/html/body/div/div/div/div[1]/div/a").click()
        time.sleep(2)
        
        #点击照相机这个工具
        pic1 = element("/html/body/div/div/div[1]/div/div/div/div/label[1]").click()
        time.sleep(2)
#       #上传身份证正面
        time.sleep(15)
        #点击照相机这个工具
        pic2 = element("/html/body/div/div/div[1]/div/div/div/div/label[2]").click()
        time.sleep(5)
        #上传身份证正面
#         time.sleep(5)
        #点击照相机这个工具
        pic2 = element("/html/body/div/div/div[1]/div/div/div/div/label[3]").click()
        time.sleep(5)
        #上传身份证正面
#         time.sleep(5)
        #点击下一步
        element("/html/body/div/div/a").click()
        time.sleep(5)
        
        #输入微信号
        web_chat = element("/html/body/div/div/ul/li[1]/input")
        web_chat.clear()
        time.sleep(3)
        web_chat.send_keys("22222222")
        time.sleep(3)
        #输入QQ号
        QQ_num = element("/html/body/div/div/ul/li[2]/input")
        QQ_num.clear()
        time.sleep(3)
        QQ_num.send_keys("22622222")
        #输入联系人1姓名
        name1 = element("/html/body/div/div/ul/li[3]/input")
        name1.clear()
        time.sleep(1)
        name1.send_keys("苏菲")
        #输入联系人1电话
        phone1 = element("/html/body/div/div/ul/li[4]/input")
        phone1.clear()
        time.sleep(1)
        phone1.send_keys("13313331333")
        #输入联系人2姓名
        name2 = element("/html/body/div/div/ul/li[5]/input")
        name2.clear()
        time.sleep(1)
        name2.send_keys("张三")
        #输入联系人2电话
        phone2 = element("/html/body/div/div/ul/li[6]/input")
        phone2.clear()
        time.sleep(3)
        phone2.send_keys("13313331334")
        #选择借款用途
        element("/html/body/div/div/div[1]/button[2]").click()
        #点击下一步按钮
        element("/html/body/div/div/a").click()
        time.sleep(5)
        #输入运营商密码
        element("/html/body/div/div/form/div[2]/div/div[2]/div[1]/input").send_keys("211314")
        element("/html/body/div/div/form/div[4]/input").click()
        time.sleep(2)
        #输入短信验证码
        time.sleep(15)
        element("/html/body/div/div/form/div[1]/div/div[2]/input[1]").send_keys("")
        time.sleep(20)
        #点击立即提交
        element("/html/body/div/div/form/div[2]/input").click()
        time.sleep(5)
        #输入银行卡号
        bank_card = element("/html/body/div[1]/div/div[1]/div[2]/div[1]/div/p/input")
        bank_card.send_keys("6228480018865092375")
        time.sleep(15)
        #选择银行所属地
        element("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/p/input").click()
        element("/html/body/div[2]/div[2]/div[2]/div[1]/ul/li[1]").click()
        time.sleep(5)
        #点击确定按钮
        element("/html/body/div[2]/div[2]/div[4]/a[1]").click()
        time.sleep(5)
        #点击领取现金
        element("/html/body/div[1]/div/div[2]/button").click()
        time.sleep(5)
        