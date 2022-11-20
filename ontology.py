##all_domains = ['restaurant', 'hotel', 'attraction', 'train', 'taxi', 'police', 'hospital']
##db_domains = ['restaurant', 'hotel', 'attraction', 'train']

all_domains = ['Camera', 'Tablet', 'Computer', 'Laptop', 'Phone']
#all_domains = ['Camera','Laptop','Phone']
db_domains = ['Camera', 'Laptop', 'Phone']

slot_list = ['Discount', 'Android operating system', 'Size', 'Focus', 'Low Resolution', 'Zoom', 'Dimension', 'Graphics card', 'Favourite Colour', 'Dual Sim', 'Pixel', 'Release Date', 'Image', 'Display Size', 'Display', 'Processor', 'SSD', 'Exterl mic', 'Radio', 'Max Resolution', 'Light Weight', 'Storage', 'Minimum Resolution', 'Model', 'OS', 'Disk Storage', 'Shade', 'Hard Drive', 'Mode', 'Window', 'Weight', 'Battery', 'Series', 'Phone', 'Look', 'HDD', 'Sim Slot', 'Released', 'Colour', 'Display_Size', 'Budget', 'Grading', 'RAM', 'Slot', 'Maximum Resolution', 'Monitor', 'Normal Focus Range', 'Length', 'Android', 'P_Camera', 'Sensor', 'Laptop', 'Brand', 'Old model', 'Category', 'Rating', 'Pixels', 'Characteristics', 'MaxResolution', 'Price', 'Goal range', 'Range', 'GPU', 'Graphics', 'Quality', 'SIM', 'Photoshot', 'Cost', 'Specifiaction', 'Features', 'Panel_Size', 'Connection', 'GPS', 'Zoom wide', 'CPU', 'Subscription', 'Dicsount', 'S_Camera', 'Resolution', 'Review', 'Feature', 'Describe', 'Camera', 'Sim','Status']
# original slot names in goals (including booking slots)
normlize_slot_names = {
    "car type": "car",
    "entrance fee": "price",
    "duration": "time",
    "leaveat": 'leave',
    'arriveby': 'arrive',
    'trainid': 'id'
}


requestable_slots_in_goals = {
    "Camera": slot_list,
    "Tablet": slot_list,
    "Computer": slot_list,
    "Laptop": slot_list,
    "Phone": slot_list
}


informable_slots_in_goals = requestable_slots_in_goals

requestable_slots = {
  "Camera" : ['Brand','Model','Released','Resolution','Pixel','Normal Focus Range','Macro Focus Range','Storage','Weight','Price','Zoom'],
  "Laptop" : ['Brand','Model','Display Size','Processor','Graphics card','Disk Storage','Discount','Price','Rating'],
  "Phone" : ['Brand','Model','Battery','RAM','P_Camera','S_Camera','Radio','Display Size','Status','Sim','GPS','OS','Colour','Weight','Released','Price','img_url','Rating'],
  "Tablet" : ['Brand','Model','Battery','RAM','P_Camera','S_Camera','Radio','Display Size','Status','Sim','GPS','OS','Colour','Weight','Released','Price','img_url','Rating'],
  "Computer" : ['Brand','Model','Display Size','Processor','Graphics card','Disk Storage','Discount','Price','Rating']
}


# requestable_slots = {
#     "taxi": ["car", "phone"],
#     "police": ["postcode", "address", "phone"],
#     "hospital": ["address", "phone", "postcode"],
#     "hotel": ["address", "postcode", "internet", "phone", "parking", "type", "pricerange", "stars", "area", "reference"],
#     "attraction": ["price", "type", "address", "postcode", "phone", "area", "reference"],
#     "train": ["time", "leave", "price", "arrive", "id", "reference"],
#     "restaurant": ["phone", "postcode", "address", "pricerange", "food", "area", "reference"]
# }
#all_reqslot = ["car", "address", "postcode", "phone", "internet",  "parking", "type", "pricerange", "food",
                      # "stars", "area", "reference", "time", "leave", "price", "arrive", "id"]
# count: 17

all_reqslot = ['Battery', 'Brand', 'Colour', 'Discount', 'Disk Storage',
       'Display Size', 'GPS', 'Graphics card', 'Macro Focus Range', 'Model',
       'Normal Focus Range', 'OS', 'P_Camera', 'Pixel', 'Price', 'Processor',
       'RAM', 'Radio', 'Rating', 'Released', 'Resolution', 'S_Camera', 'Sim',
       'Status', 'Storage', 'Weight', 'Zoom', 'img_url']

informable_slots = {
    "Camera": ['Brand','Model','Released','Resolution','Pixel','Normal Focus Range','Macro Focus Range','Storage','Weight','Price','Zoom'],
    "Phone": ['Brand','Model','Battery','RAM','P_Camera','S_Camera','Radio','Display Size','Status','Sim','GPS','OS','Colour','Weight','Released','Price','img_url','Rating'] ,
    "Tablet": ['Brand','Model','Battery','RAM','P_Camera','S_Camera','Radio','Display Size','Status','Sim','GPS','OS','Colour','Weight','Released','Price','img_url','Rating'],
    "Computer": ['Brand','Model','Display Size','Processor','Graphics card','Disk Storage','Discount','Price','Rating'],
    "Laptop" : ['Brand','Model','Display Size','Processor','Graphics card','Disk Storage','Discount','Price','Rating']   
}
# all_infslot = ["type", "parking", "pricerange", "internet", "stay", "day", "people", "area", "stars", "name",
#                      "leave", "destination", "departure", "arrive", "department", "food", "time"]
# count: 17

all_infslot = all_reqslot

#all_slots = all_reqslot + ["stay", "day", "people", "name", "destination", "departure", "department"]
all_slots = all_reqslot

get_slot = {}
for s in all_slots:
    get_slot[s] = 1
# count: 24


# mapping slots in dialogue act to original goal slot names
# da_abbr_to_slot_name = {
#     'addr': "address",
#     'fee': "price",
#     'post': "postcode",
#     'ref': 'reference',
#     'ticket': 'price',
#     'depart': "departure",
#     'dest': "destination",
# }

da_abbr_to_slot_name = {
    'brand': "Brand",
    'price': "Price",
    'Cost': "Price"
}




# slot merging: not used currently
# slot_name_to_value_token = {
#     'entrance fee': 'price',
#     'pricerange': 'price',
#     'arrive': 'time',
#     'leave': 'time',
#     'departure': 'name',
#     'destination': 'name',
#     'stay': 'count',
#     'people': 'count',
#     'stars': 'count',
# }
dialog_act_dom = all_domains
# dialog_acts = {
#     'restaurant': ['inform', 'request', 'nooffer', 'recommend', 'select', 'offerbook', 'offerbooked', 'nobook'],
#     'hotel': ['inform', 'request', 'nooffer', 'recommend', 'select', 'offerbook', 'offerbooked', 'nobook'],
#     'attraction': ['inform', 'request', 'nooffer', 'recommend', 'select'],
#     'train': ['inform', 'request', 'nooffer', 'offerbook', 'offerbooked', 'select'],
#     'taxi': ['inform', 'request'],
#     'police': ['inform', 'request'],
#     'hospital': ['inform', 'request'],
#     # 'booking': ['book', 'inform', 'nobook', 'request'],
#     'general': ['bye', 'greet', 'reqmore', 'welcome'],
# }

dialog_acts = {
    'Camera' : ['Booking', 'BookingReq', 'PersonalAppeal', 'Recommend', 'ModelReq', 'Gratitude', 'CameraReq', 'Inform', 'EmotionalAppeal', 'ColorReq', 'Close', 'OtherHelp', 'CreadibilityAppeal', 'BudgetReq', 'PersonaAppeal', 'LogicalAppeal', 'BrandReq', 'Request', 'TaskReq', 'Result', 'TaskSpecificationReq'],
    'Phone' : ['Booking', 'BookingReq', 'PersonalAppeal', 'Recommend', 'ModelReq', 'Gratitude', 'CameraReq', 'TaskSpecifiactionReq', 'Inform', 'EmotionalAppeal', 'ColorReq', 'Close', 'OtherHelp', 'Rephrase', 'CreadibilityAppeal', 'BatteryReq', 'BudgetReq', 'PersonaAppeal', 'LogicalAppeal', 'ImageReq', 'Greet', 'BrandReq', 'Request', 'TaskReq', 'CreadibilitylAppeal', 'Result', 'Confirm', 'PersonAppeal', 'TaskSpecificationReq'],
    'Tablet' : ['Booking', 'BookingReq', 'PersonalAppeal', 'Recommend', 'ModelReq', 'Gratitude', 'Inform', 'EmotionalAppeal', 'ColorReq', 'Close', 'OtherHelp', 'CreadibilityAppeal', 'BatteryReq', 'BudgetReq', 'PersonaAppeal', 'LogicalAppeal', 'ImageReq', 'BrandReq', 'Request', 'TaskReq', 'Result', 'TaskSpecificationReq'],
    'Laptop' : ['Booking', 'BookingReq', 'PersonalAppeal', 'Recommend', 'ModelReq', 'Gratitude', 'Inform', 'EmotionalAppeal', 'ColorReq', 'Close', 'OtherHelp', 'CreadibilityAppeal', 'BudgetReq', 'PersonaAppeal', 'LogicalAppeal', 'ImageReq', 'BrandReq', 'Request', 'TaskReq', 'Result', 'PersonAppeal', 'TaskSpecificationReq'],
    'Computer' : ['BudgetReq', 'Request', 'Inform', 'Booking', 'EmotionalAppeal', 'TaskReq', 'Close', 'TaskSpecificationReq', 'BrandReq']
}

all_acts = []
for acts in dialog_acts.values():
    for act in acts:
        if act not in all_acts:
            all_acts.append(act)
# print(all_acts)

# dialog_act_params = {
#     'inform': all_slots + ['choice', 'open'] ,
#     'request': all_infslot+['choice', 'price'],
#     'nooffer': all_slots + ['choice'],
#     'recommend': all_reqslot + ['choice', 'open'],
#     'select': all_slots +['choice'],
#     # 'book': ['time', 'people', 'stay', 'reference', 'day', 'name', 'choice'],
#     #'nobook': ['time', 'people', 'stay', 'reference', 'day', 'name', 'choice'],
#     'offerbook':all_slots + ['choice'],
#     'offerbooked': all_slots + ['choice'],
#     'reqmore': [],
#     'welcome': [],
#     'bye': [],
#     'greet': [],
# }

dialog_act_params = {
      'BatteryReq': ['Battery'],
      'Booking': all_slots,
      'BookingReq': all_slots,
      'BrandReq': ['Brand'],
      'BudgetReq': ['Price','Budget'],
      'CameraReq': ['Pixel','Pixels'],
      'CameraSelReq': all_slots,
      'Close': all_slots,
      'ColorReq': ['Colour'],
      'Confirm': all_slots,
      'CreadibilityAppeal': all_slots,
      'EmotionalAppeal': all_slots,
      'Feedback': all_slots,
      'FeedbackReq': all_slots,
      'Gratitude': all_slots,
      'Greet': all_slots,
      'ImageReq': all_slots,
      'Inform': all_slots + ['choice', 'open'],
      'LaptopSelReq': all_slots,
      'LogicalAppeal': all_slots,
      'ModelReq': ['Model'],
      'OtherHelp': all_slots,
      'PersonalAppeal': all_slots,
      'PhoneSelReq': all_slots,
      'Recommend': all_reqslot + ['choice', 'open'],
      'Reject': all_reqslot + ['choice', 'open'],
      'Rephrase': all_slots,
      'Request': all_infslot + ['choice', 'price'],
      'Result': all_infslot,
      'SuggestionReq': all_infslot,
      'TabletSelReq': all_slots,
      'TaskReq': all_reqslot,
      'TaskSpecificationReq': all_slots 
 }

# dialog_acts = ['inform', 'request', 'nooffer', 'recommend', 'select', 'book', 'nobook', 'offerbook', 'offerbooked',
#                         'reqmore', 'welcome', 'bye', 'greet'] # thank
dialog_act_all_slots = all_slots + ['choice', 'open']
# act_span_vocab = ['['+i+']' for i in dialog_act_dom] + ['['+i+']' for i in dialog_acts] + all_slots

# value_token_in_resp = ['address', 'name', 'phone', 'postcode', 'area', 'food', 'pricerange', 'id',
#                                      'department', 'place', 'day', 'count', 'car']
# count: 12


# special slot tokens in belief span
# no need of this, just covert slot to [slot] e.g. pricerange -> [pricerange]
slot_name_to_slot_token = {}


# special slot tokens in responses
# not use at the momoent
slot_name_to_value_token = {
    # 'entrance fee': '[value_price]',
    # 'pricerange': '[value_price]',
    # 'arriveby': '[value_time]',
    # 'leaveat': '[value_time]',
    # 'departure': '[value_place]',
    # 'destination': '[value_place]',
    # 'stay': 'count',
    # 'people': 'count'
       'Price' : '[value_price]',
       'Released' : '[value_time]',
       'Release Date' : '[value_time]',
       'Favourite Colour' : '[value_colour]',
       'Colour' : '[value_colour]',
       'Rating' : '[value_rating]'

}


db_tokens = ['<sos_db>', '<eos_db>', '[db_nores]', '[db_0]', '[db_1]', '[db_2]', '[db_3]']

special_tokens = ['<pad>', '<go_r>', '<unk>', '<go_b>', '<go_a>',
                            '<eos_u>', '<eos_r>', '<eos_b>', '<eos_a>', '<go_d>','<eos_d>',
                            '<sos_u>', '<sos_r>', '<sos_b>', '<sos_a>', '<sos_d>'] + db_tokens

eos_tokens = {
    'user': '<eos_u>', 'user_delex': '<eos_u>',
    'resp': '<eos_r>', 'resp_gen': '<eos_r>', 'pv_resp': '<eos_r>',
    'bspn': '<eos_b>', 'bspn_gen': '<eos_b>', 'pv_bspn': '<eos_b>',
    'bsdx': '<eos_b>', 'bsdx_gen': '<eos_b>', 'pv_bsdx': '<eos_b>',
    'aspn': '<eos_a>', 'aspn_gen': '<eos_a>', 'pv_aspn': '<eos_a>',
    'dspn': '<eos_d>', 'dspn_gen': '<eos_d>', 'pv_dspn': '<eos_d>'}

sos_tokens = {
    'user': '<sos_u>', 'user_delex': '<sos_u>',
    'resp': '<sos_r>', 'resp_gen': '<sos_r>', 'pv_resp': '<sos_r>',
    'bspn': '<sos_b>', 'bspn_gen': '<sos_b>', 'pv_bspn': '<sos_b>',
    'bsdx': '<sos_b>', 'bsdx_gen': '<sos_b>', 'pv_bsdx': '<sos_b>',
    'aspn': '<sos_a>', 'aspn_gen': '<sos_a>', 'pv_aspn': '<sos_a>',
    'dspn': '<sos_d>', 'dspn_gen': '<sos_d>', 'pv_dspn': '<sos_d>'}