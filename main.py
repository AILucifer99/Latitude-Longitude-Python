from geopy.geocoders import ArcGIS


def fetchByName(run):
    if run == True :
        placeName = input("Enter the location name : ")

        def fetchLocationNameWise(placeName, parse) :
            if parse :
                gisObj = ArcGIS()
                result = gisObj.geocode(placeName)
                LAT = result.latitude
                LONG = result.longitude
                print(f"The latitude for {placeName} is : {LAT}")
                print(f"The longitude for {placeName} is : {LONG}")
                return LAT, LONG
            else:
                pass

        lat, long = fetchLocationNameWise(placeName, True)
        locationList = [lat, long]

        print(f"The location for {placeName} is : {locationList}")
        return locationList

L1 = fetchByName(True)




