import arcpy
import math
import sys
s
#"Edit the path to be the path the selenium folder is in"
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def decdeg2dms(dd):
    mnt,sec = divmod(dd*3600,60)
    deg,mnt = divmod(mnt,60)
    return (deg,mnt,sec)


op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome()

#Input Solar Calculator path driver.get(Path of Calculator)
driver.get("C:/Users/prati/PycharmProjects/pythonProject4/NOAA Solar Position Calculator.html")


#Input the folder for county shapefile arcpy.env.workspace = r"Path of folder of shapefile"
arcpy.env.workspace = r"C:\GIS\Image_Footprint-PhotoCenters\Used_in_Production"
shapefile = "Tier1_Image_PhotoCenters.shp"
fields = arcpy.ListFields(shapefile)
rows = arcpy.SearchCursor(shapefile)

Easting = "Easting"
Northing = "Northing"
Image_ID = "Image_ID"
Height = "Height"
Local_Time = "Local_Time"
SunAngle = "SunAngle"
SolarDecl = "SolarDecl"
SolarAzi = "SolarAzi"
SolarZeni = "SolarZeni"
cursor = arcpy.UpdateCursor(shapefile)

for row in cursor:
    first = 0
    for i in range(len(row.Image_ID)):
        if row.Image_ID == "_":
            first = i
            break
    month = int(row.Image_ID[4:6])
    day = int(row.Image_ID[6:8])

    hours = int(row.Local_Time[0:2])
    minutes = int(row.Local_Time[3:5])
    seconds = int(row.Local_Time[6:8])

    latitude = row.Northing
    longitude = row.Easting

    select = Select(driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td[1]/center/select"))
    select.select_by_visible_text("Enter Lat/Long -->")

    driver.find_element_by_xpath("/html/body/form/center/form/center/table[2]/tbody/tr[2]/td[1]/center/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/form/center/table[2]/tbody/tr[2]/td[2]/center/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/form/center/table[2]/tbody/tr[2]/td[3]/center/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/form/center/table[2]/tbody/tr[2]/td[4]/center/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/form/center/table[2]/tbody/tr[2]/td[5]/center/input").clear()

    # latitude


    lat = decdeg2dms(latitude)
    print(longitude)
    long = decdeg2dms(-longitude)
    print(long)

    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td[3]/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td[3]/input").send_keys(int(lat[0]))

    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td[4]/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td[4]/input").send_keys(int(lat[1]))

    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td[5]/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td[5]/input").send_keys(int(lat[2]))

    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[3]/td[3]/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[3]/td[3]/input").send_keys(int(long[0]))

    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[3]/td[4]/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[3]/td[4]/input").send_keys(int(long[1]))

    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[3]/td[5]/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[3]/td[5]/input").send_keys(int(long[2]))

    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td[6]/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td[6]/input").send_keys(5)

    select_month = Select(driver.find_element_by_xpath("/html/body/form/center/form/center/table[1]/tbody/tr[2]/td[1]/select"))
    if(month == 1):
        select_month.select_by_visible_text("January")
    elif(month == 2):
        select_month.select_by_visible_text("February")
    elif(month == 3):
        select_month.select_by_visible_text("March")
    elif (month == 4):
        select_month.select_by_visible_text("April")
    elif (month == 5):
        select_month.select_by_visible_text("May")
    elif (month == 6):
        select_month.select_by_visible_text("June")
    elif (month == 7):
        select_month.select_by_visible_text("July")
    elif (month == 8):
        select_month.select_by_visible_text("August")
    elif (month == 9):
        select_month.select_by_visible_text("September")
    elif (month == 10):
        select_month.select_by_visible_text("October")
    elif (month == 11):
        select_month.select_by_visible_text("November")
    else:
        select_month.select_by_visible_text("December")

    driver.find_element_by_xpath("/html/body/form/center/form/center/table[1]/tbody/tr[2]/td[2]/center/input").clear()
    driver.find_element_by_xpath("/html/body/form/center/form/center/table[1]/tbody/tr[2]/td[2]/center/input").send_keys(day)

    driver.find_element_by_xpath("/html/body/form/center/form/center/table[1]/tbody/tr[2]/td[4]/center/input[1]").clear()
    driver.find_element_by_xpath("/html/body/form/center/form/center/table[1]/tbody/tr[2]/td[4]/center/input[1]").send_keys(hours)

    driver.find_element_by_xpath("/html/body/form/center/form/center/table[1]/tbody/tr[2]/td[4]/center/input[2]").clear()
    driver.find_element_by_xpath("/html/body/form/center/form/center/table[1]/tbody/tr[2]/td[4]/center/input[2]").send_keys(minutes)

    driver.find_element_by_xpath("/html/body/form/center/form/center/table[1]/tbody/tr[2]/td[4]/center/input[3]").clear()
    driver.find_element_by_xpath("/html/body/form/center/form/center/table[1]/tbody/tr[2]/td[4]/center/input[3]").send_keys(seconds)

    select = Select(driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td[7]/select"))
    if(month < 3 or (month == 3 and day < 14 )):
        select.select_by_visible_text("No")
    else:
        select.select_by_visible_text("Yes")

    button = driver.find_elements_by_xpath("/html/body/form/center/form/center/input")[0]
    button.click()

    SolarD = driver.find_element_by_xpath("/html/body/form/center/form/center/table[2]/tbody/tr[2]/td[2]/center/input").get_attribute("value")
    print(float(SolarD))
    row.setValue(SolarDecl, float(SolarD))

    SolarAz = driver.find_element_by_xpath("/html/body/form/center/form/center/table[2]/tbody/tr[2]/td[3]/center/input").get_attribute("value")
    row.setValue(SolarAzi, float(SolarAz))

    CosZen = driver.find_element_by_xpath("/html/body/form/center/form/center/table[2]/tbody/tr[2]/td[5]/center/input").get_attribute("value")
    ZenithAngle = (180/math.pi) * math.acos(float(CosZen))
    row.setValue(SolarZeni, ZenithAngle)
    cursor.updateRow(row)












