# FindGen

一个初学者的区块链项目

## 区块链项目——防伪链

架构图

![架构图](https://images.gitee.com/uploads/images/2020/0201/144629_2987d444_5446993.jpeg "架构图.jpeg")

记录格式

版本：1.0

![记录格式](https://images.gitee.com/uploads/images/2020/0213/160927_0c23e06e_5446993.jpeg "记录格式")

区块：  
        "Version" : ""，4字节，16进制int  
        "PrevBlockHash" : "", 32字节，字符，（长度，类型由hash函数确定）；验证，生成hash统一排序  
        "MerkleRoot" : "", 字符串  
        "Timestamp": int（精确到秒）；int(time.time())  
        # "Height": "", 待定  
        "Nonce": "", # 记录了用于证明工作量的计算参数  
        "Records" : "", 数组，记录为字典（对象）  
            记录（Records）：  
            "ersion"："， 16进制int  
                "ign"："，签名算法和验证算法来定；字符型  
            "ub_key"："，公私钥对生成算法确定；都使用（公私钥）base58加解密  
            "rec"：""字典（对象里嵌套对象）  
                流通记录（crec）：  
                    "oods_id" ""由商品id生成确定，使用字符型（未使用编码解码方式，待优化）  
                    "eq"：int  
                    "irculate_flag"："，int    这个和上面那个，int型真的可以吗  
                    "time"："，浮点型（精确到秒）  
