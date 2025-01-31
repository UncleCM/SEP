from datetime import datetime 
import js
from pyscript import document
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

def getTime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")

class THBtoUSD(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)

    def on_click(self, event):
        text = self.input_text.value
        try:
            thb_amount = float(text)
            usd_amount = thb_amount / 30
            js.alert(f"{thb_amount} THB is approximately {usd_amount:.2f} USD")
        except ValueError:
            js.alert("Please enter a valid number")

    def drawWidget(self):
        self.input_text = document.createElement("input", type="text")
        self.input_text.style.width = "600px"
        self.element.appendChild(self.input_text)

        self.button = document.createElement("button")
        self.button.innerText = "THB to USD"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)

class USDtoTHB(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)

    def on_click(self, event):
        text = self.input_text.value
        try:
            thb_amount = float(text)
            usd_amount = thb_amount * 30
            js.alert(f"{thb_amount} USD is approximately {usd_amount:.2f} THB")
        except ValueError:
            js.alert("Please enter a valid number")

    def drawWidget(self):
        self.input_text = document.createElement("input", type="text")
        self.input_text.style.width = "600px"
        self.element.appendChild(self.input_text)

        self.button = document.createElement("button")
        self.button.innerText = "USD to THB"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)

if __name__ == "__main__":
    widget = USDtoTHB("container")
    THBtoUSD = THBtoUSD("container")
    widget.drawWidget()
    THBtoUSD.drawWidget()