# Home_Care

## 1. 介绍

实现居家养老项目老人端后端

## 2. 实现逻辑和流程图

所有任务通过语音输入
经过处理服务之后转化出对应的关键词
根据关键词分发到不同的服务内容
根据不同的服务内容执行不同的服务

## 3. 服务内容

## 4. 提供接口

## 5. 目前包含的包

#### 1. File_Filter 包

- 主要目的： 实现文本->订单号
- 提供 API：

  - SetKeyWords()
  - SetDemandInfo()
  - SetFile()
  - SetUserInfo()
  - ClearInFile()
  - ClearOutFile()
  - Begin_dic = Begin(FileMode = 2 ,KeyWordMode = 2)
  - Flag = Run(Begin_dic)
  - End()
  - OutFile(FilePath , Filename)

- 注意:

  - 文件的根路径在 File_Filter 中 所以外界使用的时候应该先../从里面退出到达包外层

- 包逻辑：

  - 先用设置系列把文件加载到输入缓冲区
  - 之后调用 Begin 把缓冲区内的设置读入程序
  - 之后调用 InFile 向缓冲区内导入数据
  - 之后调用 Run 执行逻辑
  - 之后调用 OutFile 可以把输出缓冲区文件导出
  - 之后调用 End 对缓冲区进行清理

#### 2. Web_service 包

- 主要目的： 负责机器人和服务器后端的通讯
- 提供 API：

  - HttpMsg(url , type , info)

- 注意：文件的根路径在 File_Filter 中 所以外界使用的时候应该先../从里面退出到达包外层
- 包逻辑：直接调用 HttpMsg 发送信息到指定位置 只须照顾好信息就可以 无需考虑封装
