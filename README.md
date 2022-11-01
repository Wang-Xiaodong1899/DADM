# DADM
Domain Adaptation via Diffusion Models

## data synthesis
## office-home
a trash can of product style

## office-31
a trash can of webcam style

## command
we set everything aligned with BNM.
python da_home.py --dset office --lr 0.001 --net resnet50 --gpu_id 3 --batch_size 36 --base SourceOnly --method ENT --interval 6 --max_it 6000 --warm_up 3000

python da_home.py --dset office-home --net resnet50 --gpu_id 5 --batch_size 36 --base SourceOnly --method ENT --interval 6 --warm_up 0 --max_it 6000

## class info
### office-31
['back pack', 'bike', 'bike helmet', 'bookcase', 'bottle', 'calculator', 'desk chair', 'desk lamp', 'desktop computer', 'file cabinet', 'headphones', 'keyboard', 'laptop computer', 'letter tray', 'mobile phone', 'monitor', 'mouse', 'mug', 'paper notebook', 'pen', 'phone', 'printer', 'projector', 'punchers', 'ring binder', 'ruler', 'scissors', 'speaker', 'stapler', 'tape dispenser', 'trash can']