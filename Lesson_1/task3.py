Ammount = int(input("Enter ammount of seconds: " ))
Days = int(Ammount / 86400)
Ammount = (Ammount - Days * 86400)
Hours = int(Ammount / 3600)
Ammount = (Ammount - Hours * 3600)
Minutes = int(Ammount / 60)
Ammount = (Ammount - Minutes * 60)
Seconds = (Ammount)
print ("Days: " + str(Days) + "  Hours: " + str(Hours) + "   Minutes: " + str(Minutes) + "   Seconds: " +str(Seconds), end="")