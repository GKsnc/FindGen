# FindGen

一个初学者的区块链项目

## 区块链项目——防伪链

### 安装

todo?:将整个程序(包括redis)打包进docker(未来更新，初版程序使用本地客户端)

安装依赖库:
```
sudo pip install -r requirements.txt
```

安装redis

### 架构图

![架构图](https://images.gitee.com/uploads/images/2020/0201/144629_2987d444_5446993.jpeg "架构图.jpeg")

### 数据结构

![数据结构](https://images.gitee.com/uploads/images/2020/0329/164640_a3aebf7e_5446993.png "数据结构.png")

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
