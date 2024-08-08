# importing packages 
import pandas as pd 
import glob 

folder_path = 'D:\\Object_Detection\\DATA\FAIR1M\\FAIR1M_DOTA\\train\\part1\\labelTxt'
# folder_path = 'D:\\Object_Detection\\DATA\FAIR1M\\FAIR1M_DOTA\\train\\part2\\labelTxt'
# folder_path = 'D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\val\\labelTxt'

file_list = glob.glob(folder_path + "\\*.txt")
file_list.sort()
col_names =['x1','y1','x2','y2','x3','y3','x4','y4','class','score']
classes_l = []
Fine_classes_list = ['A220', 'A321', 'A330', 'A350', 'ARJ21', 'Baseball Field', 
                     'Basketball Court', 'Boeing737', 'Boeing747', 'Boeing777', 
                     'Boeing787', 'Bridge', 'Bus', 'C919', 'Cargo Truck', 'Dry Cargo Ship', 
                     'Dump Truck', 'Engineering Ship', 'Excavator', 'Fishing Boat', 
                     'Football Field', 'Intersection', 'Liquid Cargo Ship', 'Motorboat', 
                     'Passenger Ship', 'Roundabout', 'Small Car', 'Tennis Court', 'Tractor', 
                     'Trailer', 'Truck Tractor', 'Tugboat', 'Van', 'Warship', 'other-airplane', 
                     'other-ship', 'other-vehicle']
for i in range(0,len(file_list)): 
    data =  pd.read_table(file_list[i],delimiter=' ',names = col_names,header=None)
#     display(data)
#     classes_l.extend(data["class"].values.tolist())
    data.replace(to_replace=['A321','A220','ARJ21','A330','A350','C919','Boeing747','Boeing737','Boeing777','Boeing787','other-airplane'],value="Airplane",inplace=True)
    data.replace(to_replace=['Passenger_Ship','Motorboat','Fishing_Boat','Tugboat','Engineering_Ship','Liquid_Cargo_Ship','Dry_Cargo_Ship','Warship', 'other-ship'],value="Ship",inplace=True)
    data.replace(to_replace=['Small_Car','Bus','Cargo_Truck','Dump_Truck','Van','Trailer','Tractor','Truck_Tractor','other-vehicle', 'Excavator'],value="Vehicle",inplace=True)
    data.replace(to_replace=['Baseball_Field','Basketball_Court','Football_Field','Tennis_Court'],value="Court",inplace=True)
    data.replace(to_replace=['Intersection','Bridge','Roundabout'],value="Road",inplace=True)
    # data.to_csv('D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA_CORE_CLASS\\val\\labelTxt\\'+str(i)+'.txt', sep=' ', index=False,header=False)
    data.to_csv('D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA_CORE_CLASS\\train\\part1\\labelTxt\\'+str(i)+'.txt', sep=' ', index=False,header=False)
    # data.to_csv('D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA_CORE_CLASS\\train\\part2\\labelTxt\\'+str(i)+'.txt', sep=' ', index=False,header=False)
# print(set(classes_l))