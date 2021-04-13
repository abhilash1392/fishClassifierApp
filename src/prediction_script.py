from classificationNetwork import model
import torch
import PIL 
import torchvision.transforms as T

device = torch.device('cpu')
model.load_state_dict(torch.load('..\models\model_fish.pt',map_location=device))
model.eval()
int_to_str = {0: 'Hourse Mackerel', 1: 'Black Sea Sprat', 2: 'Sea Bass',
 3: 'Red Mullet', 4: 'Trout', 5: 'Striped Red Mullet', 6: 'Shrimp', 7: 'Gilt-Head Bream', 8: 'Red Sea Bream'}

transform = T.Compose([T.Resize(256),T.CenterCrop(224),T.Resize(64),T.ToTensor(),T.Normalize(mean=[0.485,0.456,0.406],std=[0.229,0.224,0.225])])

def predict_fish_class(path):
    
    image = PIL.Image.open(path)
    image = transform(image)
    image = image.unsqueeze(0)
    output = model(image)
    _,pred= torch.max(output,1)
    pred = pred.item()
    predicted_class = int_to_str[pred]
    return predicted_class




