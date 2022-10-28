
import time as TIME


class ProgramCall:
	
	@staticmethod
	def IsInRange(Start,Stop,Param):
		if Param not in range(Start,Stop+1):
			return False
		else:
			return True


	@staticmethod
	def TotalUp(**Data):
		return sum(Data)
		


	@staticmethod
	def IsNoRuns(**Param):
		collection = []
		for i in Param:
			collection.append(i)
			CheckListLen = list(map(str,collection))
			if len(CheckListLen) == 0:
				return True
			else:
				CorrectValList = list(map(int,collection))
		return TotalUp(CorrectValList)

				

	@staticmethod
	def CheckNoVal(INP):
		CheckVal = []
		for i in INP:
			CheckVal.append(INP)
			ChecKVAllen = list(map(str,CheckVal))
			if len(ChecKVAllen) == 0:
				return True
			else:
				return False



