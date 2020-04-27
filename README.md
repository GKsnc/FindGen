# FindGen

一个初学者的区块链项目

## 区块链项目——防伪链

### 安装

TODO:将程序(包括redis)打包docker(未来更新，初版程序使用CLI)  

```
git clone https://gitee.com/nksnc/FindGen.git
```

安装依赖库:
```
pip install -r requirements.txt
```

安装redis

### 架构图

![架构图](https://images.gitee.com/uploads/images/2020/0201/144629_2987d444_5446993.jpeg "架构图.jpeg")

### 数据结构

[数据结构图](https://www.processon.com/view/link/5e4e3575e4b0834dd83f0454)  
TODO 图片添加

"Version" : ""，4字节，16进制int  
"PrevBlockHash" : "", 32字节，字符，（长度，类型由hash函数确定）；验证，生成hash统一排序  
"MerkleRoot" : "", 字符串  
"Timestamp": int（精确到秒）；int(time.time())  
# "Height": "", 待定  
"Nonce": "", # 记录了用于证明工作量的计算参数  
"Records" : "", 数组，记录为字典（对象）  

样本区块见[仓库](https://gitee.com/nksnc/FindGen/blob/master/sample_block.json)

>记录（Records）：  
> "version"：标识记录版本  
> "sign"：签名（由交易方签名）  
> "pub_key"：交易方的公钥  
> "crec"：  
>>"goods_id"：商品ID（商品的唯一标识）
>>"seq"：流通索引  
>>"circulate_flag"：流通标识（生产，购买。。。）  
>>"time"：时间戳  
>>"recid"：记录标识符（hash）  
>>"adress":被交易方的地址(base58)  

流通标识（circulate_flag：4字节  
生产：0x000f
分销：0x00ff
消费者购买：0x0fff
商品生命结束：0xffff
0x0000-0x000f:上链|生产|准备  
0x000f-0x0fff：分销|插件|中间流通  
0x0fff-0xffff留作备用

TODO 列表排版  
TODO 编写开发文档
