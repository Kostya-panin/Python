import Viewer
import Worker
import Loger
def programstart():
    userinput=Viewer.dialog()
    if userinput=="1":
        Viewer.outputinfo(Worker.export_from_phonebook())
    if userinput=="2":
        info=1
        while (not info == "0"):
            info=Viewer.inputinfo()
            Worker.import_in_phonebook(info)
            Loger.createevent(info)
    if userinput == "0":
        exit