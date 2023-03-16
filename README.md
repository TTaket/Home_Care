# Home_Care

## 1. File_Filter 包

- 主要目的： 实现文本->订单号
- 提供 API：
  1. Begin(FileMode = 2 ,KeyWordMode = 2) 1 为交互式输入的方式 2 为文件输入的方式 默认下为 2
  2. End() 卸载所有的导入包
  3. SetKeyWords() 配置导入的关键词
  4. SetDemandInfo() 配置导入的需求词
  5. SetFile() 配置导入的文件
  6. SetUserInfo() 配置导入的用户信息
