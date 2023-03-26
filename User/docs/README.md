# User 模块

## 1. 功能简介

历史详情见开发记录

目前功能：实现与用户的交互 用户输入输出

## 2. 文件结构

1. docs 存放文档
2. User_InInfo 对用户语音进行转文字读入
3. User_Interact 与用户交流
4. User_OutInfo 输出内容到终端

## 3. 使用方法

- ChooseWords(srcfile , descpath) 从srcfile中读入关键词集合 过滤为用户选择关键词 之后存储到到descpath中
- OutInfo(srcfile) 对srcfile打印到用户终端
