import os

office_classes = ['back pack', 'bike', 'bike helmet', 'bookcase', 'bottle',
 'calculator', 'desk chair', 'desk lamp', 'desktop computer', 'file cabinet',
  'headphones', 'keyboard', 'laptop computer', 'letter tray', 'mobile phone',
   'monitor', 'optical mouse', 'mug', 'paper notebook', 'pen', 'phone', 'printer',
    'projector', 'hole punchers', 'ring binder', 'plastic ruler', 'scissors', 'speaker',
     'stapler', 'tape dispenser', 'trash can']

lists = os.listdir('./')
f = open('office_syn_amazon.txt','a')
for name in lists:
    for (idx, clss) in enumerate(office_classes):
        if clss in name:
            f.write(f'{name} {idx}\n')
f.close()