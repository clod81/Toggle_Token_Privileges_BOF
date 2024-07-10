from havoc import Demon, RegisterCommand

def PrintList(demon):
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "Toggle privileges")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "Usage: TogglePrivsBof enable/disable PRIV_NUMBER")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "Example: TogglePrivsBof enable 20")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "Please select a number, to provide as an argument.")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "1:\tSeCreateTokenPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "2:\tSeAssignPrimaryTokenPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "3:\tSeLockMemoryPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "4:\tSeIncreaseQuotaPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "5:\tSeUnsolicitedInputPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "6:\tSeMachineAccountPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "7:\tSeTcbPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "8:\tSeSecurityPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "9:\tSeTakeOwnershipPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "10:\tSeLoadDriverPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "11:\tSeSystemProfilePrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "12:\tSeSystemtimePrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "13:\tSeProfileSingleProcessPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "14:\tSeIncreaseBasePriorityPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "15:\tSeCreatePagefilePrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "16:\tSeCreatePermanentPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "17:\tSeBackupPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "18:\tSeRestorePrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "19:\tSeShutdownPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "20:\tSeDebugPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "21:\tSeAuditPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "22:\tSeSystemEnvironmentPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "23:\tSeChangeNotifyPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "24:\tSeRemoteShutdownPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "25:\tSeUndockPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "26:\tSeSyncAgentPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "27:\tSeEnableDelegationPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "28:\tSeManageVolumePrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "29:\tSeImpersonatePrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "30:\tSeCreateGlobalPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "31:\tSeTrustedCredManAccessPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "32:\tSeRelabelPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "33:\tSeIncreaseWorkingSetPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "34:\tSeTimeZonePrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "35:\tSeCreateSymbolicLinkPrivilege")
	demon.ConsoleWrite(demon.CONSOLE_ERROR, "36:\tSeDelegateSessionUserImpersonatePrivilege")

def TogglePrivs(demonID, *param):
    TaskID: str = None
    demon: Demon = None
    demon = Demon(demonID)
    packer : Packer = Packer()

    if len(param) < 2:
        PrintList(demon)
        return False

    if len(param) > 2:
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "Too many arguments")
        return False

    packer.addint(int(param[1]))

    action = "enable"
    if param[0] == "disable":
    	action = "disable"

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, f"Tasked demon to toggle privs.")
    demon.InlineExecute(TaskID, action, "toggle_privileges_bof.x64.o", packer.getbuffer(), False)

    return TaskID

RegisterCommand(TogglePrivs, "", "toggle_privs_bof", "Toggle privileges. Launch with no parameters to see the list of PRIV_NUMBER", 0, "[ACTION] [PRIV_NUMBER]", "enable/disable 20" )
