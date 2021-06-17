Introduction
-----
This package is used to estimate human body keypoints, developed by Waterway Research Insitutue of Nanjing  
E-mail: 1126557295@qq.com

![](https://img.shields.io/badge/build-passing-brightgreen) ![](https://img.shields.io/badge/author-ddmm-brightgreen)

our backbone network is resnet50.

Installation
-----

```bash
pip install njswpose
or 
# If you have changed your mirror source. You should try the following command.
pip install njswpose -i https://www.pypi.org/simple/
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
    
    # The test results are saved as ./pose.jpg
    # pose_detection(image, detect_threshold=0.55, vis=True)
    keypoints,kp_score = pose_detection(image, detect_threshold=0.55, vis=True)
```
Test
---
![image](https://github.com/ddmm2020/njswpose/blob/master/detection_result/test1_pose.jpg)
![image](https://github.com/ddmm2020/njswpose/blob/master/detection_result/test2_pose.jpg)
![image](https://github.com/ddmm2020/njswpose/blob/master/detection_result/test3_pose.jpg)
![image](https://github.com/ddmm2020/njswpose/blob/master/detection_result/test4_pose.jpg)
