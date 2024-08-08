import xml.etree.ElementTree as ET
import os
import json

def convert_fairm1m_to_dota(fairm1m_xml_path, dota_output_dir):
  """Converts a FAIRM1M XML file to DOTA format.

  Args:
    fairm1m_xml_path: Path to the FAIRM1M XML file.
    dota_output_dir: Directory to save the DOTA annotation file.
  """

  # Parse the FAIRM1M XML file
  tree = ET.parse(fairm1m_xml_path)
  root = tree.getroot()

  # Extract relevant information from FAIRM1M XML
  # Extract image name
  image_name = os.path.splitext(os.path.split(fairm1m_xml_path)[-1])[0]  
  # image_size = ...  # Extract image size
   # Extract object information (bounding boxes, labels, etc.)
  objects =  root.find('objects') 
  items = objects.findall('object')
  # Create DOTA annotation file
  dota_file_path = os.path.join(dota_output_dir, image_name + '.txt')
  with open(dota_file_path, 'w') as f:
    # Write DOTA annotations to the file
    ann_list = []
    for item in items:
      label = item.find('possibleresult')
      label=label.find('name').text
      label = label.replace(" ", "_")
      points = item.find('points')
      points = [[float(item) for item in point.text.split(',')] for point in points.findall('point')]
      x1, y1 = points[0]
      x2, y2 = points[1]
      x3, y3 = points[2]
      x4, y4 = points[3]

      ann = [x1, y1, x2, y2, x3, y3, x4, y4, label, 1]
      ann = [str(item) for item in ann]
      
      ann_list.append(' '.join(ann))
    f.write('\n'.join(ann_list))        
def main():

  #xml input
  fairm1m_xml_dir_train_p1 = 'D:\\Object_Detection\\DATA\FAIR1M\\FAIR1M\\train\\part1\\labelXmls'  
  #Train part1 txt output
  # dota_output_dir_train_p1 = 'D:\\Object_Detection\\DATA\FAIR1M\\FAIR1M_DOTA\\train_space\\part1\\labelTxt'
  dota_output_dir_train_p1 = 'D:\\Object_Detection\\DATA\FAIR1M\\FAIR1M_DOTA\\train\\part1\\labelTxt'
  # Iterate over FAIRM1M XML files
  for xml_file in os.listdir(fairm1m_xml_dir_train_p1):
    if xml_file.endswith('.xml'):
      fairm1m_xml_path = os.path.join(fairm1m_xml_dir_train_p1, xml_file)
      convert_fairm1m_to_dota(fairm1m_xml_path, dota_output_dir_train_p1)

  #xml input
  fairm1m_xml_dir_train_p2 = 'D:\\Object_Detection\\DATA\FAIR1M\\FAIR1M\\train\\part2\\labelXmls\\labelXml'
  #Train part2 txt output
  # dota_output_dir_train_p2 = 'D:\\Object_Detection\\DATA\FAIR1M\\FAIR1M_DOTA\\train_space\\part2\\labelTxt'
  dota_output_dir_train_p2 = 'D:\\Object_Detection\\DATA\FAIR1M\\FAIR1M_DOTA\\train\\part2\\labelTxt'
  # Iterate over FAIRM1M XML files
  for xml_file in os.listdir(fairm1m_xml_dir_train_p2):
    if xml_file.endswith('.xml'):
      fairm1m_xml_path = os.path.join(fairm1m_xml_dir_train_p2, xml_file)
      convert_fairm1m_to_dota(fairm1m_xml_path, dota_output_dir_train_p2)

  #xml input
  fairm1m_xml_dir_val = 'D:\\Object_Detection\\DATA\\FAIR1M\FAIR1M\\val\\labelXmls\\labelXml'
  #Val txt output
  dota_output_dir_val = 'D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\val\\labelTxt'
  # dota_output_dir_val = 'D:\\Object_Detection\\DATA\\FAIR1M\\FAIR1M_DOTA\\val_spaces\\labelTxt'
  # Iterate over FAIRM1M XML files
  for xml_file in os.listdir(fairm1m_xml_dir_val):
    if xml_file.endswith('.xml'):
      fairm1m_xml_path = os.path.join(fairm1m_xml_dir_val, xml_file)
      convert_fairm1m_to_dota(fairm1m_xml_path, dota_output_dir_val)
      
if __name__ == '__main__':
  main()
