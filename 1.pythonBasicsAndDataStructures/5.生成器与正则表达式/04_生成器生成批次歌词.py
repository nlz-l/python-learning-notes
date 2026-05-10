import math

def dataset_loader(batch_size):
    """

    :param batch_size: 每批次歌词条数
    :return: 生成器,每个元素都是一批的数据
    """
    with open('./data/jaychou_lyrics.txt', 'r', encoding='utf-8') as src_f:
        #lines = [line.strip() for line in src_f.readlines()]
        lines = src_f.readlines()

        total_batch = math.ceil(len(lines) / batch_size)

        for idx in range(total_batch):
            yield lines[idx * batch_size : (idx + 1) * batch_size]

dl = dataset_loader(2)
print(next(dl))
print(next(dl))
for batch_data in dl:
    print(batch_data)
