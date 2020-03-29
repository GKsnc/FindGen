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

"Version" : ""，4字节，16进制int  
"PrevBlockHash" : "", 32字节，字符，（长度，类型由hash函数确定）；验证，生成hash统一排序  
"MerkleRoot" : "", 字符串  
"Timestamp": int（精确到秒）；int(time.time())  
# "Height": "", 待定  
"Nonce": "", # 记录了用于证明工作量的计算参数  
"Records" : "", 数组，记录为字典（对象）  

样本区块见[仓库](https://gitee.com/nksnc/FindGen/blob/master/sample_block.json)

>记录（Records）：  
> "version"：16进制int  
> "recid"：记录编号，记录上一条记录所在（待）
> "sign"：签名算法和验证算法来定；字符型  
> "pub_key"：公私钥对生成算法确定；都使用（公私钥）base58加解密  
> "crec"：字典（对象里嵌套对象）  
>>流通记录（crec）：  
>>"goods_id"：由商品id生成确定，使用字符型（未使用编码解码方式，待优化）  
>>"seq"：int  
>>"circulate_flag"：int    这个和上面那个，int型真的可以吗  
>>"time"：浮点型（精确到秒)  
