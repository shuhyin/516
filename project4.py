# open a file 
with open('project3_example_text.txt') as project3_example_doc:
    project3_example_content = project3_example_doc.read()
# print(project3_example_content)

# find the annotation 
import re
project3_annotation = re.findall(r"\[\[.+?\]\]\(\(.+?\)\)", project3_example_content)
# print(project3_annotation)

#separate the annotation into different files by tags
with open('output1.txt', 'w') as output1_doc:
    output_tag1 = re.findall("\[\[.+?\]\]\(\(Establishing a niche_Indicating a gap\)\)", str(project3_annotation))
    output_tag1_lines = '\n'.join(output_tag1)
    output1_doc.write(str(output_tag1_lines))


with open('output2.txt', 'w') as output2_doc:
    output_tag2 = re.findall("\[\[.+?\]\]\(\(Establishing a territory_Making topic generalizations\)\)", str(project3_annotation))
    output_tag2_lines = '\n'.join(output_tag2)
    output2_doc.write(str(output_tag2_lines))

# write all of the annotation lines
with open('output0.txt', 'w') as output0_doc:
    output0_lines = '\n'.join(project3_annotation)
    output0_doc.write(str(output0_lines))
