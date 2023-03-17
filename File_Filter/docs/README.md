# File_Filter

## 1. 功能简介

1.0 从多个文档内提取出是否出现关键词

1.1 把提取出来的关键词经过一定包装 和时间和用户信息 包装成订单信息

1.2 添加了可支持的功能选择 优化文件结构

## 2. 文件结构

1. docs 存放一些文档 还有下一步的发展方向与问题
2. log 存放运行的日志
3. out 存放输出的匹配结果
4. tests 用于进行基准测试
5. File_Filter 用于存放主要逻辑
   1. handle 处理逻辑部分
   2. init 初始化部分
   3. interact 交互部分
   4. start 启动部分

## 3. 功能实现

- 多文档多关键词的匹配功能
- 支持自定义关键词选择逻辑
- 人机交互确认
- 较为完整的 log 日志
- 可根据入参选择模式

## 4. 测试结果

## 5. 使用方法

1. 所有的输入路径根路径为 File_Filter 根目录
2. 所有的导入文件的注释在开头'#'

MODE1 交互式输入路径

---

MODE2 API 导入

- Begin(FileMode = 2 ,KeyWordMode = 2)
  - 1 为交互式输入的方式 2 为文件输入的方式 默认下为 2
  - 返回的是一系列的用于 Run 的参数字典
- Run()运行程序 传入参数是 Begin 的返回字典
- End() 卸载所有的导入包
- SetKeyWords() 配置导入的关键词
- SetDemandInfo() 配置导入的需求词
- SetFile() 配置导入的文件
- SetUserInfo() 配置导入的用户信息
- Clear() 删除导入的文件

---

MODE2 手动导入

1. 把输入文件导入到 In/Files 目录
2. 把选中的文件在 In/FilePaths 中进行路径设定
3. 把用户 id 导入到 In/UseInfo
4. 把关键词导入到 In/KeyWords
5. 把关键词对应 id 导入到 In/DemandInfo
6. 最后运行 File_Filter.Begin()

## 6.标准导入文件格式

1. Userinfo

   1. `ID的格式xx为id号码 暂定10位 系统会截取后6位`
   2. `yyy-xxx` yyy 为用户信息的键 xxx 为值

2. KeyWords

   1. 直接每行一个关键词即可

3. DemandInfo

   1. yyy 为三位
   2. `yyy-xxx` yyy 为需求编码 xxx 为需求内容
