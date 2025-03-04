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

* **Diffusion360: Seamless 360 Degree Panoramic Image Generation based on Diffusion Models.**<br>
*Mengyang Feng, Jinlin Liu, Miaomiao Cui, Xuansong Xie.*<br>
arxiv 2023. [[PDF](https://arxiv.org/abs/2311.13141)] [[Code]](https://github.com/ArcherFMY/SD-T2I-360PanoImage)<br>

### Text-Driven NFoV Outpainting

Text-driven narrow field-of-view (NFoV) outpainting enhances user control by conditioning the generation process on both textual prompts and initial narrow NFoV images.

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

* **OPa-Ma: Text Guided Mamba for 360-degree Image Out-painting.**<br>
*Penglei Gao, Kai Yao, Tiandi Ye, Steven Wang, Yuan Yao, Xiaofeng Wang.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2407.10923)] [[Code]](https://github.com/PengleiGao/OPaMa)<br>

* **Diffusion360: Seamless 360 Degree Panoramic Image Generation based on Diffusion Models.**<br>
*Mengyang Feng, Jinlin Liu, Miaomiao Cui, Xuansong Xie.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2311.13141)] [[Code]](https://github.com/ArcherFMY/SD-T2I-360PanoImage)<br>

### Emerging 3D Applications

Recent text-driven 360-degree 3D scene generation methods utilize 360-degree panorama generation to bridge the gap between text prompts and 360-degree 3D scene reconstruction.

* **DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting.**<br>
*Shijie Zhou, Zhiwen Fan, Dejia Xu, Haoran Chang, Pradyumna Chari, Tejas Bharadwaj, Suya You, Zhangyang Wang, Achuta Kadambi.*<br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2404.06903)] [[Project](https://dreamscene360.github.io/)]  [[Code]](https://github.com/ShijieZhou-UCLA/DreamScene360)<br>

* **FastScene: Text-Driven Fast 3D Indoor Scene Generation via Panoramic Gaussian Splatting.**<br>
*Yikun Ma, Dandan Zhan, Zhi Jin.*<br>
IJCAI 2024. [[PDF](https://arxiv.org/abs/2405.05768)] [[Code]](https://github.com/Mr-Ma-yikun/FastScene)<br>

* **SceneDreamer360: Text-Driven 3D-Consistent Scene Generation with Panoramic Gaussian Splatting.**<br>
*Wenrui Li, Yapeng Mi, Fucheng Cai, Zhe Yang, Wangmeng Zuo, Xingtao Wang, Xiaopeng Fan.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2408.13711)] [[Project](https://scenedreamer360.github.io/)] [[Code]](https://github.com/liwrui/SceneDreamer360)<br>

* **LayerPano3D: Layered 3D Panorama for Hyper-Immersive Scene Generation.**<br>
*Shuai Yang, Jing Tan, Mengchen Zhang, Tong Wu, Yixuan Li, Gordon Wetzstein, Ziwei Liu, Dahua Lin.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2408.13252)] [[Project](https://ys-imtech.github.io/projects/LayerPano3D/)] [[Code]](https://github.com/YS-IMTech/LayerPano3D)<br>

* **HoloDreamer: Holistic 3D Panoramic World Generation from Text Descriptions.**<br>
*Haiyang Zhou, Xinhua Cheng, Wangbo Yu, Yonghong Tian, Li Yuan.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2407.15187)] [[Project](https://zhouhyocean.github.io/holodreamer/)] [[Code]](https://github.com/zhouhyOcean/HoloDreamer)<br>

### Benchmark

Quantitative Comparison of Representative Text-Driven 360-Degree Panorama Generation. We employ an out-of-domain dataset, [ODI-SR](https://github.com/wangh-allen/LAU-Net), on which none of the models have been explicitly trained. Metrics are based on [evaluation criteria](#evaluation-metrics). Inference time is for generating a 1024×512 panorama. The **best** and <ins>second-best</ins> results are highlighted.

<table style="width: 100%; border-collapse: collapse;">
  <colgroup>
    <col style="width: 15%;">
    <col style="width: 10%;">
    <col style="width: 10%;">
    <col style="width: 10%;">
    <col style="width: 10%;">
    <col style="width: 10%;">
    <col style="width: 10%;">
    <col style="width: 10%;">
    <col style="width: 15%;">
  </colgroup>
  <thead>
    <tr>
      <th style="text-align: left;">Method</th>
      <th style="text-align: center;">FID &darr;</th>
      <th style="text-align: center;">KID (×10⁻²) &darr;</th>
      <th style="text-align: center;">IS &uarr;</th>
      <th style="text-align: center;">CS &uarr;</th>
      <th style="text-align: center;">FAED &darr;</th>
      <th style="text-align: center;">OmniFID &darr;</th>
      <th style="text-align: center;">DS &darr;</th>
      <th style="text-align: center;">Inference (s)</th>
    </tr>
  </thead>
  <tbody>
    <!-- Category Row: Text-Only Generation -->
    <tr>
      <td colspan="9" style="text-align: center;"><strong>Text-Only Generation</strong></td>
    </tr>
    <!-- Data Rows for Text-Only Generation -->
    <tr>
      <td style="text-align: left;">Text2Light</td>
      <td style="text-align: center;">72.63</td>
      <td style="text-align: center;"><ins>1.54</ins></td>
      <td style="text-align: center;">5.35</td>
      <td style="text-align: center;"><strong>19.20</strong></td>
      <td style="text-align: center;">18.10</td>
      <td style="text-align: center;">99.81</td>
      <td style="text-align: center;">5.38</td>
      <td style="text-align: center;">33</td>
    </tr>
    <tr>
      <td style="text-align: left;">Diffusion360</td>
      <td style="text-align: center;"><ins>70.32</ins></td>
      <td style="text-align: center;">2.00</td>
      <td style="text-align: center;">5.29</td>
      <td style="text-align: center;">18.74</td>
      <td style="text-align: center;"><strong>12.43</strong></td>
      <td style="text-align: center;"><ins>92.23</ins></td>
      <td style="text-align: center;"><ins>0.94</ins></td>
      <td style="text-align: center;"><strong>3</strong></td>
    </tr>
    <tr>
      <td style="text-align: left;">StitchDiffusion</td>
      <td style="text-align: center;">76.69</td>
      <td style="text-align: center;">2.04</td>
      <td style="text-align: center;"><strong>7.36</strong></td>
      <td style="text-align: center;"><strong>19.20</strong></td>
      <td style="text-align: center;">15.58</td>
      <td style="text-align: center;">108.63</td>
      <td style="text-align: center;">1.07</td>
      <td style="text-align: center;"><ins>28</ins></td>
    </tr>
    <tr>
      <td style="text-align: left;">PanFusion</td>
      <td style="text-align: center;"><strong>61.23</strong></td>
      <td style="text-align: center;"><strong>1.07</strong></td>
      <td style="text-align: center;"><ins>6.16</ins></td>
      <td style="text-align: center;"><ins>18.96</ins></td>
      <td style="text-align: center;"><ins>13.16</ins></td>
      <td style="text-align: center;"><strong>92.22</strong></td>
      <td style="text-align: center;"><strong>0.85</strong></td>
      <td style="text-align: center;">30</td>
    </tr>
    <!-- Category Row: Text-Driven NFoV Outpainting -->
    <tr>
      <td colspan="9" style="text-align: center;"><strong>Text-Driven NFoV Outpainting</strong></td>
    </tr>
    <!-- Data Rows for Text-Driven NFoV Outpainting -->
    <tr>
      <td style="text-align: left;">PanoDiff</td>
      <td style="text-align: center;"><ins>65.94</ins></td>
      <td style="text-align: center;"><ins>2.44</ins></td>
      <td style="text-align: center;"><strong>4.72</strong></td>
      <td style="text-align: center;"><strong>19.02</strong></td>
      <td style="text-align: center;"><ins>10.24</ins></td>
      <td style="text-align: center;"><ins>122.30</ins></td>
      <td style="text-align: center;"><ins>1.10</ins></td>
      <td style="text-align: center;"><ins>48</ins></td>
    </tr>
    <tr>
      <td style="text-align: left;">Diffusion360</td>
      <td style="text-align: center;"><strong>64.19</strong></td>
      <td style="text-align: center;"><strong>2.05</strong></td>
      <td style="text-align: center;"><ins>4.53</ins></td>
      <td style="text-align: center;"><ins>17.92</ins></td>
      <td style="text-align: center;"><strong>5.50</strong></td>
      <td style="text-align: center;"><strong>101.39</strong></td>
      <td style="text-align: center;"><strong>0.72</strong></td>
      <td style="text-align: center;"><strong>4</strong></td>
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