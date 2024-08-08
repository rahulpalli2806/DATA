import os

def create_class_file_dict(data_dir):
    """
    Creates a dictionary where keys are class names and values are lists of filenames containing that class.

    Args:
        data_dir: The directory containing the .txt files.

    Returns:
        A dictionary mapping class names to lists of filenames.
    """
    class_file_dict = {}
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            class_name = line.split()[-2]
                            if class_name not in class_file_dict:
                                class_file_dict[class_name] = []
                            class_file_dict[class_name].append(file_path)
    return class_file_dict

def write_class_files(class_file_dict, output_dir):
    """
    Writes the file lists for each class name to individual text files.

    Args:
        class_file_dict: A dictionary mapping class names to lists of filenames.
        output_dir: The directory where the class files will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for class_name, file_list in class_file_dict.items():
        print(f"{class_name} : {len(file_list)}")
        file_name = f"{class_name}.txt"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'w') as f:
            for file in file_list:
                f.write(f"{file}\n")
print("---------- Train part1 ----------")
data_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA//train//part1//labelTxt//"
output_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA//classewise_file_list//train//part1//"

class_file_dict = create_class_file_dict(data_dir)
write_class_files(class_file_dict, output_dir)

print("---------- Train part2 ----------")
data_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA//train//part2//labelTxt//"
output_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA//classewise_file_list//train//part2//"

class_file_dict = create_class_file_dict(data_dir)
write_class_files(class_file_dict, output_dir)

print("---------- Val ----------")
data_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA//val//labelTxt//"
output_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA//classewise_file_list//val//"

class_file_dict = create_class_file_dict(data_dir)
write_class_files(class_file_dict, output_dir)
