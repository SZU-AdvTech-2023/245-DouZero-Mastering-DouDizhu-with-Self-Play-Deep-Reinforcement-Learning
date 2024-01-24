创建并激活虚拟环境
conda create -n douzero python==3.7
conda activate douzero
安装相关依赖
cd douzero
pip3 install -r requirements.txt
安装稳定版本的 Douzero
pip3 install douzero

1.训练模型
至少拥有一块可用的 GPU，运行
python3 train.py

如果需要用多个 GPU 训练 Douzero，使用以下参数：
--gpu_devices: 用作训练的 GPU 设备名
--num_actor_devices: 被用来进行模拟（如自我对弈）的 GPU 数量
--num_actors: 每个设备的演员进程数
--training_device: 用来进行模型训练的设备
如：
python3 train.py --gpu_devices 0,1,2,3 --num_actor_devices 3 --num_actors 15 --training_device 3
在 CPU 上运行：
python3 train.py --actor_device_cpu --training_device cpu

2.评估
第 1 步：生成评估数据
python3 generate_eval_data.py
第 2 步：自我对弈
python3 evaluate.py

以下为一些重要的超参数。

--landlord: 扮演地主的智能体，可选值：random, rlcard 或预训练模型的路径
--landlord_up: 扮演地主上家的智能体，可选值：random, rlcard 或预训练模型的路径
--landlord_down: 扮演地主下家的智能体，可选值：random, rlcard 或预训练模型的路径
--eval_data: 包含评估数据的 pickle 文件
--num_workers: 用多少个进程进行模拟
--gpu_device: 用哪个 GPU 设备进行模拟。默认用 CPU

例如，可以通过以下命令评估 DouZero-ADP 智能体作为地主对阵随机智能体

python3 evaluate.py --landlord baselines/douzero_ADP/landlord.ckpt --landlord_up random --landlord_down random
