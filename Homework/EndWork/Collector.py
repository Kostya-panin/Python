import Viewer
import Worker
import Loger

def programstart():
    userinput=None
    while(userinput != "0"):
        #Показываем главное меню
        userinput=Viewer.maindialog()
        #Если пользователь ввел 1
        if userinput=="1":
            #Запрашиваем у пользователя как бы он хотел видеть список заметок
            userinput=Viewer.dialogfiltermotes()
            #Если пользователь ввел 1
            if userinput=="1":
                #Тогда показываем список всех заметок
                Viewer.outputinfo("Ваш список заметок:")
                Viewer.outputinfo(Worker.get_list_notes('Notes\\'))
                Viewer.outputinfo("")
                #Показываем меню действий с заметками и возвращаем ответ пользователя
                userinput=Viewer.dialoglistnotes()
                #Если пользователь ввел 1
                if userinput=="1":
                    #Тогда запрашиваем имя заметки
                    namenote=Viewer.dialognamenote()
                    #Запрашиваем заголовок заметки
                    titlenote=Viewer.dialogtitlenote()
                    #Запрашиваем тело заметки
                    bodynote=Viewer.dialogbodynote()
                    #Запускаем фнкцию редактирования заметки
                    Worker.edit_note(namenote,titlenote,bodynote)   
            #Если пользователь ввел 2
                if userinput=="2":
                    #Тогда запрашиваем у пользователя имя заметки
                    userinput=Viewer.dialognamenote()
                    #Запускаем функцию чтения заметки
                    Viewer.outputinfo(Worker.read_note(userinput))
            #Если пользователь ввел 3
                if userinput=="3":
                    #тогда запрашиваем у пользователя имя заметки
                    userinput=Viewer.dialognamenote()
                    #запускаем функцию удаления заметки
                    Worker.remove_note(userinput)
            #Если пользователь ввел 2
            if userinput=="2":
                #Тогда показываем список всех заметок
                Viewer.outputinfo("Ваш список заметок отфильтрованный по дате:")
                Viewer.outputinfo(Worker.get_filter_list_notes('Notes\\'))
                Viewer.outputinfo("")
                #Показываем меню действий с заметками и возвращаем ответ пользователя
                userinput=Viewer.dialoglistnotes()
        ##Если пользователь ввел 2
        if userinput == "2":
            #Тогда запрашиваем имя заметки
            namenote=Viewer.dialognamenote()
            #Запрашиваем заголовок заметки
            titlenote=Viewer.dialogtitlenote()
            #Запрашиваем тело заметки
            bodynote=Viewer.dialogbodynote()
            #Запускаем фнкцию создания новой заметки
            Worker.new_note(namenote,titlenote,bodynote)
        if userinput == "0":
            exit