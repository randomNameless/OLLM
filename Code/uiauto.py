# %%
import uiautomator
from uiautomator import Device
import os
import time
import xml.etree.ElementTree as ET

# %%
d = Device("emulator-5554")

# %%
folder_name = '5'
d.screenshot("{}.png".format(folder_name))

# %%

def parse_uix_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    def recursive_parse(node):
        print(node.tag, node.attrib)
        for child in node:
            recursive_parse(child)
    
    recursive_parse(root)


# %%
def get_buttons(root):
    clickable_buttons = []
    checkable_buttons = []
    long_clickable_buttons = []
    other_buttons = []


    for node in root.iter('node'):


        # Categorize the node
        if node.attrib.get('clickable') == 'true':
            if node.attrib.get('text') != "":
                clickable_buttons.append('text: '+ node.attrib.get('text'))
            elif node.attrib.get('content-desc') != "":
                long_clickable_buttons.append('content-desc: '+ node.attrib.get('content-desc'))
            #elif node.attrib.get('class') == "android.widget.ImageButton" and node.attrib.get('resource-id') != "":
                #other_buttons.append('image-button-resource-id'+node.attrib.get('resource-id'))
        elif node.attrib.get('long-clickable') == 'true':
            if node.attrib.get('text') != "":
                long_clickable_buttons.append('text: '+ node.attrib.get('text'))
            elif node.attrib.get('content-desc') != "":
                long_clickable_buttons.append('content-desc: '+ node.attrib.get('content-desc'))
            #elif node.attrib.get('class') == "android.widget.ImageButton" and node.attrib.get('resource-id') != "":
                #other_buttons.append('image-button-resource-id'+node.attrib.get('resource-id'))
        elif node.attrib.get('checkable') == 'true':
            if node.attrib.get('text') != "":
                long_clickable_buttons.append('text: '+ node.attrib.get('text'))
            elif node.attrib.get('content-desc') != "":
                long_clickable_buttons.append('content-desc: '+ node.attrib.get('content-desc'))
            #elif node.attrib.get('class') == "android.widget.ImageButton" and node.attrib.get('resource-id') != "":
                #other_buttons.append('image-button-resource-id'+node.attrib.get('resource-id'))
        else:
            if node.attrib.get('text') != "":
                other_buttons.append('text: '+ node.attrib.get('text'))
            elif node.attrib.get('content-desc') != "":
                other_buttons.append('content-desc: '+ node.attrib.get('content-desc'))
            #elif node.attrib.get('class') == "android.widget.ImageButton":
                #other_buttons.append('image-button-resource-id'+node.attrib.get('resource-id'))

    return clickable_buttons, checkable_buttons, long_clickable_buttons, other_buttons

# %%
def get_dump_files(folder_path):
    dump_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".xml"):
            # Get the full file path
            full_path = os.path.join(folder_path, file)
            # Get the creation time of the file
            creation_time = os.path.getctime(full_path)
            # Append both file name and creation time to the list
            dump_files.append((file, creation_time))
    
    # Sort the files by creation time
    dump_files.sort(key=lambda x: x[1])

    # Optionally convert creation time to a human-readable format
    return [file[0]for file in dump_files]



# %%
with open(file='actions.txt', encoding='UTF-8', mode='r') as f:
    actions = f.readlines()

print(actions)

# %%
count = 1
folder_name = '48'
try:
    os.makedirs(folder_name)
except:
    pass
screenshot_file = f"{folder_name}/screenshot_{count}.png"
d.screenshot(screenshot_file)
d.dump("{}/{}.xml".format(folder_name, count))
for a in actions:
    print(a)

    if a.startswith('click'):
        try:
            print("trying pixels")
            x = int(a.split()[1].split(":")[0])
            y = int(a.split()[1].split(":")[1])
            d.click(x, y)
            time.sleep(3)
            # d(description="Open Drawer").click()
        except:
            if "." in a and "/" in a and ":" in a:
                resource_id = a.split()[1]
                d(resourceId=resource_id).click()
                time.sleep(3)
            else:
                text = " ".join(a.split()[1:])
                try:
                    d(description=text).click()
                    time.sleep(3)
                except:
                    d(text=text).click()
                    time.sleep(3)



    elif a.startswith('long_click'):
        try:
            x = int(a.split()[1].split(":")[0])
            y = int(a.split()[1].split(":")[1])
            d.long_click(x, y)
            time.sleep(1)

        except:
            if "." in a and "/" in a and ":" in a:
                resource_id = a.split()[1]
                d(resource_id=resource_id).long_click()
                time.sleep(1)
            else:
                text = " ".join(a.split()[1:])
                try:
                    d(description=text).long_click()
                    time.sleep(1)
                except:
                    d(text=text).long_click()
                    time.sleep(1)
    elif a.startswith('drag'):
        sx = int(a.split()[1].split(":")[0])
        sy = int(a.split()[1].split(":")[1])
        ex = int(a.split()[1].split(":")[2])
        ey = int(a.split()[1].split(":")[3])
        d.drag(sx, sy, ex, ey)
        time.sleep(1)
    elif a.startswith('swipe'):
        sx = int(a.split()[1].split(":")[0])
        sy = int(a.split()[1].split(":")[1])
        ex = int(a.split()[1].split(":")[2])
        ey = int(a.split()[1].split(":")[3])
        d.swipe(sx, sy, ex, ey)
        time.sleep(1)
    elif a.startswith('scroll_to'):
        text = " ".join(a.split()[1:]).strip()
        d(scrollable=True).scroll.to(text=text)
        time.sleep(1)
        print("Scrolled to ", text)
    elif a.startswith('input'):
        #txt_field = a.split()[1]
        #text = " ".join(a.split()[2:])
        #d(resourceId=txt_field).set_text(text)
        tx=a.split()[1]
        os.system('adb shell input text {}'.format(tx))
        time.sleep(2)


    elif a.startswith('back'):
        d.press.back()
        time.sleep(3)
    elif a.startswith('home'):
        d.press.home()
        time.sleep(1)
    elif a.startswith('enter'):
        d.press('enter')
        time.sleep(1)
    elif a.startswith('rotate'):
        d.orientation = a.split()[1]
        time.sleep(1)
    elif a.startswith('wait'):
        time.sleep(5)

    else:
        pass
    time.sleep(0.5)
    count += 1
    screenshot_file = f"{folder_name}/screenshot_{count}.png"
    d.screenshot(screenshot_file)
    d.dump("{}/{}.xml".format(folder_name, count))



# %%
folder_path = str(folder_name)
dump_files = get_dump_files(os.path.join(".", folder_path))
print(dump_files)
file = dump_files[0]
print(file)
file_path = os.path.join(folder_path, file)
print(file_path)
with open(file_path, 'r', encoding="UTF-8") as file:
    tree = ET.parse(file)
root = tree.getroot()
get_buttons(root)

clickable_buttons, checkable_buttons, long_clickable_buttons, other_buttons = get_buttons(root)
print(other_buttons)

# %%
'''This prompt create prompt version 1: dump after each action'''
#question = "Above is an app flow, containing page text and actions to reach other pages. Ignore battery, time and signal fluctuates in page content and coordinate in actions and do not evaluate them in the following question. Is there any inconsistency, a discrepancy, a logical error, or a bug in the output after the given test sequence? Provide your answer with yes or no, and the reason. The reason should be biref and concise"
#question="Above is an app flow, containing page text and actions to reach other pages. Ignore battery, time and signal fluctuates in page content and coordinate in actions and do not evaluate them in the following question. Is there any inconsistency, a discrepancy, a logical error, or a bug in the output after the given test sequence? Provide your answer with yes or no. If your answer is yes, please also provide the reason.  The reason should be biref and concise.  If you didn't detect any error, please answer no."
result_prompt = "Promptv1:\n\n"
for i in range(len(dump_files)):
    try:
        action = actions[i].strip() + "."
    except:
        action = ""
    
    if i == 0:
        output_text = """
Initial structure:
"""
    else:
        output_text = """
Output structure:
"""
    file = dump_files[i]
    #print(file)
    file_path = os.path.join(folder_path, file)
    with open(file_path, 'r', encoding="UTF-8") as file:
        tree = ET.parse(file)
    root = tree.getroot()
    get_buttons(root)

    clickable_buttons, checkable_buttons, long_clickable_buttons, other_buttons = get_buttons(root)
    
    if len(long_clickable_buttons) > 0:
        output_text += "    Long Clickable Buttons: "    
        output_text += f"{long_clickable_buttons}"

    if len(clickable_buttons) > 0:
        output_text += "\n    Clickable Buttons: "
        output_text += f"{clickable_buttons}"

    if len(checkable_buttons) > 0:
        output_text += "\n    Checkable Buttons: "
        output_text += f"{checkable_buttons}"
        for button in checkable_buttons:
            output_text += f"\t{button}"

    if len(other_buttons) > 0:
        output_text += "\n    Other Buttons: "
        output_text += f"{other_buttons}"
    
    result_prompt += output_text + ".\n\n"
    result_prompt += action


#result_prompt += "\n" + question
print(result_prompt)
with open("{}/prompt_v1_{}.txt".format(folder_name, folder_name), 'w', encoding="UTF-8") as f:
    f.write(result_prompt)