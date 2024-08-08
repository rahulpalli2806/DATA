import os

def create_class_directories(data_dir, output_dir):
  """
  Creates separate directories for each class and saves corresponding lines in respective text files.

  Args:
    data_dir: The directory containing the .txt files.
    output_dir: The directory to create class-specific directories and text files.
  """

  for root, _, files in os.walk(data_dir):
    for file in files:
      if file.endswith(".txt"):
        file_path = os.path.join(root, file)
        with open(file_path, 'r') as f:
          for line in f:
            line = line.strip()
            if line:
              class_name = line.split()[-2]
              class_dir = os.path.join(output_dir, class_name)
              
              # Create the class directory if it doesn't exist
              os.makedirs(class_dir, exist_ok=True)

              # Create the file path for the new text file
              new_file_path = os.path.join(class_dir, file)

              # Append the line to the new text file
              with open(new_file_path, 'a') as new_f:
                new_f.write(line + '\n')

# Example usage:
print("---------- Train part1 ----------")
data_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA_CORE_CLASS//train//part1//labelTxt//"
output_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA_CORE_CLASS//classewise_labels//train//part1//"
create_class_directories(data_dir, output_dir)

print("---------- Train part2 ----------")
data_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA_CORE_CLASS//train//part2//labelTxt//"
output_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA_CORE_CLASS//classewise_labels//train//part2//"
create_class_directories(data_dir, output_dir)

print("---------- Val ----------")
data_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA_CORE_CLASS//val//labelTxt//"
output_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA_CORE_CLASS//classewise_labels//val//"
create_class_directories(data_dir, output_dir)
