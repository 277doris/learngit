#coding:utf-8
import xlrd
def get_webinfo(path):
    #字典形式
    web_info = {}
    #以只读形式打开文件，如遇编码格式问题，导入codecs 
    config = open(path)
    #将webinfo中的信息遍历读取
    for line in config:
        #使用 = 进行分割并返回一个列表
        result = [ele.strip() for ele in line.split(' = ')]
        #将列表转换成字典，并更新字典到webinfo中
        web_info.update(dict([result]))
    return web_info
         
def get_userinfo(path):
    #列表形式
    user_info = []
    #以只读形式打开文件
    config = open(path)
    #将userinfo中的信息遍历读取
    for line in config:
        #定义一个字典
        user_dict = {}
        #使用 = 进行分割并返回一个列表
        result = [ele.strip() for ele in line.split(' ')]
        for r in result:
            account = [ele.strip() for ele in r.split('=')]
            #将用户数据添加到字典中
            user_dict.update(dict([account]))
        #将用户字典添加到列表中
        user_info.append(user_dict)
    return user_info 

class XlUserinfo(object):
    #初始化
    def __init__(self, path = ''):
        self.xl = xlrd.open_workbook(path)
    #得到数据表中所有数据  
    def get_sheet_info(self):
        #逐行读取Excel表格，并将uname，upwd组成一个字典
        listkey = ['uname', 'upwd', 'ucode']
        infolist = []
        for row in range(1, self.sheet.nrows):
            info = self.sheet.row_values(row)
            tmp = zip(listkey, info)
            infolist.append(dict(tmp))
        return infolist
    #通过名字获取表格
    def get_sheetinfo_by_name(self, name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()
    #通过索引获取表格
    def get_sheetinfo_by_index(self, index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_sheet_info()

if __name__ == '__main__':     
#     #r代表只读形式，读取txt中的文件
#     webinfo = get_webinfo(r'C:\eclipse\workspace\TestH5\webinfo.txt')
#     for key in webinfo:
#         print(key, webinfo[key])
#     user_info = get_userinfo(r'C:\eclipse\workspace\TestH5\userinfo.txt')
#     for l in user_info:
#         print(l)
#     print(user_info)
    #读取Excel文件
    xinfo = XlUserinfo(r'C:\Users\22648\Desktop\userinfo.xlsx')
    #通过sheet表单的索引读取
    info = xinfo.get_sheetinfo_by_index(0)
    print(info)
    #通过读取文件名读取信息
    info = xinfo.get_sheetinfo_by_name('Sheet1')
    print(info)   