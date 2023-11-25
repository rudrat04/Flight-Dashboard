import mysql.connector

class DB:
    def __init__(self):
        
        try:
            # engine = create_engine("mysql+pymysql://admin:911Pentagon@database-1.codzmntflx6t.ap-northeast-1.rds.amazonaws.com/flights")
            # # {root}:{password}@{url}/{database}
            # df.to_sql('flights', con = engine)
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Rudra@2002",
                database="flights"
            )

            self.mycursor = self.conn.cursor()
            print("Connection Established")
        except:
            print("Connection Error")
            
    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
                              SELECT DISTINCT(Source) FROM flight
                                UNION
                                SELECT DISTINCT(Destination) FROM flight
                              """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
        return city
    
    def fetch_all_flights(self, source, destination):
        self.mycursor.execute("""
                              SELECT Airline, Route, Dep_Time, Duration,Price FROM flight
                              WHERE Source = '{}' AND Destination = '{}'
                              """.format(source,destination)
                              )
        data = self.mycursor.fetchall()
        return data
    
    def fetch_airline_freq(self):
        airline = []
        frequency = []
        self.mycursor.execute(
        """
        SELECT Airline,COUNT(*) FROM flight
        group by Airline
        """
        )
        data = self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline,frequency
        
    def busy_airport(self):
        city = []
        frequency = []
        self.mycursor.execute(
        """
        SELECT Source, COUNT(*) FROM (SELECT Source FROM flight
								UNION ALL
								SELECT Destination FROM flight) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """
        )
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city,frequency
        
        
    def daily_frequency(self):
        date = []
        frequency = []
        self.mycursor.execute(
        """
        SELECT Date_of_Journey, COUNT(*) FROM flight
        GROUP BY Date_of_Journey
        """
        )
        data = self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date,frequency
        
