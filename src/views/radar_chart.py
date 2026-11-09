import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PySide6.QtWidgets import QVBoxLayout, QWidget

class RadarChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Configuração da figura do Matplotlib com fundo transparente ou escuro (combinando com o estilo do app)
        self.figure, self.ax = plt.subplots(figsize=(2,2), subplot_kw=dict(polar=True))
        self.canvas = FigureCanvasQTAgg(self.figure)
        
        layout = QVBoxLayout(self.layout() or parent and parent.layout() or self)
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0, 0, 0, 0)

        #config padrao de angulação
        self.ax.set_theta_offset(np.pi / 2)
        
        # Estilização básica para combinar com tema dark/RPG
        self.figure.patch.set_facecolor('#03161a') # Cor de fundo do painel
        self.ax.set_facecolor('#16292d')
        
    def plot_stats(self, labels, stats_values):
        """
        Plota os dados no gráfico de radar.
        :param labels: Lista com os nomes dos atributos (ex: ['HP', 'Str', 'Mag', 'Skl', 'Spd', 'Def', 'Res'])
        :param stats_values: Lista com os valores numéricos correspondentes
        """
        self.ax.clear()

        
        # Número de variáveis
        num_vars = len(labels)
        
        # Calcula o ângulo de cada eixo no radar (dividindo o círculo em partes iguais)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        
        # O gráfico é fechado em círculo, então repetimos o primeiro valor no final
        stats_values = list(stats_values)
        stats_values += stats_values[:1]
        angles += angles[:1]
        
        # Desenha os eixos e preenche a área
        self.ax.plot(angles, stats_values, color="#ffcc0000", linewidth=2, linestyle='solid') # cor da linha
        self.ax.fill(angles, stats_values, color='#8e8372', alpha=1.0) # Preenchimento translúcido
        
        # Configura os rótulos dos atributos
        self.ax.set_theta_offset(np.pi / 2) # Começa do topo
        self.ax.set_theta_direction(-1)     # Sentido horário
        
        self.ax.set_xticks(angles[:-1])
        self.ax.set_xticklabels(labels, color='white', size=9, weight='bold')
        
        # Remove os números de escala concêntricos para ficar mais limpo
        self.ax.set_yticklabels([])
        #self.ax.grid(color="#555555FF", linestyle='--', linewidth=0.1)
        self.ax.spines['polar'].set_color('#8e8372')

        #self.ax.grid(True, color='#4c5c64', linestyle='-', linewidth=0.5)
        #self.ax.yaxis.grid(False)

        # GRADIENTE --------------------------------------------

        self.ax.grid(False)
        self.ax.yaxis.grid(False)

        max_val = 100
        num_steps = 10

        for angle in angles[:-1]:
            r_values = np.linspace(0, max_val, num_steps)
            for i in range(len(r_values) - 1):
                r_start = r_values[i]
                r_end = r_values[i+1]
                
                # O alpha (opacidade) aumenta à medida que 'r' se afasta do centro (0 -> 1)
                # Assim, perto do centro fica transparente e na borda fica opaco
                alpha_val = (i + 1) / num_steps * 0.6  # Ajuste o 0.6 para mais claro/escuro
                
                self.ax.plot(
                    [angle, angle], 
                    [r_start, r_end], 
                    color="#8e8372", 
                    linestyle='-', 
                    linewidth=1.0, 
                    alpha=alpha_val
                )

        #-------------------------------------------------------

        self.ax.set_ylim(0, 100) #limite do grafico (100% de growths representaria a linha cheia no radar)
        
        self.ax.set_theta_offset(7 * np.pi / 8) #offset para esquerda
        #self.ax.set_theta_direction(1) #sentido anti horario
        
        # Atualiza o canvas na interface
        self.canvas.draw()