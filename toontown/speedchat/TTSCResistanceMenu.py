# File: T (Python 2.4)

from direct.showbase import PythonUtil
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat.SCMenuHolder import SCMenuHolder
from toontown.chat import ResistanceChat
from TTSCResistanceTerminal import TTSCResistanceTerminal

class TTSCResistanceMenu(SCMenu):
    
    def __init__(self):
        SCMenu.__init__(self)
        self.accept('resistanceMessagesChanged', self._TTSCResistanceMenu__resistanceMessagesChanged)
        self._TTSCResistanceMenu__resistanceMessagesChanged()
        submenus = []

    
    def destroy(self):
        SCMenu.destroy(self)

    
    def clearMenu(self):
        SCMenu.clearMenu(self)

    
    def _TTSCResistanceMenu__resistanceMessagesChanged(self):
        self.clearMenu()
        
        try:
            lt = base.localAvatar
        except:
            return None

        phrases = lt.resistanceMessages
        for menuIndex in ResistanceChat.resistanceMenu:
            menu = SCMenu()
            for itemIndex in ResistanceChat.getItems(menuIndex):
                textId = ResistanceChat.encodeId(menuIndex, itemIndex)
                charges = lt.getResistanceMessageCharges(textId)
                if charges > 0:
                    menu.append(TTSCResistanceTerminal(textId, charges))
                    continue
            
            textId = ResistanceChat.encodeId(menuIndex, 0)
            menuName = ResistanceChat.getMenuName(textId)
            self.append(SCMenuHolder(menuName, menu))
        


