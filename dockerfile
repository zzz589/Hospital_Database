# 使用官方的 Python 镜像作为基础镜像
FROM python:3.12-slim

# 安装必需的系统依赖
RUN apt-get update && apt-get install -y libpq-dev gcc

# 设定工作目录
WORKDIR /app

# 将依赖文件复制到容器中
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 将代码复制到容器中
COPY . .

# 设置环境变量，例如数据库连接
ENV POSTGRES_USER=youruser
ENV POSTGRES_PASSWORD=yourpassword
ENV POSTGRES_DB=yourdb
ENV POSTGRES_HOST=db

# 暴露应用的端口号
EXPOSE 5000

# 设置容器启动后执行的命令
CMD ["python", "run.py"]
