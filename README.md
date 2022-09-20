# ResTimeSformer
## Contents
1. [Abstract](#Abstract)
2. [Performance Benchmark](#Performance-Benchmark)
3. [Model Zoo](#Model-Zoo) 
4. [Dependencies](#Dependencies)
5. [Usage](#Usage)
6. [Acknowledgements](#Acknowledgements)
7. [Contact](#Contact)

## Abstract
Videos are frozen fragment shots of a past reality. That is no wonder why within the
last decade, and with the emergence of social media and videoconferencing tools, a huge
number of users upload, download, share, and communicate using video streams. That
being said, with the constantly increasing bit rates and the apparition of HD and 4k videos,
Quality of Experience (QoE) becomes thus a critical aspect to take into consideration in
the different communication systems. Accordingly, it become essential to evaluate the
quality of those different videos in order to be able to optimize their processing.
User Generated Videos represent however two main challenges in their evaluation process:
first, no reference pristine video is available for the sake of comparison, second, they are
altered by an unpredictable and authentic set of distortions that can occur on both spatial
and temporal dimensions.
Thereby, we introduce a blind video quality assessment model ResTimeSFormer, that
combines the advantage given by the high quality of CNNs extracted features and the
spatio-temporal aspect of the novel TimeSFormer architecture. Moreover, in order to take
full advantage of the tranformer network, we make it possible to parallelize the feature
extraction process on different nodes, for the sake of computational run time reduction.

  ![](https://github.com/hbrachemi/ResTimeSformer/blob/main/Resnet.jpg)
  ![](https://github.com/hbrachemi/ResTimeSformer/blob/main/TimeSformer_h.jpg)

## Performance Benchmark
#### LIVE-VQC

|Metric| SROCC ↑| PLCC ↑|KRCC ↑|RMSE ↓|
|------|:-------------:|:---------------:|:---------------:|:---------------:|
|BRISQUE| 0.5925 | 0.6380 | 0.4162 | 13.100
|NIQE|   0.5957 | 0.6286 | 0.4252 | 13.110 
|IL-NIQE| 0.5037 | 0.5437 | 0.3555|14.148
|GM-LOG| 0.5881 | 0.6212 | 0.4180 | 13.223
|HIGRADE| 0.6103 | 0.6332| 0.4391 | 13.027 
|FRIQUEE| 0.6579 | 0.7000 | 0.4770 | 12.198
|CORNIA|  0.6719 | 0.7183 | 0.4849 | 11.832
|HOSA| 0.6873 | 0.7414 | 0.5033 | 11.353
|ResNet-50| 0.6636 | 0.7205 | 0.4786 | 11.591
|KonCept512| 0.6645 | 0.7278 | 0.4793 | 11.626
|PaQ-2-PiQ| 0.6436 | 0.6683 | 0.4568 | 12.619
|V-BLIINDS| 0.6939 | 0.7178 | 0.5078 | 11.765
|TLVQM| 0.7988 | 0.8025 | 0.6080 | 10.145
|VIDEVAL| 0.7522 | 0.7514 | 0.5639 | 11.100
|RAPIQUE| 0.7415 | 0.7659 | 0.5576 | 10.6653
|ResNet50 + TimeSFormer|  0.7754 | 0.8288 | 0.6009 | 9.7905

#### KoNViD-1k
|Metric| SROCC ↑| PLCC ↑|KRCC ↑|RMSE ↓|
|------|:-------------:|:---------------:|:---------------:|:---------------:|
|BRISQUE| 0.6567 | 0.6576| 0.4761 | 0.4813
|NIQE|   0.5417 |0.5530 |0.3790 | 0.5336
|IL-NIQE| 0.5264 |0.5400 |0.3692| 0.5406
|GM-LOG| 0.6578 |0.6636 |0.4770 |0.4818
|HIGRADE| 0.7206| 0.7269| 0.5319 |0.4391 
|FRIQUEE| 0.7472| 0.7482 |0.5509| 0.4252
|CORNIA|  0.7169 |0.7135 |0.5231| 0.4486
|HOSA| 0.7654 |0.7664| 0.5690| 0.4142
|ResNet-50| 0.8018| 0.8104| 0.6100| 0.3749
|KonCept512| 0.7349 |0.7489 |0.5425 |0.4260
|PaQ-2-PiQ| 0.6130 |0.6014| 0.4334| 0.5148
|V-BLIINDS| 0.7101 |0.7037 |0.5188 |0.4595
|TLVQM| 0.7729| 0.7688| 0.5770| 0.4102
|VIDEVAL| 0.7832 |0.7803 |0.5845| 0.4026
|RAPIQUE| 0.8072 |0.8157| 0.6189| 0.3644
|ResNet50 + TimeSFormer|  0.8478 |0.8607| 0.6537 |0.3339


#### YouTube-UGC
|Metric| SROCC ↑| PLCC ↑|KRCC ↑|RMSE ↓|
|------|:-------------:|:---------------:|:---------------:|:---------------:|
|BRISQUE| 0.3820 | 0.3952| 0.2635| 0.5919
|NIQE|   0.2379 |0.2776 |0.1600 |0.6174
|IL-NIQE| 0.2918 |0.3302 |0.1980| 0.6052
|GM-LOG| 0.3678 |0.3920 |0.2517 |0.5896
|HIGRADE| 0.7376 |0.7216| 0.5478| 0.4471 
|FRIQUEE| 0.7652 |0.7571 |0.5688 |0.4169
|CORNIA|  0.5972| 0.6057| 0.4211| 0.5136
|HOSA| 0.6025 |0.6047 |0.4257 |0.5132
|ResNet-50| 0.7183 |0.7097| 0.5229 |0.4538
|KonCept512| 0.5872 |0.5940 |0.4101 |0.5135
|PaQ-2-PiQ| 0.2658 |0.2935| 0.1778| 0.6153
|V-BLIINDS| 0.5590 |0.5551 |0.3899 |0.5356
|TLVQM| 0.6693 |0.6590| 0.4816| 0.4849
|VIDEVAL| 0.7787 |0.7733 |0.5830 |0.4049
|RAPIQUE| 0.7610 |0.7620| 0.5610 |0.4060
|ResNet50 + TimeSFormer|  0,8497 | 0,8611| 0,6561| 0,3403


## Model Zoo
[The features](https://drive.google.com/drive/folders/1j16rD5OdO8lia4uiYu9hPXBuPMH2Pqsc?usp=sharing) exctracted from the different datasets and the weights of the different models can be found [here](https://drive.google.com/drive/folders/1rVdQ5K41EvOPecJg9u6DoyBemWZgl5gt?usp=sharing).

## Dependencies
Dependencies can also be directly downloaded from the notebooks, packages required are installed using the following commands:
- !pip install 'git+https://github.com/facebookresearch/fvcore'
- !pip install simplejson
- !pip install av
- !pip install timm==0.4.9
- !pip install einops
- !pip install slidingwindow

## Usage
Both features extraction and the train/test codes are available in the ipynb notebooks.
Please make sure to instanciate the model by setting the number of patches and frames to p=45 and f=10, p=15 and f=8 or p=50 and f=20 with the LIVE-VQC, KoNViD-1k and YouTube-UGC datasets respectively before trying to load the available weights as those parametres correspond to the configuration of the model used in the training phase.  

## Acknowledgements

Our code uses the [TimeSformer](https://github.com/facebookresearch/TimeSformer) architecture, we are thus thankful to the authors for making their code source available.
```BibTeX
@inproceedings{gberta_2021_ICML,
    author  = {Gedas Bertasius and Heng Wang and Lorenzo Torresani},
    title = {Is Space-Time Attention All You Need for Video Understanding?},
    booktitle   = {Proceedings of the International Conference on Machine Learning (ICML)}, 
    month = {July},
    year = {2021}
}
```

Moreover, TimeSformer is built on top of [PySlowFast](https://github.com/facebookresearch/SlowFast) and [pytorch-image-models](https://github.com/rwightman/pytorch-image-models). We find it thus useful citing these works as well:

```BibTeX
@misc{fan2020pyslowfast,
  author =       {Haoqi Fan and Yanghao Li and Bo Xiong and Wan-Yen Lo and
                  Christoph Feichtenhofer},
  title =        {PySlowFast},
  howpublished = {\url{https://github.com/facebookresearch/slowfast}},
  year =         {2020}
}
```

```BibTeX
@misc{rw2019timm,
  author = {Ross Wightman},
  title = {PyTorch Image Models},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  doi = {10.5281/zenodo.4414861},
  howpublished = {\url{https://github.com/rwightman/pytorch-image-models}}
}
```



## Contact 
Hanene F.Z Brachemi Meftah , `hbrachemi@inttic.dz`

Sid Ahmed Fezza , `sfezza@inttic.dz`

