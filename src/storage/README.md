### 使用说明

- 创建一个与redis数据库的连接(用户层未提供接口)
    con = Redis(Host='127.0.0.1',Db='0')  
    Db表示数据库名，这里默认无密码，端口为6379，可以传入Port和Password参数进行修改
- 存入一个区块  
    con.set(flag,block)  
    flag唯一表示一个区块，可为区块头的哈希，block为区块的内容（json字符串)  
    若存入成功返回1，失败返回0
- 获取一个区块的信息  
    con.jget(key)
    返回的内容为字典(json字符解析python对象返回)
- 同步（非p2p，暂定）  
    con.sync(ip,port)  
    ip为需要同步的主机ip，port为端口，默认为6379
- 写入磁盘
    con.save()
