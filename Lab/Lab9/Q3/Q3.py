from datetime import datetime 
import js
from pyodide.ffi import create_proxy
from pyscript import document
from abc import ABC, abstractmethod
import random

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


class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.counter = 1
        self.interval = None

    def on_click(self, event):
        if self.button.innerText == "pause":
            self.button.innerText = "play"
            js.clearInterval(self.interval)
            self.jump_sound.pause()
        else:
            self.button.innerText = "pause"
            on_setInterval = create_proxy(self.on_setInterval)
            self.interval = js.setInterval(on_setInterval, 100)

    def on_setInterval(self):
        self.counter += 1
        if self.counter > 20:
            self.counter = 1
            self.jump_sound.play()
        self.image.src = f"./images/frame-{self.counter}.png"

    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        self.element.appendChild(self.image)

        self.button = document.createElement("button")
        self.button.innerText = "play"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)

        self.jump_sound = document.createElement("audio")
        self.jump_sound.src = "./sounds/rabbit_jump.wav"
        self.element.appendChild(self.jump_sound)


class ColorfulAnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.counter = 1
        self.interval = None

    def on_click(self, event):
        if self.play_button.innerText == "pause":
            self.play_button.innerText = "play"
            js.clearInterval(self.interval)
            self.jump_sound.pause()
        else:
            self.play_button.innerText = "pause"
            on_setInterval = create_proxy(self.on_setInterval)
            self.interval = js.setInterval(on_setInterval, 100)

    def on_setInterval(self):
        self.counter += 1
        if self.counter > 20:
            self.counter = 1
            self.jump_sound.play()  # Play sound on frame 1
        self.image.src = f"./images/frame-{self.counter}.png"

    def randomColor_on_click(self, event):
        color = f"#{''.join([random.choice('0123456789ABCDEF') for _ in range(6)])}"
        self.image.style.backgroundColor = color

    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        self.element.appendChild(self.image)

        self.play_button = document.createElement("button")
        self.play_button.innerText = "play"
        self.play_button.style.width = "600px"
        self.play_button.onclick = self.on_click
        self.element.appendChild(self.play_button)

        self.color_button = document.createElement("button")
        self.color_button.innerText = "Random Color"
        self.color_button.style.width = "600px"
        self.color_button.onclick = self.randomColor_on_click
        self.element.appendChild(self.color_button)

        self.jump_sound = document.createElement("audio")
        self.jump_sound.src = "./sounds/rabbit_jump.wav"
        self.element.appendChild(self.jump_sound)


if __name__ == "__main__":
    widget = ColorfulAnimationWidget("container")
    widget.drawWidget()