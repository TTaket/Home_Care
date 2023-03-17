# Home_Care

## 1. File_Filter 包

- 主要目的： 实现文本->订单号
- 提供 API：
  - Begin(FileMode = 2 ,KeyWordMode = 2)
    - 1 为交互式输入的方式 2 为文件输入的方式 默认下为 2
    - 返回的是一系列的用于 Run 的参数字典
  - Run()运行程序 传入参数是 Begin 的包
  - End() 卸载所有的导入包
  - SetKeyWords() 配置导入的关键词
  - SetDemandInfo() 配置导入的需求词
  - SetFile() 配置导入的文件
  - SetUserInfo() 配置导入的用户信息
  - Clear() 删除导入的文件
- 文件的根路径在 File_Filter 中 所以外界使用的时候应该先../从里面退出到达包外层
