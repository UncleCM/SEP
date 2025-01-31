import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod
from datetime import datetime

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None

    @property
    def element(self):
        """Return the dom element"""
        if not self._element:
            self._element = document.querySelector(f'#{self.element_id}')
        return self._element
    
    @abstractmethod
    def drawWidget(self):
        pass

#########################################################################################

def getTime():
    now = datetime.now()
    return now.strftime("%M/%D/%Y, %H:%M:%S")

class Notification(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)

    def on_click(self, event):
        text = self.input_text.value
        js.alert("Hello " + text + "at" + getTime())

    def drawWidget(self):
        self.input_text = document.createElement('input', type='text')
        self.input_text.style.width = '600px'
        self.element.appendChild(self.input_text)

        self.button = document.createElement('button')
        self.button.innerText = 'Click me!'
        self.button.style.width = '600px'
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)

if __name__ == '__main__':
    notification = Notification('container')
    notification.drawWidget()