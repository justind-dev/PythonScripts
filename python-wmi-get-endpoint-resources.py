import wmi
import getpass
g = 'start'
while g != 'exit' or g != 0:
    g = input("Enter computer ip : ") 
    u = input('Enter Username in the format domain\\username :')
    p = getpass.getpass(prompt='Enter the password: ',stream=None)
    totalDisks = 0
    print('-'*25,'*'*11,'-'*25)
    c = wmi.WMI(g, user=u, password=p)


    try:
        for disk in c.Win32_LogicalDisk(['DeviceID', 'Size','FreeSpace','SystemName'], DriveType=3):
            systemName = disk.SystemName
            sizeGB = round(int(disk.Size) / 1000000000, 2)
            usedGB = round(int(disk.FreeSpace) / 1000000000, 2)
            freeSpace = int(sizeGB) - int(usedGB)
            diskUtilization = round(int(usedGB)/int(sizeGB),3)*100
            diskID = disk.DeviceID
            totalDisks += 1
            print('Host: {0} | Disk Letter: {1} | Total Size: {2} GB| Total Used: {3} GB| Free Space {4} GB| Utilization: {5}%'.format(systemName, diskID, sizeGB, usedGB, freeSpace, diskUtilization))
        print('TOTAL NUMBER OF DISKS {0}'.format(totalDisks))
    except:
        print('Could not retrieve disk information.')
    totalProcessors = 0
    processorMaxSpeed = 0

    try:
        for processor in c.Win32_Processor(['MaxClockSpeed', 'SocketDesignation', 'DeviceID','SystemName']):
            procID = processor.DeviceID
            procSpeed = round(int(processor.MaxClockSpeed) / 1000, 2)
            totalProcessors += 1
            procSocket = processor.SocketDesignation[-4:]
            if (processor.MaxClockSpeed > processorMaxSpeed):
                processorMaxSpeed = processor.MaxClockSpeed
            print('Processor ID: {0} | Socket Location: {1} | Max Speed: {2} GHz'.format(procID, procSocket, procSpeed))
        processorMaxSpeed = round(processorMaxSpeed / 1000, 2)
        print('Total Processors: {0} | Processors Speed: {1} GHz'.format(totalProcessors, processorMaxSpeed))
    except:
        print('Could not retrieve processor information')
    print('--------------------------------------------------')
    
    try:
        for memory in c.Win32_PhysicalMemory(['Capacity']):
            sizeMemory = round(int(memory.Capacity) / (1024 * 1024 * 1024))
            print('Total Memory: {0} GB'.format(sizeMemory))
    except:
        print('Could not retrieve memory information.')
    print('-'*25,'*'*11,'-'*25)