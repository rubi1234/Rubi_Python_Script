def GUI():
    print("*********GUI TEST RESULTS**********\n")
    list=[]
    Project_Number=0
    Line_Number=0
    Debug=0
    Release=0
    Compiler_line=0
    Eroor_type1="error: #error"
    Eroor_type2=": error:"
    Error_Number=0
    str=" "
    Eroor_type4="_mainapp: fatal error:"    
    Eroor_type5="message: fatal error:"      
    Eroor_type6="undefined reference to"
    Eroor_type7="_mainapp: undefined reference to"   
    Eroor_type8="message: undefined reference to"   
    file=open("C:\Modus\outG5.log","r+")
    Error_type1_count=0
    Error_type1_match=0
    for row in file:
        ##Project_Number Number GUI
        if(row.find('Started logging')!=-1):
            Project_Number=Project_Number+1
            print("Project_Number number",Project_Number)
        ##Application Name
        if(row.find('Project_Number')!=-1):
            Line_Number=Line_Number+1
            if(Line_Number==1):
                b=row.split()
                a=b[5].replace('_mainapp:','')
                print("Application: ",a)
        ##Configuration
        if(Debug==0 and Release==0):
            if(row.find('Debug')!=-1):
                print("Configuration Debug")
                Debug=Debug+1
            if(row.find('Release')!=-1):
                print("Configuration: Release")
                Release=Release+1
        ##Compiler
        if(row.find('Invoking:')!=-1):
            Compiler_line=Compiler_line+1
            if(Compiler_line==1):
                b=row.split()
                b.remove('Invoking:')
                print("Toolchain:",str.join(b))
        ##Error
        if(row.find('.c: In function')!=-1):
            row = row.strip('\n')
            print(row)

        if(row.find('.o: In function')!=-1):
            row=row.strip('\n')
            print(row)
        if(row.find('warning:')!=-1):
            print(row)
        if(row.find(Eroor_type1)!=-1):
            Error_Number=Error_Number+1
            list.append(row)
            Error_type1_count=Error_type1_count+1
            for a in range(Error_type1_count):
                if(list[a]==row):
                     Error_type1_match=Error_type1_match+1
            if(Error_type1_match>1):
                pass
            else:
                Error_type1_match=0
                print(row)
        
        elif(row.find(Eroor_type2)!=-1):
            Error_Number=Error_Number+1
            row = row.strip('\n')
            print(row)
            print(file.readline())
        if(row.find(Eroor_type4)!=-1):
            Error_Number=Error_Number+1
            pass
        elif(row.find(Eroor_type5)!=-1):
            Error_Number=Error_Number+1
            pass
        elif(row.find('fatal error:')!=-1):
            Error_Number=Error_Number+1
            print(row)
        if(row.find(Eroor_type7)!=-1):
            pass
        elif(row.find(Eroor_type8)!=-1):
            pass
        elif(row.find(Eroor_type6)!=-1):
           print(row)
            
        ##Result
        if(row.find('Parser')!=-1):
            if(Error_Number>0):
                print('Fail')
                print('\n')
                Error_Number=0
                Debug=0
                Release=0
                Line_Number=0
                Compiler_line=0
            else:
                Debug=0
                Release=0
                Line_Number=0
                Compiler_line=0
                print('Pass')
                print('\n')


def CLI():
    print("###############################################################################\n")
    print("*********CLI TEST RESULTS*************\n")
    Project_Number=0
    Line_Number=0
    Debug=0
    Release=0
    Compiler_line=0
    Eroor_type1="error: #error"
    Eroor_type2=": error:"
    error3=0
    Error_Number=0
    str=" "
    Eroor_type4="_mainapp: fatal error:"
    Eroor_type5="message: fatal error:"
    Eroor_type6="undefined reference to"
    Eroor_type7="_mainapp: undefined reference to"   
    Eroor_type8="message: undefined reference to"   
    file=open("C:\Modus\outCLI1.txt","r")
    for row in file:
    ##Project_Number Number CLI
        if(row.find('Initializing')!=-1):
            Project_Number=Project_Number+1
            print("Project_Number Number:",Project_Number)
            b=row.split()
            application=b[3]
            Compiler=b[6]
            print("Application:",application)
            print("Toolchain:",Compiler)

        ##Configuration
        if(Debug==0 and Release==0):
            if(row.find('Debug')!=-1):
                print("Configuration: Debug")
                Debug=Debug+1
            if(row.find('Release')!=-1):
                print("Configuration: Release")
                Release=Release+1
          ##Errors
        if(row.find('.c: In function')!=-1):
            row = row.strip('\n')
            print(row)

        if(row.find('.o: In function')!=-1):
            row=row.strip('\n')
            print(row)
        if(row.find('warning:')!=-1):
            print(row)
        if(row.find(Eroor_type1)!=-1):
            Error_Number=Error_Number+1
            print(row)
        elif(row.find(Eroor_type2)!=-1):
            Error_Number=Error_Number+1
            row = row.strip('\n')
            print(row)
            print(file.readline())
        if(row.find(Eroor_type4)!=-1):
            Error_Number=Error_Number+1
            pass
        elif(row.find(Eroor_type5)!=-1):
            Error_Number=Error_Number+1
            pass
        elif(row.find('fatal error:')!=-1):
            row = row.strip('\n')
            Error_Number=Error_Number+1
            print(row)
        if(row.find(Eroor_type7)!=-1):
            pass
        elif(row.find(Eroor_type8)!=-1):
            pass
        elif(row.find(Eroor_type6)!=-1):
           print(row)
        if(row.find('Stop')!=-1):
            row = row.strip('\n')
            Error_Number=Error_Number+1
            print(row)
        if(row.find('= Artifact mainapp complete =')!=-1):
            print("Result : Pass")

    if(Error_Number>0):
        Error_Number=0
        print("Result: Fail")
##FUNCTION CALL
GUI()
CLI()











































