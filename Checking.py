import os
import xml.etree.ElementTree as ET

def compare_xml_and_text(xml_dir, text_dir):
    """Compares XML tag values with text file lines and counts matching files.

    Args:
        xml_dir: Path to the directory containing XML files.
        text_dir: Path to the directory containing text files.
        xml_tag: The XML tag to extract values from.

    Returns:
        The number of files with matching values.
    """
    # match_count = 0
    matching_files = []
    un_matching_files = []

    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join(xml_dir, xml_file)
            text_file = os.path.join(text_dir, xml_file[:-4] + ".txt")
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                xml_objects = []
                for obj in root.findall('objects/object'):
                    # point_s = obj.find('points')
                    xml_object = {
                        'name': obj.find('possibleresult/name').text,
                        'points': [(float(p.text.split(',')[0]), float(p.text.split(',')[1])) for p in obj.findall('points/point')]
                    }
                    xml_object['name'] = xml_object['name'].replace(" ", "_")
                    xml_object['points'] = xml_object['points'][:-1]
                    xml_objects.append(xml_object)

                with open(text_file, 'r') as f:
                    text_objects = []
                    for line in f:
                        parts = line.split()
                        text_object = {
                            'name': parts[8],
                            'points': [(float(parts[0]), float(parts[1])), (float(parts[2]), float(parts[3])),
                                        (float(parts[4]), float(parts[5])), (float(parts[6]), float(parts[7]))]
                        }
                        text_objects.append(text_object)
                if len(xml_objects) == len(text_objects):
                    match = True
                    for xml_obj, text_obj in zip(xml_objects, text_objects):
                        if xml_obj['name'] != text_obj['name'] or xml_obj['points'] != text_obj['points']:
                            match = False
                            break
                    if match:
                     # match_count+=1
                     matching_files.append((xml_path, text_file, True))
                    else:
                     un_matching_files.append((xml_path, text_file, False))

            except FileNotFoundError:
                print(f"Error: File not found: {xml_file} or {text_file}")
            except Exception as e:
                print(f"Error processing files: {xml_file}, {text_file}: {e}")

    with open("D:\\Object_Detection\\DATA\\FAIR1M\\matching_files.txt", "w") as file:
        for item in matching_files:
         file.write(f"{item[0]}, {item[1]},{item[2]}\n")
    with open("D:\\Object_Detection\\DATA\\FAIR1M\\un_matching_files.txt", "w") as file:
        for item in un_matching_files:
         file.write(f"{item[0]}, {item[1]},{item[2]}\n")

    return len(un_matching_files) , len(matching_files) #match_count

# Example usage:
# xml_directory = "D:\\Object_Detection\\DATA\FAIR1M\\FAIR1M\\train\\part1\\labelXmls"
xml_directory = "D:\\Object_Detection\\DATA\FAIR1M\\FAIR1M\\train\\part2\\labelXmls\\labelXml"
# xml_directory = "D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M\\val\\labelXmls\\labelXml"

# text_directory = "D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\train\\part1\\labelTxt\\"
text_directory = "D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\train\\part2\\labelTxt\\"
# text_directory = "D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\val\\labelTxt"

# text_directory = "D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\train\\part1\\labelTxt\\"
# text_directory = "D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\train\\part2\\labelTxt\\"
# text_directory = "D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\val_spaces\\labelTxt"

un_match_count,match_count= compare_xml_and_text(xml_directory, text_directory)
print("Number of matching files:", match_count)
print("Number of unmatching files:",un_match_count)
