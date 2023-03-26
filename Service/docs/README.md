# Service 模块

## 1. 功能简介

历史详情见开发记录

目前功能：订单号的生成

## 2. 文件结构

1. docs 存放文档
2. OrderInfo 生成订单并且发送
3. Web_Service 封装好的网络接口

## 3. 使用方法

- Order(src , desc) 把 src 里的需求读取出来自动生成订单并发送 把回复包内容发送到 desc
- HttpMsg(url , typ , info) 提供url typ 和info 发送信息到指定url
