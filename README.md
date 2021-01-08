Introduction
-----
This package is used to estimate human body keypoints, developed by Waterway Research Insitutue of Nanjing  
E-mail: 1126557295@qq.com

Installation
-----

```bash
pip install njswpose
```

Example
-----

```bash
    from PIL import Image
    import PIL
    from torchvision.transforms import transforms
    from njswpose import pose_detection
    
    image = Image.open('./test.jpg').convert('RGB')
    loader = transforms.Compose([
        transforms.ToTensor()])
    image = loader(image)
    pose_detection(image, detect_threshold=0.55, vis=True)
```
