# OrderInfo

## 1. 功能简介

版本 1.0： 基本实现功能 完成对外的信息传递和初步的接口封装

## 2. 文件结构

1. docs 存放一些文档 还有下一步的发展方向与问题
2. log 存放运行的日志
3. img 存放一些图片
4. tests 用于进行基准测试
5. Web_Service 用于存放主要逻辑
   1. SendHttpMsg 发送信息的逻辑层
   2. WebBase 发送信息的网络层

## 3. 功能实现

- 实现机器人对外的网络通讯（主动方)

## 4. 测试结果

## 5. 使用方法

- HttpMsg(url , type , info)
  - 功能：向 url 发送 type 类型内容为 info 的 http 包 方法为 post
  - 入参：url 地址 type 内容类型 info 信息
  - 返回值：http 的返回包
