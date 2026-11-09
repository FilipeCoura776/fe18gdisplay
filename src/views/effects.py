from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect

class StyleHelper:
    @staticmethod
    def apply_glow(widget, color="#ffcc00", blur_radius=15):
        """
        Aplica um efeito de glow em qualquer widget do PySide6
        e mantém a referência viva para evitar que suma.
        """
        # Cria o efeito tendo o próprio widget como pai
        effect = QGraphicsDropShadowEffect(widget)
        effect.setBlurRadius(blur_radius)
        effect.setColor(QColor(color))
        effect.setOffset(0, 0)  # Centralizado para espalhar uniformemente
        
        # IMPORTANTE: Salva o efeito dentro do próprio widget para o Python não apagar
        widget._glow_reference = effect
        
        # Aplica o efeito
        widget.setGraphicsEffect(effect)