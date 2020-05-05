# FindGen

一个初学者的区块链项目

## 区块链项目——防伪链

### 安装



安装redis：  
参考：<https://www.redis.com.cn/redis-installation>

克隆仓库：
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

![数据结构](https://images.gitee.com/uploads/images/2020/0505/100007_60ed80b4_5446993.png "数据结构v1.png")
详细说明见 [**系统结构说明** ](https://gitee.com/nksnc/FindGen/blob/master/FindGen%E7%B3%BB%E7%BB%9F%E7%BB%93%E6%9E%84%E8%AF%B4%E6%98%8E.md)

样本区块见[仓库](https://gitee.com/nksnc/FindGen/blob/master/block.json)

### 未来更新TODO  

-  为了方便安装，将程序打包docker（两种安装方式）并使用web访问的模式（B/S），目前使用CLI
- 多线程处理
- 共识算法的更新
- P2P网络模块
- ENA13商品ID生成，优化与添加验证模块
- 类结构调整；（Records类与Participants类；blockchain类与redis类等，方法权限管理）
- 验证模块统一；上链，发布区块，接收区块，发布记录，接受记录等

