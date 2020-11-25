##server项目结构说明
server项目基本结构如下：
```
|Server
|--app/
|----apis/
|----configs/
|----models/
|----tools/
|--conf/
|--docs/
```
各级文件夹使用介绍：

- app: 代码核心
    - app/apis: 所有视图文件代码
    - app/configs: 配置文件代码
    - app/models: 所有模型文件代码
    - app/tools: 所有工具模块代码
- conf: 配置
- docs: 文档

## 依赖
- 安装
```
pip3 install -r conf/requirements.txt
```
- 写入配置
```
pip3 freeze > conf/requirements.txt
```