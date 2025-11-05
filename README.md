## A Survey on Text-Driven 360-Degree Panorama Generation


<a href='https://arxiv.org/abs/2502.14799'>
  <img src='https://img.shields.io/badge/Paper-Paper-green?style=flat&logo=arxiv&logoColor=green' alt='arxiv Paper'>
</a>
<a href='https://littlewhitesea.github.io/Text-Driven-Pano-Gen/' style='padding-left: 0.5rem;'>
  <img src='https://img.shields.io/badge/Project-Page-blue?style=flat&logo=Google%20chrome&logoColor=blue' alt='Project Page'>
</a>


### Introduction

This project lists representative papers/codes/datasets about **Text-Driven 360-Degree Panorama Generation**, which aims to comprehensively and systematically summarize the recent advances from 2022 to 2025 to the best of our knowledge.

We aim to constantly update the latest relevant papers and help the community track this topic. If you find any missed resources or errors, please feel free to open an issue or make a pull request.

### Text-Only Generation

Text-only generation focuses on synthesizing 360-degree panoramas from textual descriptions only.

* **Omni<sup>2</sup>: Unifying Omnidirectional Image Generation and Editing in an Omni Model.**<br>
*Liu Yang, Huiyu Duan, Yucheng Zhu, Xiaohong Liu, Lu Liu, Zitong Xu, Guangji Ma, Xiongkuo Min, Guangtao Zhai, Patrick Le Callet.*<br>
ACM MM 2025. [[PDF](https://arxiv.org/abs/2504.11379)] [[Code]](https://github.com/IntMeGroup/Omni2)<br>

* **What Makes for Text to 360-degree Panorama Generation with Stable Diffusion?.**<br>
*Jinhong Ni, Chang-Bin Zhang, Qiang Zhang, Jing Zhang.*<br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2505.22129)] [[Code]](https://github.com/jinhong-ni/UniPano)<br>

* **Spherical Manifold Guided Diffusion Model for Panoramic Image Generation.**<br>
*Xiancheng Sun, Mai Xu, Shengxi Li, Senmao Ma, Xin Deng, Lai Jiang, Gang Shen.*<br>
CVPR 2025. [[PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Sun_Spherical_Manifold_Guided_Diffusion_Model_for_Panoramic_Image_Generation_CVPR_2025_paper.pdf)] [[Code]](https://github.com/chronos123/SMGD-CVPR2025)<br>

* **DiffPano: Scalable and Consistent Text to Panorama Generation with Spherical Epipolar-Aware Diffusion.**<br>
*Weicai Ye, Chenhao Ji, Zheng Chen, Junyao Gao, Xiaoshui Huang, Song-Hai Zhang, Wanli Ouyang, Tong He, Cairong Zhao, Guofeng Zhang.*<br>
NeurIPS 2024. [[PDF](https://arxiv.org/abs/2410.24203)] [[Project](https://zju3dv.github.io/DiffPano/)] [[Code]](https://github.com/zju3dv/DiffPano)<br>

* **PanoFree: Tuning-Free Holistic Multi-view Image Generation with Cross-view Self-Guidance.**<br>
*Aoming Liu, Zhong Li, Zhang Chen, Nannan Li, Yi Xu, Bryan A. Plummer.*<br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2408.02157)] [[Project](https://panofree.github.io/)] [[Code]](https://github.com/zxcvfd13502/PanoFree)<br>

* **Taming Stable Diffusion for Text to 360° Panorama Image Generation.**<br>
*Cheng Zhang, Qianyi Wu, Camilo Cruz Gambardella, Xiaoshui Huang, Dinh Phung, Wanli Ouyang, Jianfei Cai.*<br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2404.07949)] [[Project](https://chengzhag.github.io/publication/panfusion/)] [[Code]](https://github.com/chengzhag/PanFusion)<br>

* **Customizing 360-degree panoramas through text-to-image diffusion models.**<br>
*Hai Wang, Xiaoyu Xiang, Yuchen Fan, Jing-Hao Xue.*<br>
WACV 2024. [[PDF](https://arxiv.org/abs/2310.18840)] [[Project](https://littlewhitesea.github.io/stitchdiffusion.github.io/)] [[Code]](https://github.com/littlewhitesea/StitchDiffusion)<br>

* **Text2Light: Zero-Shot Text-Driven HDR Panorama Generation.**<br>
*Zhaoxi Chen, Guangcong Wang, Ziwei Liu.*<br>
TOG 2022 (SIGGRAPH Asia). [[PDF](https://arxiv.org/abs/2209.09898)] [[Project](https://frozenburning.github.io/projects/text2light/)] [[Code]](https://github.com/FrozenBurning/Text2Light)<br>

* **Conditional Panoramic Image Generation via Masked Autoregressive Modeling.**<br>
*Chaoyang Wang, Xiangtai Li, Lu Qi, Xiaofan Lin, Jinbin Bai, Qianyu Zhou, Yunhai Tong.*<br>
arxiv 2025. [[PDF](https://arxiv.org/abs/2505.16862)] [[Project](https://wang-chaoyang.github.io/project/par/)] [[Code]](https://github.com/wang-chaoyang/par)<br>

* **SphereDiff: Tuning-free Omnidirectional Panoramic Image and Video Generation via Spherical Latent Representation.**<br>
*Minho Park, Taewoong Kang, Jooyeol Yun, Sungwon Hwang, Jaegul Choo.*<br>
arxiv 2025. [[PDF](https://arxiv.org/abs/2504.14396)] [[Project](https://pmh9960.github.io/research/SphereDiff/)] [[Code]](https://github.com/pmh9960/SphereDiff)<br>

* **Diffusion360: Seamless 360 Degree Panoramic Image Generation based on Diffusion Models.**<br>
*Mengyang Feng, Jinlin Liu, Miaomiao Cui, Xuansong Xie.*<br>
arxiv 2023. [[PDF](https://arxiv.org/abs/2311.13141)] [[Code]](https://github.com/ArcherFMY/SD-T2I-360PanoImage)<br>

### Text-Driven NFoV Outpainting

Text-driven narrow field-of-view (NFoV) outpainting enhances user control by conditioning the generation process on both textual prompts and initial narrow NFoV images.

* **Omni<sup>2</sup>: Unifying Omnidirectional Image Generation and Editing in an Omni Model.**<br>
*Liu Yang, Huiyu Duan, Yucheng Zhu, Xiaohong Liu, Lu Liu, Zitong Xu, Guangji Ma, Xiongkuo Min, Guangtao Zhai, Patrick Le Callet.*<br>
ACM MM 2025. [[PDF](https://arxiv.org/abs/2504.11379)] [[Code]](https://github.com/IntMeGroup/Omni2)<br>

* **DreamCube: 3D Panorama Generation via Multi-plane Synchronization.**<br>
*Yukun Huang, Yanning Zhou, Jianan Wang, Kaiyi Huang, Xihui Liu.*<br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2506.17206)] [[Project]](https://yukun-huang.github.io/DreamCube/) [[Code]](https://github.com/yukun-huang/DreamCube)<br>

* **Spherical-Nested Diffusion Model for Panoramic Image Outpainting.**<br>
*Xiancheng Sun, Senmao Ma, Shengxi Li, Mai Xu, Jingyuan Xia, Lai Jiang, Xin Deng, Jiali Wang.*<br>
ICML 2025. [[PDF](https://openreview.net/pdf?id=JVDFkVf4QY)] [[Code]](https://github.com/chronos123/SpND-ICML2025)<br>

* **Panorama Generation From NFoV Image Done Right.**<br>
*Dian Zheng, Cheng Zhang, Xiao-Ming Wu, Cao Li, Chengfei Lv, Jian-Fang Hu, Wei-Shi Zheng.*<br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2503.18420)] [[Project](https://isee-laboratory.github.io/PanoDecouple/)] [[Code]](https://github.com/iSEE-Laboratory/PanoDecouple)<br>

* **CubeDiff: Repurposing Diffusion-Based Image Models for Panorama Generation.**<br>
*Nikolai Kalischek, Michael Oechsle, Fabian Manhardt, Philipp Henzler, Konrad Schindler, Federico Tombari.*<br>
ICLR 2025. [[PDF](https://arxiv.org/abs/2501.17162)] [[Project]](https://cubediff.github.io/)<br>

* **Autoregressive Omni-Aware Outpainting for Open-Vocabulary 360-Degree Image Generation.**<br>
*Zhuqiang Lu, Kun Hu, Chaoyue Wang, Lei Bai, Zhiyong Wang.*<br>
AAAI 2024. [[PDF](https://arxiv.org/abs/2309.03467)] [[Code]](https://github.com/zhuqiangLu/AOG-NET-360)<br>

* **360-Degree Panorama Generation from Few Unregistered NFoV Images.**<br>
*Jionghao Wang, Ziyu Chen, Jun Ling, Rong Xie, Li Song.*<br>
ACM MM 2023. [[PDF](https://arxiv.org/abs/2308.14686)] [[Code]](https://github.com/shanemankiw/Panodiff)<br>

* **Guided Co-Modulated GAN for 360° Field of View Extrapolation.**<br>
*Mohammad Reza Karimi Dastjerdi, Yannick Hold-Geoffroy, Jonathan Eisenmann, Siavash Khodadadeh, Jean-François Lalonde.*<br>
3DV 2022. [[PDF](https://arxiv.org/abs/2204.07286)] [[Project](https://lvsn.github.io/ImmerseGAN/)]<br>

* **Conditional Panoramic Image Generation via Masked Autoregressive Modeling.**<br>
*Chaoyang Wang, Xiangtai Li, Lu Qi, Xiaofan Lin, Jinbin Bai, Qianyu Zhou, Yunhai Tong.*<br>
arxiv 2025. [[PDF](https://arxiv.org/abs/2505.16862)] [[Project](https://wang-chaoyang.github.io/project/par/)] [[Code]](https://github.com/wang-chaoyang/par)<br>

* **OPa-Ma: Text Guided Mamba for 360-degree Image Out-painting.**<br>
*Penglei Gao, Kai Yao, Tiandi Ye, Steven Wang, Yuan Yao, Xiaofeng Wang.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2407.10923)] [[Code]](https://github.com/PengleiGao/OPaMa)<br>

* **Diffusion360: Seamless 360 Degree Panoramic Image Generation based on Diffusion Models.**<br>
*Mengyang Feng, Jinlin Liu, Miaomiao Cui, Xuansong Xie.*<br>
arxiv 2023. [[PDF](https://arxiv.org/abs/2311.13141)] [[Code]](https://github.com/ArcherFMY/SD-T2I-360PanoImage)<br>

### Emerging 3D Applications

Recent text-driven 360-degree 3D scene generation methods utilize 360-degree panorama generation to bridge the gap between text prompts and 360-degree 3D scene reconstruction.

* **LayerPano3D: Layered 3D Panorama for Hyper-Immersive Scene Generation.**<br>
*Shuai Yang, Jing Tan, Mengchen Zhang, Tong Wu, Yixuan Li, Gordon Wetzstein, Ziwei Liu, Dahua Lin.*<br>
SIGGRAPH 2025. [[PDF](https://arxiv.org/abs/2408.13252)] [[Project](https://ys-imtech.github.io/projects/LayerPano3D/)] [[Code]](https://github.com/YS-IMTech/LayerPano3D)<br>

* **DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting.**<br>
*Shijie Zhou, Zhiwen Fan, Dejia Xu, Haoran Chang, Pradyumna Chari, Tejas Bharadwaj, Suya You, Zhangyang Wang, Achuta Kadambi.*<br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2404.06903)] [[Project](https://dreamscene360.github.io/)]  [[Code]](https://github.com/ShijieZhou-UCLA/DreamScene360)<br>

* **FastScene: Text-Driven Fast 3D Indoor Scene Generation via Panoramic Gaussian Splatting.**<br>
*Yikun Ma, Dandan Zhan, Zhi Jin.*<br>
IJCAI 2024. [[PDF](https://arxiv.org/abs/2405.05768)] [[Code]](https://github.com/Mr-Ma-yikun/FastScene)<br>

* **SceneDreamer360: Text-Driven 3D-Consistent Scene Generation with Panoramic Gaussian Splatting.**<br>
*Wenrui Li, Yapeng Mi, Fucheng Cai, Zhe Yang, Wangmeng Zuo, Xingtao Wang, Xiaopeng Fan.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2408.13711)] [[Project](https://scenedreamer360.github.io/)] [[Code]](https://github.com/liwrui/SceneDreamer360)<br>

* **HoloDreamer: Holistic 3D Panoramic World Generation from Text Descriptions.**<br>
*Haiyang Zhou, Xinhua Cheng, Wangbo Yu, Yonghong Tian, Li Yuan.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2407.15187)] [[Project](https://zhouhyocean.github.io/holodreamer/)] [[Code]](https://github.com/zhouhyOcean/HoloDreamer)<br>

### Text-Driven 360-Degree Panoramic Video Generation

Recent progress in text-driven 360-degree panoramic image synthesis has spurred research into the more challenging task: text-driven 360-degree panoramic video generation.

* **DynamicScaler: Seamless and Scalable Video Generation for Panoramic Scenes.**<br>
*Jinxiu Liu, Shaoheng Lin, Yinxiao Li, Ming-Hsuan Yang.*<br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2412.11100v1)] [[Project](https://dynamic-scaler.pages.dev/)] [[Code]](https://github.com/sh-Lin/DynamicScaler)<br>

* **PanoDiT: Panoramic Videos Generation with Diffusion Transformer.**<br>
*Muyang Zhang, Yuzhi Chen, Rongtao Xu, Changwei Wang, Jinming Yang, Weiliang Meng, Jianwei Guo, Huihuang Zhao, and Xiaopeng Zhang.*<br>
AAAI 2025. [[PDF](https://ojs.aaai.org/index.php/AAAI/article/view/33089)]<br>

* **360DVD: Controllable Panorama Video Generation with 360-Degree Video Diffusion Model.**<br>
*Qian Wang, Weiqi Li, Chong Mou, Xinhua Cheng, Jian Zhang.*<br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2401.06578)] [[Project](https://akaneqwq.github.io/360DVD/)] [[Code]](https://github.com/Akaneqwq/360DVD)<br>

* **PanoWan: Lifting Diffusion Video Generation Models to 360° with Latitude/Longitude-aware Mechanisms.**<br>
*Yifei Xia, Shuchen Weng, Siqi Yang, Jingqi Liu, Chengxuan Zhu, Minggui Teng, Zijian Jia, Han Jiang, Boxin Shi.*<br>
arxiv 2025. [[PDF](https://arxiv.org/abs/2505.22016)] [[Project](https://panowan.variantconst.com/)] [[Code]](https://github.com/VariantConst/PanoWan)<br>

* **VideoPanda: Video Panoramic Diffusion with Multi-view Attention.**<br>
*Kevin Xie, Amirmojtaba Sabour, Jiahui Huang, Despoina Paschalidou, Greg Klar, Umar Iqbal, Sanja Fidler, Xiaohui Zeng.*<br>
arxiv 2025. [[PDF](https://arxiv.org/abs/2504.11389)] [[Project](https://research.nvidia.com/labs/toronto-ai/VideoPanda/)]<br>

* **SphereDiff: Tuning-free Omnidirectional Panoramic Image and Video Generation via Spherical Latent Representation.**<br>
*Minho Park, Taewoong Kang, Jooyeol Yun, Sungwon Hwang, Jaegul Choo.*<br>
arxiv 2025. [[PDF](https://arxiv.org/abs/2504.14396)] [[Project](https://pmh9960.github.io/research/SphereDiff/)] [[Code]](https://github.com/pmh9960/SphereDiff)<br>



### Benchmark

Quantitative Comparison of Representative Text-Driven 360-Degree Panorama Generation. We employ an out-of-domain dataset, [ODI-SR](https://github.com/wangh-allen/LAU-Net), on which none of the models have been explicitly trained. Metrics are based on [evaluation criteria](#evaluation-metrics). Inference time is for generating a 1024×512 panorama. The **best** and <ins>second-best</ins> results are highlighted.

<table style="width:100%;">
  <colgroup>
    <col style="width: 14%" />
    <col style="width: 7%" />
    <col style="width: 13%" />
    <col style="width: 7%" />
    <col style="width: 7%" />
    <col style="width: 7%" />
    <col style="width: 12%" />
    <col style="width: 7%" />
    <col style="width: 12%" />
    <col style="width: 14%" />
  </colgroup>
  <thead>
    <tr class="header">
      <th>Method</th>
      <th>FID ↓</th>
      <th>KID (×10⁻²) ↓</th>
      <th>IS ↑</th>
      <th>CS ↑</th>
      <th>FAED ↓</th>
      <th>OmniFID ↓</th>
      <th>DS ↓</th>
      <th>Inference (s)</th>
      <th>GPU Memory (GB) ↓</th> <!-- New column header -->
    </tr>
  </thead>
  <tbody>
    <!-- Category Row: Text-Only Generation -->
    <tr class="odd">
      <td colspan="10" style="text-align: center;"><strong>Text-Only Generation</strong></td>
    </tr>
    <!-- Data Rows for Text-Only Generation -->
    <tr class="even">
      <td>Text2Light</td>
      <td style="text-align: center;">72.63</td>
      <td style="text-align: center;">1.54</td>
      <td style="text-align: center;">5.35</td>
      <td style="text-align: center;"><u>19.20</u></td>
      <td style="text-align: center;">18.10</td>
      <td style="text-align: center;">99.81</td>
      <td style="text-align: center;">5.38</td>
      <td style="text-align: center;">33</td>
      <td style="text-align: center;">12.5</td> <!-- Placeholder -->
    </tr>
    <tr class="odd">
      <td>Diffusion360</td>
      <td style="text-align: center;">70.32</td>
      <td style="text-align: center;">2.00</td>
      <td style="text-align: center;">5.29</td>
      <td style="text-align: center;">18.74</td>
      <td style="text-align: center;"><strong>12.43</strong></td>
      <td style="text-align: center;"><u>92.23</u></td>
      <td style="text-align: center;">0.94</td>
      <td style="text-align: center;"><u>3</u></td>
      <td style="text-align: center;"><strong>3.5</strong></td>
    </tr>
    <tr class="even">
      <td>StitchDiffusion</td>
      <td style="text-align: center;">76.69</td>
      <td style="text-align: center;">2.04</td>
      <td style="text-align: center;"><strong>7.36</strong></td>
      <td style="text-align: center;"><u>19.20</u></td>
      <td style="text-align: center;">15.58</td>
      <td style="text-align: center;">108.63</td>
      <td style="text-align: center;">1.07</td>
      <td style="text-align: center;">28</td>
      <td style="text-align: center;"><u>3.6</u></td>
    </tr>
    <tr class="odd">
      <td>PanFusion</td>
      <td style="text-align: center;"><strong>61.23</strong></td>
      <td style="text-align: center;"><strong>1.07</strong></td>
      <td style="text-align: center;">6.16</td>
      <td style="text-align: center;">18.96</td>
      <td style="text-align: center;"><u>13.16</u></td>
      <td style="text-align: center;"><strong>92.22</strong></td>
      <td style="text-align: center;">0.85</td>
      <td style="text-align: center;">30</td>
      <td style="text-align: center;">26.3</td>
    </tr>
    <tr class="even">
      <td>PAR</td>
      <td style="text-align: center;"><u>64.96</u></td>
      <td style="text-align: center;"><u>1.49</u></td>
      <td style="text-align: center;"><u>6.68</u></td>
      <td style="text-align: center;">18.91</td>
      <td style="text-align: center;">13.99</td>
      <td style="text-align: center;">104.02</td>
      <td style="text-align: center;"><u>0.76</u></td>
      <td style="text-align: center;">17</td>
      <td style="text-align: center;">18.6</td>
    </tr>
    <tr class="odd">
      <td>SMGD</td>
      <td style="text-align: center;">74.91</td>
      <td style="text-align: center;">2.00</td>
      <td style="text-align: center;">4.23</td>
      <td style="text-align: center;"><strong>19.22</strong></td>
      <td style="text-align: center;">16.78</td>
      <td style="text-align: center;">106.68</td>
      <td style="text-align: center;"><strong>0.75</strong></td>
      <td style="text-align: center;"><strong>2</strong></td>
      <td style="text-align: center;">8.0</td>
    </tr>
    <!-- Category Row: Text-Driven NFoV Outpainting -->
    <tr class="even">
      <td colspan="10" style="text-align: center;"><strong>Text-Driven NFoV Outpainting</strong></td>
    </tr>
    <!-- Data Rows for Text-Driven NFoV Outpainting -->
    <tr class="odd">
      <td>PanoDiff</td>
      <td style="text-align: center;"><ins>65.94</ins></td>
      <td style="text-align: center;"><ins>2.44</ins></td>
      <td style="text-align: center;"><ins>4.72</ins></td>
      <td style="text-align: center;">19.02</td>
      <td style="text-align: center;">10.24</td>
      <td style="text-align: center;">122.30</td>
      <td style="text-align: center;"><ins>1.10</ins></td>
      <td style="text-align: center;">48</td>
      <td style="text-align: center;">36.0</td>
    </tr>
    <tr class="even">
      <td>Diffusion360</td>
      <td style="text-align: center;"><strong>64.19</strong></td>
      <td style="text-align: center;"><strong>2.05</strong></td>
      <td style="text-align: center;">4.53</td>
      <td style="text-align: center;">17.92</td>
      <td style="text-align: center;"><strong>5.50</strong></td>
      <td style="text-align: center;"><strong>101.39</strong></td>
      <td style="text-align: center;"><strong>0.72</strong></td>
      <td style="text-align: center;"><strong>4</strong></td>
      <td style="text-align: center;"><strong>3.7</strong></td>
    </tr>
    <tr class="odd">
      <td>SpND</td>
      <td style="text-align: center;">69.54</td>
      <td style="text-align: center;">3.00</td>
      <td style="text-align: center;">3.77</td>
      <td style="text-align: center;"><ins>19.17</ins></td>
      <td style="text-align: center;"><ins>8.67</ins></td>
      <td style="text-align: center;">119.05</td>
      <td style="text-align: center;">1.40</td>
      <td style="text-align: center;">22</td>
      <td style="text-align: center;"><ins>16.7</ins></td>
    </tr>
    <tr class="even">
      <td>DreamCube</td>
      <td style="text-align: center;">66.15</td>
      <td style="text-align: center;"><strong>2.05</strong></td>
      <td style="text-align: center;"><strong>4.88</strong></td>
      <td style="text-align: center;"><strong>19.26</strong></td>
      <td style="text-align: center;">15.87</td>
      <td style="text-align: center;"><ins>115.52</ins></td>
      <td style="text-align: center;"><ins>1.10</ins></td>
      <td style="text-align: center;"><ins>12</ins></td>
      <td style="text-align: center;"><ins>16.7</ins></td>
    </tr>
  </tbody>
</table>



### Dataset

Summary of popular datasets used in text-driven 360-degree panorama generation. Categories are indoor (I), outdoor (O), or hybrid (I, O).

|  **Dataset**  | **Year**     | **Category**    | **# Samples** | **Resolution** |  **License**                                     |
|:-------------:|:------------:|:---------------:|:-------------:|:--------------:|:------------------------------------------------:|
| [SUN360](https://vision.cs.princeton.edu/projects/2012/SUN360/data/)        | 2012         | I & O            | 67,583       | 9104 × 4552    |  [Custom](https://3dvision.princeton.edu/projects/2012/SUN360/)                                                |
| [Matterport3D](https://niessner.github.io/Matterport/)  | 2017         | I                | 10,800       | 2048 x 1024    |  [Custom](https://kaldir.vc.in.tum.de/matterport/MP_TOS.pdf)                                                |
| [Laval Indoor](http://hdrdb.com/indoor/)  | 2017         | I                | 2,233        | 7668  × 3884   |  [Custom](https://www.dropbox.com/scl/fi/r6niq8zmm0w03xgswj4b7/Laval-Indoor-HDR-Database-EULA.pdf?rlkey=yeetamvzevcmxrkcf9hy23ita&e=1&dl=0)     |
| [Laval Outdoor](http://hdrdb.com/outdoor/) | 2019         | O                | 205          | 7668  × 3884   |  [Custom](https://www.dropbox.com/scl/fi/17pka14s69c8c02gnpqg4/Laval-Outdoor-HDR-Database-EULA.pdf?rlkey=ptb0j0l46aj08laion6y551e3&e=1&dl=0)    |
| [Structured3D](https://structured3d-dataset.org/)  | 2020         | I                | 196,515      | 1024  × 512    |  [Custom](https://drive.google.com/file/d/13ZwWpU_557ZQccwOUJ8H5lvXD7MeZFMa/view)                                                  |
| [Pano360](https://spec.is.tue.mpg.de/)       | 2021         | I & O            | 35,000       | 8192  × 4096   |  [Custom](https://spec.is.tue.mpg.de/license.html)                                                |
| [Polyhaven](https://polyhaven.com/hdris)     | 2025            | I & O            | 786          | 8192  × 4096   | [CC0](https://polyhaven.com/license)             |
| [Humus](https://www.humus.name/index.php?page=Textures)         | 2025            | I & O            | 139          | 8192  × 4096   | [CC BY 3.0](https://www.humus.name/index.php?page=Textures)                                                |

### Evaluation Metrics

#### Universal Metrics

* Fréchet Inception Distance (FID) [code](https://lightning.ai/docs/torchmetrics/stable/image/frechet_inception_distance.html)

* Kernel Inception Distance (KID) [code](https://lightning.ai/docs/torchmetrics/stable/image/kernel_inception_distance.html)

* Inception Score (IS) [code](https://lightning.ai/docs/torchmetrics/stable/image/inception_score.html)

* CLIP Score (CS) [code](https://lightning.ai/docs/torchmetrics/stable/multimodal/clip_score.html)

#### Panorama-Specific Metrics

* Fréchet Auto-Encoder Distance (FAED) [code](https://github.com/chengzhag/PanFusion)

* Omnidirectional FID (OmniFID) [paper](https://link.springer.com/chapter/10.1007/978-3-031-72989-8_16)

* Discontinuity Score (DS) [paper](https://link.springer.com/chapter/10.1007/978-3-031-72989-8_16)

* Distortion-perception FID (Distort-FID) [code](https://github.com/iSEE-Laboratory/PanoDecouple)


### Citation

If this repository benefits your research, please consider citing our paper.

```bibtex
@article{wang2025survey,
    author  = {Wang, Hai and Xiang, Xiaoyu and Xia, Weihao and Xue, Jing-Hao},
    title   = {A Survey on Text-Driven 360-Degree Panorama Generation},
    journal = {arxiv preprint arxiv: 2502.14799},
    year={2025}
  }
```