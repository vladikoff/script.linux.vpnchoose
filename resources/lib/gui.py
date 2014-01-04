import sys
import xbmc
import xbmcaddon
import xbmcgui
import time
import subprocess

#enable localization
getLS   = sys.modules[ "__main__" ].__language__
__cwd__ = sys.modules[ "__main__" ].__cwd__


class GUI(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)
        self.msg = kwargs['msg']
        self.first = kwargs['first']
        self.doModal()


    def onInit(self):
        self.defineControls()

        self.status_label.setLabel(self.msg)
        
    def defineControls(self):
        #actions
        self.action_cancel_dialog = (9, 10)
        #control ids
        self.control_heading_label_id         = 2
        self.control_list_label_id            = 3
        self.control_list_id                  = 10
        self.control_disconnect           = 14
        self.control_usa     = 15
        self.control_uk = 16
        self.control_status           = 17     
        self.control_cancel        = 18

        self.control_status_label_id          = 100
        
        #controls
        self.heading_label      = self.getControl(self.control_heading_label_id)
        self.list_label         = self.getControl(self.control_list_label_id)
        self.list               = self.getControl(self.control_list_id)
        self.disconnect_btn        = self.getControl(self.control_disconnect)
        self.usa_btn        = self.getControl(self.control_usa)
        self.uk_btn        = self.getControl(self.control_uk)
        self.status_btn        = self.getControl(self.control_status)


        self.status_label       = self.getControl(self.control_status_label_id)


    def closeDialog(self):
        self.close()

    def onClick(self, controlId):
        # NMCLI
        # CONNECT UK:
        # nmcli con down id USEWR
        # nmcli con up id UKLON

        # CONNECT USA:
        # nmcli con down id UKLON
        # nmcli con up id USEWR
        
        # DISCONNECT:
        # nmcli con down id USEWR
        # nmcli con down id UKLON
        #

        self.msg = ""
        
                    
        #Activate connection from list
        if controlId == self.control_list_id:
            self.closeDialog()
            

        # Disconnect
        elif controlId == self.control_disconnect:
            cmd = "nmcli con down id USEWR"
            o = subprocess.check_output(cmd.split(),  stderr=subprocess.STDOUT)
            cmd2 = " nmcli con down id UKLON"
            o2 = subprocess.check_output(cmd2.split(),  stderr=subprocess.STDOUT)
            print o
            print o2
            self.status_label.setLabel(o2)

            
        # USA
        elif controlId == self.control_usa:
            cmd = "nmcli con down id UKLON"
            o = subprocess.check_output(cmd.split(),  stderr=subprocess.STDOUT)
            cmd2 = "nmcli con up id USEWR"
            o2 = subprocess.check_output(cmd2.split(),  stderr=subprocess.STDOUT)
            print o
            print o2
            self.status_label.setLabel(o2)
            
            
        #UK
        elif controlId == self.control_uk:
            cmd = "nmcli con down id USEWR"
            o = subprocess.check_output(cmd.split(),  stderr=subprocess.STDOUT)
            cmd2 = "nmcli con up id UKLON"
            o2 = subprocess.check_output(cmd2.split(),  stderr=subprocess.STDOUT)
            print o
            print o2
            self.status_label.setLabel(o2)
           
        
        #Status button
        elif controlId == self.control_status:
            cmd = "nmcli -f name,vpn con status"
            o = subprocess.check_output(cmd.split(),  stderr=subprocess.STDOUT)
            self.status_label.setLabel(o)
               
        #cancel dialog
        elif controlId == self.control_cancel:
            self.closeDialog()

    
    def onAction(self, action):
        if action in self.action_cancel_dialog:
            self.closeDialog()

    def onFocus(self, controlId):
        msg = ""
        if hasattr(self, 'status_label'):
            self.status_label.setLabel(msg)
            
