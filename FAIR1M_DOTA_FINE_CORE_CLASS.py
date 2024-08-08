import pandas as pd
import glob
import os

def convert_fair1m_to_core_classes(input_folder, output_folder):
    """Converts FAIR1M annotations to core classes.

    Args:
        input_folder: Path to the input folder containing FAIR1M annotation files.
        output_folder: Path to the output folder for core class annotations.
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    col_names = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'class', 'score']
    class_mapping = {
        'A321': 'Airplane', 'A220': 'Airplane', 'ARJ21': 'Airplane', 'A330': 'Airplane',
        'A350': 'Airplane', 'C919': 'Airplane', 'Boeing747': 'Airplane', 'Boeing737': 'Airplane',
        'Boeing777': 'Airplane', 'Boeing787': 'Airplane', 'other-airplane': 'Airplane',
        'Passenger_Ship': 'Ship', 'Motorboat': 'Ship', 'Fishing_Boat': 'Ship', 'Tugboat': 'Ship',
        'Engineering_Ship': 'Ship', 'Liquid_Cargo_Ship': 'Ship', 'Dry_Cargo_Ship': 'Ship',
        'Warship': 'Ship', 'other-ship': 'Ship',
        'Small_Car': 'Vehicle', 'Bus': 'Vehicle', 'Cargo_Truck': 'Vehicle', 'Dump_Truck': 'Vehicle',
        'Van': 'Vehicle', 'Trailer': 'Vehicle', 'Tractor': 'Vehicle', 'Truck_Tractor': 'Vehicle',
        'other-vehicle': 'Vehicle', 'Excavator': 'Vehicle',
        'Baseball_Field': 'Court', 'Basketball_Court': 'Court', 'Football_Field': 'Court', 'Tennis_Court': 'Court',
        'Intersection': 'Road', 'Bridge': 'Road', 'Roundabout': 'Road'
    }

    for file in glob.glob(input_folder + "\\*.txt"):
        data = pd.read_table(file, delimiter=' ', names=col_names, header=None)
        data['class'] = data['class'].map(class_mapping)
        output_file = os.path.join(output_folder, os.path.basename(file))
        data.to_csv(output_file, sep=' ', index=False, header=False)

# input and output:
input_folder = 'D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\train\\part1\\labelTxt\\'
output_folder = 'D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA_CORE_CLASS\\train\\part1\\labelTxt'
convert_fair1m_to_core_classes(input_folder, output_folder)

input_folder = 'D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\train\\part2\\labelTxt\\'
output_folder = 'D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA_CORE_CLASS\\train\\part2\\labelTxt\\'
convert_fair1m_to_core_classes(input_folder, output_folder)

input_folder = 'D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\val\\labelTxt\\'
output_folder = 'D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA_CORE_CLASS\\val\\labelTxt\\'
convert_fair1m_to_core_classes(input_folder, output_folder)
