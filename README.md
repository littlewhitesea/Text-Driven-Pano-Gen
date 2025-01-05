# Text-to-360Pano-Gen
A Survey on Text-Driven 360-Degree Panorama Generation

## Text-based 360-degree panorama generation

**DiffPano: Scalable and Consistent Text to Panorama Generation with Spherical Epipolar-Aware Diffusion.**<br>
*Weicai Ye, Chenhao Ji, Zheng Chen, Junyao Gao, Xiaoshui Huang, Song-Hai Zhang, Wanli Ouyang, Tong He, Cairong Zhao, Guofeng Zhang.*<br>
NeurIPS 2024. [[PDF](https://arxiv.org/abs/2410.24203)] [[Project](https://zju3dv.github.io/DiffPano/)] [[Code]](https://github.com/zju3dv/DiffPano)<br>
Comments: 

**PanoFree: Tuning-Free Holistic Multi-view Image Generation with Cross-view Self-Guidance.**<br>
*Aoming Liu, Zhong Li, Zhang Chen, Nannan Li, Yi Xu, Bryan A. Plummer.*<br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2408.02157)] [[Project](https://panofree.github.io/)] [[Code]](https://github.com/zxcvfd13502/PanoFree)<br>
Comments: It takes text prompts as guidance to create multi-view perspective images through sequential warping and inpainting steps, which can be stitched into a wide-angle panorama. 360 panorama (only horizontal 360-degree) is regarded as the central part of the final 360-degree panorama, then expansion and closing stages are employed to generate final 360-degree panorama using a training-free method.

**Taming Stable Diffusion for Text to 360° Panorama Image Generation.**<br>
*Cheng Zhang, Qianyi Wu, Camilo Cruz Gambardella, Xiaoshui Huang, Dinh Phung, Wanli Ouyang, Jianfei Cai.*<br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2404.07949)] [[Project](https://chengzhag.github.io/publication/panfusion/)] [[Code]](https://github.com/chengzhag/PanFusion)<br>
Comments: It proposes a dual-branch pipeline for 360-degree panorama generation based on SD and LoRA. Specifically, one branch is used for the generation of panorama latent, while the other branch is utilized for perspective latent. The two branches communicate with each other through equirectangular-perspective projection attention modules.

**EdgeRelight360: Text-Conditioned 360-Degree HDR Image Generation for Real-Time On-Device Video Portrait Relighting.**<br>
*Min-Hui Lin, Mahesh Reddy, Guillaume Berger, Michel Sarkis, Fatih Porikli, Ning Bi.*<br>
CVPRW 2024. [[PDF](https://arxiv.org/abs/2404.09918)]<br>

**Diffusion360: Seamless 360 Degree Panoramic Image Generation based on Diffusion Models.**<br>
*Mengyang Feng, Jinlin Liu, Miaomiao Cui, Xuansong Xie.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2311.13141)] [[Code]](https://github.com/ArcherFMY/SD-T2I-360PanoImage)<br>
Comments: It adopts dreambooth strategy to fine-tune stable diffusion for text-driven 360-degree panorama generation. Specifically, it proposes circular blending in the latent space and VAE decoder to keep boundary continuity. In addition, it utilizes ControlNet-outpainting to generate a 360-degree panorama from an ordinary image at perspective view, guided by an input text prompt.

**Customizing 360-degree panoramas through text-to-image diffusion models.**<br>
*Hai Wang, Xiaoyu Xiang, Yuchen Fan, Jing-Hao Xue.*<br>
WACV 2024. [[PDF](https://arxiv.org/abs/2310.18840)] [[Project](https://littlewhitesea.github.io/stitchdiffusion.github.io/)] [[Code]](https://github.com/littlewhitesea/StitchDiffusion)<br>

**Autoregressive Omni-Aware Outpainting for Open-Vocabulary 360-Degree Image Generation.**<br>
*Zhuqiang Lu, Kun Hu, Chaoyue Wang, Lei Bai, Zhiyong Wang.*<br>
AAAI 2024. [[PDF](https://arxiv.org/abs/2309.03467)] [[Code]](https://github.com/zhuqiangLu/AOG-NET-360)<br>
Comments: It propose an autoregressive generative network to generate 360-degree panorama by outpainting an incomplete 360-degree panorama progressively with nFoV and text guidances jointly or individually.

**MVDiffusion: Enabling Holistic Multi-view Image Generation with Correspondence-Aware Diffusion.**<br>
*Shitao Tang, Fuyang Zhang, Jiacheng Chen, Peng Wang, Yasutaka Furukawa.*<br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2307.01097)] [[Project](https://mvdiffusion.github.io/)] [[Code]](https://github.com/Tangshitao/MVDiffusion)<br>
Comments: Actually, in terms of 360-degree panorama generation, it adopts a text-driven narrow field-of-view outpainting method, and the generated image is not a real 360-degree panorama, it only covers 360-degree field-of-view horizontally, which is also indicated in PanFusion.

**360-Degree Panorama Generation from Few Unregistered NFoV Images.**<br>
*Jionghao Wang, Ziyu Chen, Jun Ling, Rong Xie, Li Song.*<br>
ACM MM 2023. [[PDF](https://arxiv.org/abs/2308.14686)] [[Code]](https://github.com/shanemankiw/Panodiff)<br>
Comments: Incomplete panorama and text prompts are as control signals instead of text prompts only.

**Text2Light: Zero-Shot Text-Driven HDR Panorama Generation.**<br>
*Zhaoxi Chen, Guangcong Wang, Ziwei Liu.*<br>
TOG 2022 (SIGGRAPH Asia). [[PDF](https://arxiv.org/abs/2209.09898)] [[Project](https://frozenburning.github.io/projects/text2light/)] [[Code]](https://github.com/FrozenBurning/Text2Light)<br>

## Text-based 360-degree video generation

**360DVD: Controllable Panorama Video Generation with 360-Degree Video Diffusion Model.**<br>
*Qian Wang, Weiqi Li, Chong Mou, Xinhua Cheng, Jian Zhang.*<br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2401.06578)] [[Project](https://akaneqwq.github.io/360DVD/)] [[Code]](https://github.com/Akaneqwq/360DVD)<br>

**Imagine360: Immersive 360 Video Generation from Perspective Anchor.**<br>
*Jing Tan, Shuai Yang, Tong Wu, Jingwen He, Yuwei Guo, Ziwei Liu, Dahua Lin.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2412.03552)] [[Project](https://ys-imtech.github.io/projects/Imagine360/)] [[Code]](https://github.com/YS-IMTech/Imagine360)<br>

## Null-Text 360-degree panorama outpainting

**2S-ODIS: Two-Stage Omni-Directional Image Synthesis by Geometric Distortion Correctionn.**<br>
*Atsuya Nakata, Takao Yamanaka.*<br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2409.09969)] [[Code]](https://github.com/islab-sophia/2S-ODIS)<br>

**CamFreeDiff: Camera-free Image to Panorama Generation with Diffusion Model.**<br>
*Xiaoding Yuan, Shitao Tang, Kejie Li, Alan Yuille, Peng Wang.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2407.07174)]<br>

**HORIZON: High-Resolution Semantically Controlled Panorama Synthesis.**<br>
*Kun Yan, Lei Ji, Chenfei Wu, Jian Liang, Ming Zhou, Nan Duan, Shuai Ma.*<br>
AAAI 2024. [[PDF](https://ojs.aaai.org/index.php/AAAI/article/view/28463)]<br>

**Dream360: Diverse and Immersive Outdoor Virtual Scene Creation via Transformer-Based 360 Image Outpainting.**<br>
*Hao Ai, Zidong Cao, Haonan Lu, Chen Chen, Jian Ma, Pengyuan Zhou, Tae-Kyun Kim, Pan Hui, Lin Wang.*<br>
VR 2024. [[PDF](https://arxiv.org/abs/2401.10564)]<br>

**PanoDiffusion: 360-degree Panorama Outpainting via Diffusion.**<br>
*Tianhao Wu, Chuanxia Zheng, Tat-Jen Cham.*<br>
ICLR 2024. [[PDF](https://arxiv.org/abs/2307.03177)] [[Project](https://sm0kywu.github.io/panodiffusion/)] [[Code]](https://github.com/PanoDiffusion/PanoDiffusion)<br>

## Text-Driven 360-degree panoramic image-to-image translation

**360PanT: Training-Free Text-Driven 360-Degree Panorama-to-Panorama Translation.**<br>
*Hai Wang, Jing-Hao Xue.*<br>
WACV 2025. [[PDF](https://arxiv.org/abs/2409.08397)] [[Project](https://littlewhitesea.github.io/360PanT.github.io/)] [[Code]](https://github.com/littlewhitesea/360PanT)<br>

**Panoramic Image-to-Image Translation.**<br>
*Soohyun Kim, Junho Kim, Taekyung Kim, Hwan Heo, Seungryong Kim, Jiyoung Lee, Jin-Hwa Kim.*<br>
arxiv 2023. [[PDF](https://arxiv.org/abs/2304.04960)]<br>
Comments: It doesn't involve text prompts.

## 360-degree panoramic image super-resolution

**OmniSSR: Zero-shot Omnidirectional Image Super-Resolution using Stable Diffusion Model.**<br>
*Runyi Li, Xuhan Sheng, Weiqi Li, Jian Zhang.*<br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2404.10312)] [[Project](https://lirunyi2001.github.io/projects/omnissr/)] [[Code]](https://github.com/LiRunyi2001/OmniSSR)<br>

**OSRT: Omnidirectional Image Super-Resolution with Distortion-aware Transformer.**<br>
*Fanghua Yu, Xintao Wang, Mingdeng Cao, Gen Li, Ying Shan, Chao Dong.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2302.03453)] [[Code]](https://github.com/Fanghua-Yu/OSRT)<br>

## Evaluation Metrics

**Geometry Fidelity for Spherical Images.**<br>
*Anders Christensen, Nooshin Mojab, Khushman Patel, Karan Ahuja, Zeynep Akata, Ole Winther, Mar Gonzalez-Franco, Andrea Colaco.*<br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2407.18207)]<br>

**AIGCOIQA2024: Perceptual Quality Assessment of AI Generated Omnidirectional Images.**<br>
*Liu Yang, Huiyu Duan, Long Teng, Yucheng Zhu, Xiaohong Liu, Menghan Hu, Xiongkuo Min, Guangtao Zhai, Patrick Le Callet.*<br>
ICIP 2024. [[PDF](https://arxiv.org/abs/2404.01024)]<br>

**Perceptual Depth Quality Assessment of Stereoscopic Omnidirectional Images.**<br>
*Wei Zhou, Zhou Wang.*<br>
TCSVT 2024. [[PDF](https://arxiv.org/abs/2408.10134)]<br>

## 3D reconstruction using 360-degree panoramas

**360Recon: An Accurate Reconstruction Method Based on Depth Fusion from 360 Images.**<br>
*Zhongmiao Yan, Qi Wu, Songpengcheng Xia, Junyuan Deng, Xiang Mu, Renbiao Jin, Ling Pei.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2411.19102)] <br>

**ODGS: 3D Scene Reconstruction from Omnidirectional Images with 3D Gaussian Splattings.**<br>
*Suyoung Lee, Jaeyoung Chung, Jaeyoo Huh, Kyoung Mu Lee.*<br>
NeurIPS 2024. [[PDF](https://arxiv.org/abs/2410.20686)] [[Code]](https://github.com/esw0116/ODGS)<br>

**OmniGS: Fast Radiance Field Reconstruction using Omnidirectional Gaussian Splatting.**<br>
*Longwei Li, Huajian Huang, Sai-Kit Yeung, Hui Cheng.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2404.03202)]<br>

**MaGRITTe: Manipulative and Generative 3D Realization from Image, Topview and Text.**<br>
*Takayuki Hara, Tatsuya Harada.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2404.00345)] [[Project](https://hara012.github.io/MaGRITTe-project/)]<br>

**LayerPano3D: Layered 3D Panorama for Hyper-Immersive Scene Generation.**<br>
*Shuai Yang, Jing Tan, Mengchen Zhang, Tong Wu, Yixuan Li, Gordon Wetzstein, Ziwei Liu, Dahua Lin.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2408.13252)] [[Project](https://ys-imtech.github.io/projects/LayerPano3D/)] [[Code]](https://github.com/YS-IMTech/LayerPano3D)<br>

**SceneDreamer360: Text-Driven 3D-Consistent Scene Generation with Panoramic Gaussian Splatting.**<br>
*Wenrui Li, Yapeng Mi, Fucheng Cai, Zhe Yang, Wangmeng Zuo, Xingtao Wang, Xiaopeng Fan.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2408.13711)] [[Code]](https://github.com/liwrui/SceneDreamer360)<br>

**Pano2Room: Novel View Synthesis from a Single Indoor Panorama.**<br>
*Guo Pu, Yiming Zhao, Zhouhui Lian.*<br>
SIGGRAPH Asia 2024. [[PDF](https://arxiv.org/abs/2408.11413)] [[Code]](https://github.com/TrickyGo/Pano2Room)<br>

**HoloDreamer: Holistic 3D Panoramic World Generation from Text Descriptions.**<br>
*Haiyang Zhou, Xinhua Cheng, Wangbo Yu, Yonghong Tian, Li Yuan.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2407.15187)] [[Project](https://zhouhyocean.github.io/holodreamer/)] [[Code]](https://github.com/zhouhyOcean/HoloDreamer)<br>

**DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting.**<br>
*Shijie Zhou, Zhiwen Fan, Dejia Xu, Haoran Chang, Pradyumna Chari, Tejas Bharadwaj, Suya You, Zhangyang Wang, Achuta Kadambi.*<br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2404.06903)] [[Project](https://dreamscene360.github.io/)]<br>

**FastScene: Text-Driven Fast 3D Indoor Scene Generation via Panoramic Gaussian Splatting.**<br>
*Yikun Ma, Dandan Zhan, Zhi Jin.*<br>
IJCAI 2024. [[PDF](https://arxiv.org/abs/2405.05768)] [[Code]](https://github.com/Mr-Ma-yikun/FastScene)<br>

**PERF: Panoramic Neural Radiance Field from a Single Panorama.**<br>
*Guangcong Wang, Peng Wang, Zhaoxi Chen, Wenping Wang, Chen Change Loy, Ziwei Liu.*<br>
TPAMI 2024. [[PDF](https://arxiv.org/abs/2310.16831)] [[Project](https://perf-project.github.io/)] [[Code]](https://github.com/perf-project/PeRF)<br>


## Application

**OmniDrag: Enabling Motion Control for Omnidirectional Image-to-Video Generation.**<br>
*Weiqi Li, Shijie Zhao, Chong Mou, Xuhan Sheng, Zhenyu Zhang, Qian Wang, Junlin Li, Li Zhang, Jian Zhang.*<br>
arxiv 2024. [[PDF](https://arxiv.org/abs/2412.09623)] [[Project](https://lwq20020127.github.io/OmniDrag/)] [[Code]](https://github.com/lwq20020127/OmniDrag)<br>
