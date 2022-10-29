Ammount = int(input("Enter ammount of seconds: " ))
Days = int(Ammount / 86400)
Ammount = int(Ammount - Days * 86400)
Hours = int(Ammount / 3600)
Ammount = int(Ammount - Hours * 3600)
Minutes = int(Ammount / 60)
Ammount = int(Ammount - Minutes * 60)
Seconds = int(Ammount)
print ("Days: " + str(Days) + "  Hours: " + str(Hours) + "   Minutes: " + str(Minutes) + "   Secounds: " +str(Seconds))









 