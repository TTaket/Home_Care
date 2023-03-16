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

1. 对外 API： Begin(FileMode = 2 ,KeyWordMode = 2) 1为交互式输入的方式 2为文件输入的方式 默认下为2
2. Begin支持两个参数

---



1. 把输入文件导入到 In/Files 目录
4. 把选中的文件在 In/FilePaths 中进行路径设定
5. 把用户 id 导入到 In/UseInfo
6. 把关键词导入到 In/KeyWords
7. 把关键词对应 id 导入到 In/DemandInfo
8. 最后运行 File_Filter.Begin()
