from collections import namedtuple

from se.clipspy_version.se_with_time_track import run as clips_run
from se.pyknow_version.se_with_track import run as pyknow_run
import matplotlib.pyplot as plt
import numpy as np
import os


try:
    # Tenta criar a pasta para salvar o gráfico
    os.mkdir('./img')
except Exception:
    pass


Data = namedtuple('Data', 'ph vazao_produto vazao_agua_lavagem injecao_neutralizante')


scenarios = [
    Data(ph=5.,
         vazao_produto=5.,
         vazao_agua_lavagem=130.,
         injecao_neutralizante=20.),
    Data(ph=5.,
         vazao_produto=5.9,
         vazao_agua_lavagem=130.,
         injecao_neutralizante=20.),
    Data(ph=5.,
         vazao_produto=5.,
         vazao_agua_lavagem=129.,
         injecao_neutralizante=20.)
]

pyknow_data = [
    pyknow_run(x.ph, x.vazao_produto, x.vazao_agua_lavagem, x.injecao_neutralizante) for _ in range(5)
    for x in scenarios
]


clipspy_data = [
    clips_run(x.ph, x.vazao_produto, x.vazao_agua_lavagem, x.injecao_neutralizante) for _ in range(5)
    for x in scenarios
]


plt.title('Comparação de tempo Clipspy vs. Pyknow')
plt.ylabel('Tempo')
plt.xlabel('Execução')
plt.plot(np.arange(len(pyknow_data)), pyknow_data, color='g', label='Pyknow')
plt.plot(np.arange(len(clipspy_data)), clipspy_data, color='r', label='Clipspy')
plt.legend()
plt.savefig('./img/comparison.png')
plt.close()
