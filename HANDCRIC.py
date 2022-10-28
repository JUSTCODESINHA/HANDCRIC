import random as rd
import time
import os
import CallHandling

'''
----------------------------------------------------------
FUNCTION DEFINED IN CallHandling.py                      |
Class Name :- ProgramCall()                              |
Functions used till :- 1. IsRange(Start , Stop , param)  |
---------------------------------------------------------|

'''         



CheckRange = CallHandling.ProgramCall()


def Toss():
    global USR_NM

    TossMain = ["HEAD", "TAILS"]
    TOSS_COMP = ["HEAD", "TAILS"]

    USR_NM = input("ENTER YOUR NAME => ")

    TossUser = input("ENTER YOUR TOSS CHOICE => ")
    TossComp = rd.choice(TOSS_COMP)
    CoinToss = rd.choice(TossMain)

    # WHEN USER WON TOSS
    if TossUser == CoinToss:
        UsrChoice = input('''YOU HAVE WON THE TOSS WHAT DO YOU WANT TO DO "
                              FOR BATTING(B) AND FOR BOWLING(b) =>      ''')
        if UsrChoice == "B":
            print(f"{USR_NM.upper()} HAS WON THE TOSS AND ELECTED FOR BATTING FIRST !")
            BatFirst()

        elif UsrChoice == "b":
            print(f"{USR_NM.upper()} HAS WON THE TOSS AND ELECTED FOR BOWLING FIRST !")
            BatSecond()



    # WHEN COMPUTER HAS WON THE TOSS
    elif TossComp == CoinToss or TossUser != CoinToss:
        TurnSelectionUsr = int(input("ENTER A NUMBER BETWEEN (1 AND 10) => "))

        if CheckRange.IsInRange(1,10,TurnSelectionUsr) == False:
            time.sleep(4)
            print("------------INVALID INPUT !-------------")
            print("===========GAME RESTARTING !============")
            time.sleep(4)
            os.system('cls')
            Toss()

        elif CheckRange.IsInRange(1,10,TurnSelectionUsr) == True:
            TurnSelectionComp = rd.randint(1, 10)

            if TurnSelectionUsr % TurnSelectionComp == 0:
                print("COMPUTER HAS WON THE TOSS AND ELECTED TO BAT FIRST !")
                BatSecond()
            elif TurnSelectionUsr % TurnSelectionComp != 0:
                print("COMPUTER HAS WON THE TOSS AND ELECTED TO BALL FIRST !")
                BatFirst()



    # LITTLE BIT EXCEPTION , IF USER TOSS GETS SAME WITH THE TOSS OF THE COMPUTER
    elif TossComp == TossUser:
        uSelec = int(input("ENTER A NUMBER BETWEEN (1 TO 10 => "))

        if CheckRange.IsInRange(1,10,uSelec) == False:
            time.sleep(4)
            print("------------INVALID INPUT !-------------")
            print("===========GAME RESTARTING !============")
            time.sleep(4)
            os.system('cls')
            Toss()

        elif CheckRange.IsInRange(1,10,uSelec) == True:
            cSelec = rd.randint(1, 10)

            if uSelec % cSelec == 0:
                uDesci = input('''YOU HAVE WON THE TOSS WHAT DO YOU WANT TO DO 
                              BATTING (B) AND BOWLING (b) =>           ''')
                if uDesci == "B":
                    BatFirst()
                elif uDesci == "b":
                    BatSecond()

            elif uSelec % cSelec != 0:
                cChoice = rd.choice(["BATTING", "BOWLING"])
                if cChoice == "BATTING":
                    print('''COMPUTER HAS WON TOSS AND ELECETD TO BAT FIRST !''')
                    BatSecond()

                elif cChoice == "BOWLING":
                    print("COMPUTER HAS WON TOSS AND ELECETD TO BOWL FIRST !")
                    BatFirst()


# HERE BAT FIRSST REFERS TO THE USERS BATTING TURN WILL BE FIRST
def BatFirst():
    global WaitingPrompt

    print('\n')
    DecideOver = int(input("HOW MANY OVERS WOULD YOU LIKE TO PLAY => "))
    if (len(str(DecideOver)) == 0):
        time.sleep(4)
        print("------------INVALID INPUT !-------------")
        print("===========GAME RESTARTING !============")
        time.sleep(4)
        os.system('cls')
        Toss()

    else:
        Ballsplayed = 0
        TotalBallsToPlay = 6 * (DecideOver)
        RunScored = 0
        PlayChances = 5
        CompBowlingBowls = [0,1, 2, 3, 4, 5, 6]

        while (Ballsplayed < TotalBallsToPlay):

            CompBowling = rd.choice(CompBowlingBowls)
            print("\n")
            UsrBatting = int(input("ENTER YOUR RUNS BETWEEN (0 TO 6) => "))

            if CheckRange.IsInRange(0,6,UsrBatting) == False:
                time.sleep(4)
                print("------------INVALID INPUT !-------------")
                print("===========GAME RESTARTING !============")
                time.sleep()
                os.system('cls')
                Toss()

            elif CheckRange.IsInRange(0,6,UsrBatting) == True:
                if (UsrBatting == CompBowling):
                    PlayChances -= 1
                    RunScored += 0
                    print(f"OH NO WICKETS LOST ! , WICKETS LEFT => {PlayChances} ")
                    print(f"RUNS SCORED => {RunScored}")

                elif (PlayChances == 0):
                    break

                else:
                    PlayChances -= 0
                    RunScored += UsrBatting
                    print(f"RUNS SCORED => {RunScored}")

            Ballsplayed += 1

        print('\n')
        print(f"TOTAL RUNS SCORED => {RunScored} AND WICKETS LEFT => {PlayChances}")
        print(f"TOTAL OVERS PLAYED => {Ballsplayed / 6}")
        print("\n")
        print(F"TARGET FOR COMPUTER = {RunScored + 1} RUNS  IN {Ballsplayed / 6} OVERS")
        print("===========================FIRST INNINGS OVER==============================")
        time.sleep(8)
        os.system('cls')

        ControlToEnd = input("PRESS ANY KEY TO CONTINUE => ")

        if len(ControlToEnd) == 0:

            print("===========================SECOND INNINGS STARTING============================")
            time.sleep(4)

            #Computer Chasing Turn
            TargetToChase =  RunScored
            BallsplayedC = 0
            TotalBallsToPlayC = 6 * (DecideOver)
            ChaseScore = 0  # Sore towards the target
            PlayChancesC = 5


            while BallsplayedC < TotalBallsToPlayC:

                CompBatting = rd.randint(0, 6)
                print("\n")
                UserBowling = int(input("ENTER THE BOWLING RANGES BETWEEN (0 TO 6) => "))

                if CheckRange.IsInRange(0,6,UserBowling) == False:
                    time.sleep(4)
                    print("------------INVALID INPUT !-------------")
                    print("===========GAME RESTARTING !============")
                    time.sleep(4)
                    os.system('cls')
                    Toss()

                elif CheckRange.IsInRange(0,6,UserBowling) == True:
                    if (CompBatting == UserBowling):
                        PlayChancesC -= 1
                        ChaseScore += 0
                        print(f"OH NO WICKETS LOSED ! , WICKETS LEFT => {PlayChancesC} ")
                        print(f"RUNS SCORED => {ChaseScore}")

                    elif PlayChancesC == 0:
                        print("-----------COMPUTER INNNINGS COME TO END-------------")
                        break

                    else:
                        PlayChancesC -= 0
                        ChaseScore += CompBatting
                        print(f"RUNS SCORED => {CompBatting}")

            BallsplayedC += 1
            print(f"TOTAL RUNS SCORED COMPUTER  => {ChaseScore}")

            WinDiff = TargetToChase - ChaseScore

            if ChaseScore < TargetToChase:
                print(f"-------------------OH HO THIS TIME {USR_NM.upper()} WON THE MATCH BY {WinDiff} RUNS ---------------------")
                print("------------------------------COMPUTER LOST THE MATCH-------------------------------")
            else:
                print("----------------------------OH HO COMPUTER HAS WON THE MATCH-------------------------------")
                print(f"--------------------------SO SAD {USR_NM.upper()} HAS LOST THE MATCH---------------------------")


            ControlToEnd = input("PRESS ANY KEY TO CONTINUE => ")
            if len(ControlToEnd) == 0:
                time.sleep(6)
                os.system('cls')
                WaitingPrompt = input("DO YOU WANT TO PLAY THE GAME AGAIN => ")



# HERE BAT SECOND REFERS TO THE USERS BATTING TURN WILL BE SECOND
def BatSecond():

    global WaitingPrompt

    #COMPUTER TURN
    print("\n")
    DecideOver = int(input("HOW MANY OVERS DO YOU WANT TO PLAY => "))
    if len(str(DecideOver)) == 0:
        time.sleep(4)
        print("------------INVALID INPUT !-------------")
        print("===========GAME RESTARTING !============")
        os.system('cls')
        Toss()

    else:
        BallsplayedC = 0
        TotalBallsToPlayC = 6 * (DecideOver)
        RunScoredC = 0
        PlayChancesC = 5
        CompBattingRuns = [0,1, 2, 3, 4, 5, 6]

        while (BallsplayedC < TotalBallsToPlayC):

            CompBatting = rd.choice(CompBattingRuns)
            print("\n")
            UsrBowling = int(input("ENTER THE BOWLING RANGES BETWEEN (0 TO 6) => "))

            if CheckRange.IsInRange(0,6,UserBowling) == False:
                time.sleep(4)
                print("------------INVALID INPUT !-------------")
                print("===========GAME RESTARTING !============")
                time.sleep(4)
                os.system('cls')
                Toss()

            elif CheckRange.IsInRange(0,6,UserBowling) == True:
                if (UsrBowling == CompBatting):
                    PlayChancesC -= 1
                    RunScoredC += 0
                    print(f"OH NO WICKETS LOST ! , WICKETS LEFT => {PlayChancesC} ")
                    print(f"RUNS SCORED => {RunScoredC}")

                elif (PlayChancesC == 0):
                    break

                else:
                    PlayChancesC -= 0
                    RunScoredC += CompBatting
                    print(f"RUNS SCORED => {RunScoredC}")

            BallsplayedC += 1

        print('\n')
        print(f"TOTAL RUNS SCORED => {RunScoredC} AND WICKETS LEFT => {PlayChancesC}")
        print(f"TOTAL OVERS PLAYED => {BallsplayedC / 6}")
        print("\n")
        print(F"TARGET FOR USER => {RunScoredC + 1} IN {DecideOver} OVERS")
        print("===========================FIRST INNINGS OVER==============================")
        time.sleep(8)
        os.system('cls')

        ControlToEnd = input("PRESS ANY KEY TO CONTINUE => ")
        if len(ControlToEnd) == 0:

            print("===========================SECOND INNINGS STARTING============================")
            time.sleep(4)
            
            # USER TURN TO CHASE
            TargetToChaseU = RunScoredC
            BallsplayedU = 0
            TotalBallsToPlayU = 6 * (DecideOver)
            ChaseScoreU = 0  # Sore towards the target
            PlayChancesU = 5

            while BallsplayedU < TotalBallsToPlayU:

                CompBowling = rd.randint(0, 6)
                print("\n")
                UserBatting = int(input("ENTER YOUR RUNS BETWEEN (0 TO 6) => "))

                if CheckRange.IsInRange(0,6,UsrBatting) == False:
                    time.sleep(4)
                    print("------------INVALID INPUT !-------------")
                    print("===========GAME RESTARTING !============")
                    time.sleep(4)
                    os.system('cls')
                    Toss()

                elif CheckRange.IsInRange(0,6,UsrBatting) == True:
                    if (CompBowling == UserBatting):
                        PlayChancesU -= 1
                        ChaseScoreU += 0
                        print(f"OH NO WICKETS LOSED ! , WICKETS LEFT => {PlayChancesU} ")
                        print(f"RUNS SCORED => {ChaseScoreU}")

                    elif PlayChancesU == 0:
                        print("-----------COMPUTER INNNINGS COME TO END-------------")
                        break

                    else:
                        PlayChancesU -= 0
                        ChaseScoreU += UserBatting
                        print(f"RUNS SCORED => {UserBatting}")

            BallsplayedU += 1
            print(f"TOTAL RUNS SCORED BY {USR_NM.upper()} => {ChaseScoreU}")

            WinDiff = TargetToChaseU - ChaseScoreU
            if ChaseScoreU < TargetToChaseU:
                print(f"--------------OH HO THIS TIME {USR_NM.upper()} LOSS THE MATCH BY {WinDiff} RUNS---------------")
                print("---------------------------COMPUTER HAS WON THE MATCH----------------------------")
            else:
                print(F"--------------OH GREAT ! , {USR_NM.upper()} WON THE MATCH--------------------------------")
                print("------------------------COMPUTER HAS LOST THE MATCH----------------------- ")


            ControlToEnd = input("PRESS ANY KEY TO CONTINUE => ")
            if len(ControlToEnd) == 0:
                time.sleep(5)
                os.system('cls')
                WaitingPrompt = input("DO YOU WANT TO PLAY THE GAME AGAIN => ")


os.system('cls')
print("================================== WELCOME TO HANDCRICKET GAME ====================================")



while True:
    UsrPromptWaiting = input("DO YOU WANT TO PLAY THE GAME => ")
    if UsrPromptWaiting == "yes" or UsrPromptWaiting == "YES":
        Toss()
        if WaitingPrompt == "yes" or WaitingPrompt == "YES":
            Toss()
        else:
            print("========================= THANKYOU FOR VISITING THE GAME ! =============================😊😊😊")
            time.sleep(5)
            exit()


    else:
        print("========================= THANKYOU FOR VISITING THE GAME ! =============================😊😊😊")
        time.sleep(5)
        exit()


