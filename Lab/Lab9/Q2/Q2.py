from datetime import datetime 
import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None

    @property
    def element(self):
        """Return the dom element """
        if not self._element:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element

    @abstractmethod
    def drawWidget(self):
        pass


def jump_sound():
    audio = document.createElement("audio")
    audio.src = "./sounds/rabbit_jump.wav"
    return audio

class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.counter = 1
        self.is_paused = False 
        self.interval_id = None 

    def on_click(self, event):
        if self.is_paused:
            self.button.innerText = "Pause"
            self.is_paused = False
            on_setInterval = create_proxy(self.on_setInterval)
            self.interval_id = js.setInterval(on_setInterval, 100)
        else:
            self.button.innerText = "Play"
            self.is_paused = True
            js.clearInterval(self.interval_id)

    def on_setInterval(self):
        self.counter += 1
        if self.counter > 20:
            self.jump_sound.play()
            self.counter = 1
        self.image.src = f"images/frame-"+str(self.counter)+".png"

    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = f"images/frame-1.png"
        on_setInterval = create_proxy(self.on_setInterval)
        self.interval_id = js.setInterval(on_setInterval, 100)
        self.element.appendChild(self.image)
        self.jump_sound = js.eval("new Audio('./sounds/rabbit_jump.wav')")
        self.button = document.createElement("button")
        self.button.innerText = "Pause"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)

if __name__ == '__main__':
    animation = AnimationWidget('container')
    animation.drawWidget()