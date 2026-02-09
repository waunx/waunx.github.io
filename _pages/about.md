---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hi, I am **Xu Wan (万旭)**, a third-year PhD student at the College of Control Science and Engineering, Zhejiang University, and currently serves as a visiting student at the [IDEAL Lab](https://www.ideallab-smy.com/) of Peking University under the supervision of [Prof. Mingyang Sun](https://scholar.google.com/citations?user=Vq9aHxoAAAAJ&hl). During my graduate studies, I have gained valuable research experience as a research intern at ByteDance Seed Robotics Team, Alibaba DAMO Academy, and NetEase Fuxi AI Lab, collaborating with  [Prof. Wotao Yin](https://scholar.google.com/citations?user=kpQGGFUAAAAJ&hl), [Dr. Yansheng Wang](https://scholar.google.com/citations?user=h6ryv2oAAAAJ&hl), and [Dr. Yujing Hu](https://scholar.google.com/citations?user=IR5WY-wAAAAJ&hl). I am currently an intern with Tecent Hunyuan team.

My research interests include large language models (LLMs), reinforcement learning (RL), and large-scale AI applications, with a special focus on LLM post-training. I’ve published several first-author papers at international AI conferences like NeurIPS, ICML, ICLR, KDD, and AAAI, as well as in journals such as IEEE Transactions on Power Systems with google citations <a href='https://scholar.google.com/citations?user=NhsHZZwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

Beyond research, I am passionate about fitness and enjoys running and strength training. You can follow my training journey on my [Strava profile](https://www.strava.com/athletes/wan_kris). I am also enthusiastic about trail running and hiking.

# 🔥 News
- *2026.01*: &nbsp;🎉🎉 One paper about LLM RL got accepted at **ICLR 2026** (first author)!
- *2025.09*: &nbsp;🎉🎉 One paper about robust safe RL got accepted at **NeurIPS 2025** (first author)!
- *2025.07*: &nbsp;🎉🎉 <span style="color:#ff6666">I was supported by the **CIE-Tencent Doctoral Research Incentive Project** (with **only 23** recipients nationwide and a research fund of **100,000 RMB**)!</span>
- *2025.05*: &nbsp;🎉🎉 One paper about elastic cloud service got accepted at **SIGKDD 2025** (co-first author)!
- *2025.05*: &nbsp;🎉🎉 One paper about LLM and RL colloboratation got accepted at **ICML 2025** (first author)!
- *2024.12*: &nbsp;🎉🎉 One paper about multi-agent RL got accepted as an <span style="color:#ff6666">**oral**</span> presentation at **AAAI 2025** (first author)!

# 📝 Publications 

## 🍾 Spotlight Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/BAPO_framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Buffer Matters: Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning](https://iclr.cc/virtual/2026/poster/10009473)

**Xu Wan**, Chao Yang,  Yansheng Wang, Wenqi Huang, Mingyang Sun

- BAPO is an off-policy RLVR framework to improve the data efficiency in large language models post-training.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arxiv</div><img src='images/AdapThink-Framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AdapThink: Adaptive Thinking Preferences for Reasoning Language Model](https://arxiv.org/abs/2506.18237)

**Xu Wan**, Wei Wang, Wenyue Xu, Wotao Yin, Jie Song, Mingyang Sun

- AdapThink is an adaptive length penalty method for efficient thinking of reasoning language models.
</div>
</div>

	
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arxiv</div><img src='images/ProOPF_framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ProOPF: Benchmarking and Improving LLMs for Professional-Grade Power Systems Optimization Modeling](https://www.arxiv.org/abs/2602.03070)

Chao Shen, Zihan Guo, **Xu Wan*(co-first author)**, Zhenghao Yang, Yifan Zhang, Wengi Huang, Jie Song, Zongyan Zhang, Mingyang Sun

- ProOPF introduces a 12K-instance dataset and a 121-case expert benchmark for evaluating and improving LLMs on professional-grade optimal power flow modeling from natural language.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">under review</div><img src='images/DABA_res.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation for LLMs.

**Xu Wan**, SpeedZhu, Jiawei Cai, Guang Chen, Ximing Huang, Wiggin Zhou, Mingyang Sun

-  DABA implements a Lambert W policy to execute strategic abandonment, sacrificing insolvent tasks to redistribute critical computational resources to solvable complex queries.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/ACE-Motivation.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making](https://arxiv.org/pdf/2506.02522)

**Xu Wan**, Wenyue Xu, Chao Yang, Mingyang Sun

- Agents Co-Evolution (ACE) is a synergistic framework between LLMs and RL agents for large-scale decision-making scenarios. 
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/Fuz-res.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Fuz-RL: A Fuzzy-Guided Robust Framework for Safe Reinforcement Learning under Uncertainty](https://openreview.net/forum?id=SuewCbLYBS&referrer=%5BAuthor%20Console%5D)

**Xu Wan**, Chao Yang, Cheng Yang, Jie Song, Mingyang Sun

- Fuz-RL is a novel fuzzy-guided robust framework for safe RL.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/SrSv-framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SrSv: Integrating Sequential Rollouts with Sequential Value Estimation for Multi-agent Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/download/34500/36655)

**Xu Wan**, Chao Yang, Cheng Yang, Jie Song, Mingyang Sun

- SrSv aims to capture agent interdependence and provide a scalable solution for cooperative MARL.
</div>
</div>

## 📖 Full Publications

\* denotes co-first authors, \# denotes corresponding author.

### Under Review

<ul>

  <li>The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation for LLMs, <strong>Xu Wan*</strong>, SpeedZhu*, Jiawei Cai, Guang Chen, Ximing Huang, Wiggin Zhou, Mingyang Sun,<strong>Under Review</strong></li>


  <li><a href="https://arxiv.org/abs/2506.18237">ProOPF: Benchmarking and Improving LLMs for Professional-Grade Power Systems Optimization Modeling</a>, Chao Shen*, Zihan Guo*, <strong>Xu Wan*</strong>, Zhenghao Yang, Yifan Zhang, Wengi Huang, Jie Song, Zongyan Zhang, Mingyang Sun, <strong>Under Review</strong></li>

  <li><a href="https://arxiv.org/abs/2506.18237">AdapThink: Adaptive Thinking Preferences for Reasoning Language Model</a>, <strong>Xu Wan</strong>, Wei Wang, Wenyue Xu, Wotao Yin, Jie Song, Mingyang Sun, <strong>Under Review</strong></li>

  <li><a href="https://arxiv.org/abs/2410.18626">SAMG: Offline-to-Online Reinforcement Learning via State-Action-Conditional Offline Model Guidance</a>, Liyu Zhang, <strong>Xu Wan</strong>, Haochi Wu, Quan Kong, Ruilong Deng, Mingyang Sun, <strong>Under Review</strong></li>
</ul>


### 2026
<ul>
   <li><a href="https://iclr.cc/virtual/2026/poster/10009473"> Buffer Matters, Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning</a>, <strong>Xu Wan</strong>, Yansheng Wang, Wenqi Huang, Mingyang Sun, <strong> ICLR 2026</strong></li>
</ul>

### 2025 
<ul>

  <li><a href="https://openreview.net/forum?id=SuewCbLYBS&referrer=%5BAuthor%20Console%5D"> Fuz-RL: A Fuzzy-Guided Robust Framework for Safe Reinforcement Learning under Uncertainty</a>, <strong>Xu Wan</strong>, Chao Yang, Cheng Yang, Jie Song, Mingyang Sun, <strong>NeurIPS 2025</strong> <a href="https://github.com/waunx/FuzRL">[Code]</a></li>

  <li><a href="https://dl.acm.org/doi/10.1145/3711896.3737381">IVMR suite: An Industrial-scale Virtual Machine Rescheduling Dataset and Benchmark for Elastic Cloud Service</a>, Yupeng Zhang*, <strong>Xu Wan*</strong>, Xiangyun Kong*, Chao Yang, Binda Ma, Wotao Yin, Jian Zhou, <strong>SIGKDD 2025</strong> <a href="https://github.com/MDrW/IVMRSuite-KDD">[Code]</a> </li>
  
  <li><a href="https://arxiv.org/pdf/2506.02522">Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making</a>, <strong>Xu Wan</strong>, Wenyue Xu, Chao Yang, Mingyang Sun, <strong>ICML 2025</strong></li>
</ul>

### 2024
<ul>
  <li><a href="https://arxiv.org/abs/2503.01458">SrSv: Integrating Sequential Rollouts with Sequential Value Estimation for Multi-agent Reinforcement Learning</a>, <strong>Xu Wan</strong>, Wenyue Xu, Chao Yang, Mingyang Sun, <strong>AAAI 2025 (Oral)</strong> <a href="https://github.com/waunx/SrSv">[Code]</a></li>
  
  <li><a href="https://ieeexplore.ieee.org/abstract/document/10726595/">AdapSafe2: Prior-Free Safe-Certified Reinforcement Learning for Multi-Area Frequency Control</a>, <strong>Xu Wan</strong>, Mingyang Sun, <strong>IEEE Trans. Power System</strong></li>
</ul>

### 2023
<ul>
  <li><a href="https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/enc2.12086">Highly Transferable Adversarial Attack Against Deep-Reinforcement-Learning-Based Frequency Control</a>, Zhongwei Li, Yang Liu, Peng Qiu, Hongyan Yin, <strong>Xu Wan #</strong>, Mingyang Sun, <strong>Energy Convers. Econ</strong></li>
  
  <li><a href="https://ojs.aaai.org/index.php/AAAI/article/view/25660">AdapSafe: Adaptive and Safe-Certified Deep Reinforcement Learning-Based Frequency Control for Carbon-neutral Power Systems</a>, <strong>Xu Wan</strong>, Mingyang Sun, Boli Chen, Zhongda Chu, Fei Teng, <strong>AAAI 2023</strong> <a href="https://github.com/waunx/AdapSafe">[Code]</a> </li>
</ul>

### 2022 and Prior
<ul>
  <li><a href="https://ieeexplore.ieee.org/abstract/document/9834132">Physics-Constrained Vulnerability Assessment of Deep Reinforcement Learning-Based SCOPF</a>, Lanting Zen, Mingyang Sun, <strong>Xu Wan</strong>, Zhenyong Zhang, Ruilong Deng, Yan Xu, <strong>IEEE Trans. Power System</strong></li>
  
  <li><a href="https://www.ijcai.org/proceedings/2022/0549.pdf">Exploring the Vulnerability of Deep Reinforcement Learning-based Emergency Control for Low Carbon Power Systems</a>, <strong>Xu Wan</strong>, Lanting Zen, Mingyang Sun, <strong>IJCAI 2022</strong> <a href="https://github.com/waunx/RT-Attack-DB-Defense">[Code]</a> </li>
</ul>


# 🎖 Honors and Awards

- *2022.11*: **First Prize** in the 4th China Graduate Student Artificial Intelligence Innovation Competition (Huawei Cup), **Top 6 Nationally**
- *2022.08*: **First Prize** in the 3rd National College Student Mathematical Modeling Competition (Huashu Cup), **Top 5% Nationally**
- *2020.04*: **First Prize** in American Mathematical Contest in Modeling (MCM), **Top 7.4% Globally**
- *2022.10*: **Second Prize** in Baidu PaddlePaddle China University Computer Competition, **Top 8 Nationally**  
- *2022.05*: **Second Prize** in MathorCup College Student Mathematical Modeling Challenge, **Top 15% Nationally**
- *2021.11*: **Second Prize** in the 19th China Graduate Student Mathematical Modeling Competition, **Top 15% Nationally**


# 👨‍💼 Services 

- Reviewer for ICML 2026

- Reviewer for ICLR 2026

- Reviewer for NeurIPS 2025

- Reviewer for TPWRS (Transactions on Power System)

- Program Committee for AAAI 2026 (Main Track and AIA track)

<!-- # 📖 Educations -->

<!-- - *2024.03 - Present*, **Ph.D. Student in Control Science and Engineering**, Zhejiang University, Hangzhou, China. 
  - [IDEAL Lab](https://www.ideallab-smy.com/), supervised by [Prof. Mingyang Sun](https://scholar.google.com/citations?user=Vq9aHxoAAAAJ)
  - Visiting student at Peking University (2024-Present)

- *2021.09 - 2024.03*, **M.S. in Control Science and Engineering**, Zhejiang University, Hangzhou, China.
  - [NeSC Lab](http://nesc.zju.edu.cn/#/), supervised by [Prof. Mingyang Sun](https://scholar.google.com/citations?user=Vq9aHxoAAAAJ) and [Prof. Jiming Chen](https://scholar.google.com/citations?user=zK9tvo8AAAAJ)
  - GPA: 1/60, **National Scholarship**, Outstanding Graduate Student

- *2017.09 - 2021.06*, **B.S. in Automation**, China University of Geosciences (Wuhan), Wuhan, China.
  - Intelligent Systems Research Institute, supervised by [Prof. Changhe Li](https://scholar.google.com/citations?user=MmLvGr0AAAAJ)
  - GPA: 2/182, **National Scholarship**, Outstanding Graduate -->
