class Date:
    def __init__(self, day, month, year): #intializing the constructure 
        self.__day = day
        self.__month = month
        self.__year = year



    def set_day(self, day): #setting day
        self.__day = day

    def set_month(self, month): #setting month
        self.__month = month

    def set_year(self, year): #setting year
        self.__year = year
    


    def get_day(self): #getting day
        return self.__day

    def get_month(self): #getting month
        return self.__month
