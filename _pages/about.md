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

<h1 class="section-title"><i class="fas fa-user" aria-hidden="true"></i> About Me</h1>

<!-- Hi, I am **Xu Wan (万旭)**, a PhD 毕业自 the College of Control Science and Engineering, Zhejiang University, and currently serves as a visiting student at the [IDEAL Lab](https://www.ideallab-smy.com/) of Peking University under the supervision of [Prof. Mingyang Sun](https://scholar.google.com/citations?user=Vq9aHxoAAAAJ&hl). During my graduate studies, I have gained valuable research experience as a research intern at Tecent Hunyuan team， ByteDance Seed Robotics Team, Alibaba DAMO Academy, and NetEase Fuxi AI Lab, collaborating with  [Prof. Wotao Yin](https://scholar.google.com/citations?user=kpQGGFUAAAAJ&hl), [Dr. Yansheng Wang](https://scholar.google.com/citations?user=h6ryv2oAAAAJ&hl), and [Dr. Yujing Hu](https://scholar.google.com/citations?user=IR5WY-wAAAAJ&hl). I am currently an intern with ByteDance Seed Robotics Team. -->

<div class="intro-panel" markdown="1">

Hi, I am **Xu Wan (万旭)**. I am currently a researcher in the ByteDance Seed Team. I received my Ph.D. from the College of Control Science and Engineering at [Zhejiang University](https://www.zju.edu.cn/) in June 2026. I was previously a visiting student at the [IDEAL Lab](https://www.ideallab-smy.com/), Peking University, advised by [Prof. Mingyang Sun](https://scholar.google.com/citations?user=Vq9aHxoAAAAJ&hl). During my Ph.D., I interned at Tencent Hunyuan, ByteDance Seed, Alibaba DAMO Academy, and NetEase Fuxi AI Lab, and had the pleasure of collaborating with [Prof. Wotao Yin](https://scholar.google.com/citations?user=kpQGGFUAAAAJ&hl), Dr. Speed Zhu, [Dr. Sheng Chen](https://scholar.google.com/citations?user=i1lEbzQAAAAJ&hl=en), [Dr. Yujing Hu](https://scholar.google.com/citations?user=IR5WY-wAAAAJ&hl), and many other outstanding researchers.

<div class="opportunity-callout">
  I am actively seeking <span class="primary-gradient-text">academic collaborations</span>. Please feel free to <a class="primary-gradient-text opportunity-callout__email" href="mailto:{{ site.author.email }}">reach out via email</a>.
</div>

<div class="research-vision" markdown="1">

<span class="research-kicker">Research vision</span>

## Learning in Constraint Spaces

My research asks a central question: **how can intelligent systems learn to reason and act when computation, feedback, and physical rules are limited?** I view constraints not merely as obstacles, but as useful structure for building intelligence that is more efficient, reliable, and deployable.

</div>

{% include research-constraint-map.html %}

Together, these threads explore how limited resources and hard rules can become **design signals for better intelligence**.

Beyond research, I am passionate about fitness and enjoy running and strength training. You can follow my training journey on my [Strava profile](https://www.strava.com/athletes/wan_kris). I am also enthusiastic about trail running and hiking.

{% include strava-heatmap.html %}

</div>

<span class='anchor' id='news'></span>

<h1 class="section-title"><i class="fas fa-fire" aria-hidden="true"></i> News</h1>

<div class="news-list" markdown="1">

- *2026.05*: &nbsp;🎉🎉 Three papers about LLM Token Allocation / LLM for Optimization / T2I RL post-train got accepted at **ICML 2026**!
- *2026.03*: &nbsp;🎉🎉 One paper about Length Penalty of LLM got accepted at **ACL 2026**!
- *2026.01*: &nbsp;🎉🎉 One paper about Off-policy LLM-RL post-train got accepted at **ICLR 2026** (first author)!
- *2025.09*: &nbsp;🎉🎉 One paper about robust safe RL got accepted at **NeurIPS 2025** (first author)!
- *2025.07*: &nbsp;🎉🎉 <span style="color:#ff6666">I was supported by the **CIE-Tencent Doctoral Research Incentive Project** (with **only 23** recipients nationwide and a research fund of **100,000 RMB**)!</span>
- *2025.05*: &nbsp;🎉🎉 One paper about elastic cloud service got accepted at **SIGKDD 2025** (co-first author)!
- *2025.05*: &nbsp;🎉🎉 One paper about LLM and RL colloboratation got accepted at **ICML 2025** (first author)!
- *2024.12*: &nbsp;🎉🎉 One paper about multi-agent RL got accepted as an <span style="color:#ff6666">**oral**</span> presentation at **AAAI 2025** (first author)!

</div>

<span class='anchor' id='publications'></span>

<h1 class="section-title"><i class="fas fa-book-open" aria-hidden="true"></i> Publications</h1>

## Spotlight Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/BAPO_framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Buffer Matters: Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning](https://arxiv.org/abs/2602.20722) <a href="https://github.com/waunx/BAPO_ICLRL">[Code]</a>

**Xu Wan**, Yansheng Wang, Wenqi Huang, Mingyang Sun

- BAPO is an off-policy RLVR framework to improve the data efficiency in large language models post-training.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2026</div><img src='images/CLEAR_motivation.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation for LLMs](https://arxiv.org/abs/2606.03092) <a href="https://github.com/waunx/CLEAR">[Code]</a>

**Xu Wan**, SpeedZhu, Jiawei Cai, Guang Chen, Ximing Huang, Wiggin Zhou, Mingyang Sun

-  CLEAR implements a Lambert W policy to execute strategic abandonment, sacrificing insolvent tasks to redistribute critical computational resources to solvable complex queries.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/AdapThink-Framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AdapThink: Adaptive Thinking Preferences for Reasoning Language Model](https://arxiv.org/abs/2506.18237) <a href="https://github.com/waunx/AdapThink">[Code]</a>

Wenyue Xu*, **Xu Wan*(co-first author)**, Wei Wang, Wotao Yin, Wenqi Huang, Shengjie Zhao, Mingyang Sun

- AdapThink is an adaptive length penalty method for efficient thinking of reasoning language models.
</div>
</div>

	
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2026</div><img src='images/ProOPF_framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ProOPF: Benchmarking and Improving LLMs for Professional-Grade Power Systems Optimization Modeling](https://www.arxiv.org/abs/2602.03070) <a href="https://github.com/shenchao188/ProOPF-Benchamrk-Dataset">[Code]</a>

Chao Shen*, Zihan Guo*, **Xu Wan*(co-first author)**, Zhenghao Yang, Yifan Zhang, Wengi Huang, Jie Song, Zongyan Zhang, Mingyang Sun

- ProOPF introduces a 12K-instance dataset and a 121-case expert benchmark for evaluating and improving LLMs on professional-grade optimal power flow modeling from natural language.
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

[Fuz-RL: A Fuzzy-Guided Robust Framework for Safe Reinforcement Learning under Uncertainty](https://arxiv.org/abs/2602.20729) <a href="https://github.com/waunx/FuzRL">[Code]</a>

**Xu Wan**, Chao Yang, Cheng Yang, Jie Song, Mingyang Sun

- Fuz-RL is a novel fuzzy-guided robust framework for safe RL.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/SrSv-framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SrSv: Integrating Sequential Rollouts with Sequential Value Estimation for Multi-agent Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/download/34500/36655) <a href="https://github.com/waunx/SrSv">[Code]</a>

**Xu Wan**, Chao Yang, Cheng Yang, Jie Song, Mingyang Sun

- SrSv aims to capture agent interdependence and provide a scalable solution for cooperative MARL.
</div>
</div>

## Full Publications

\* denotes co-first authors, \# denotes corresponding author.

### Under Review

<ul>
  <li><a href="https://arxiv.org/abs/2410.18626">SAMG: Offline-to-Online Reinforcement Learning via State-Action-Conditional Offline Model Guidance</a>, Liyu Zhang, <strong>Xu Wan</strong>, Haochi Wu, Quan Kong, Ruilong Deng, Mingyang Sun, <strong>Under Review</strong></li>
</ul>


### 2026
<ul>
  <li><a href="https://arxiv.org/abs/2606.03092">The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation for LLMs</a>, <strong>Xu Wan*</strong>, SpeedZhu*, Jiawei Cai, Guang Chen, Ximing Huang, Wiggin Zhou, Mingyang Sun,<strong>ICML 2026</strong> <a href="https://github.com/waunx/CLEAR">[Code]</a> </li>

  <li><a href="https://arxiv.org/abs/2506.18237">ProOPF: Benchmarking and Improving LLMs for Professional-Grade Power Systems Optimization Modeling</a>, Chao Shen*, Zihan Guo*, <strong>Xu Wan*</strong>, Zhenghao Yang, Yifan Zhang, Wengi Huang, Jie Song, Zongyan Zhang, Mingyang Sun, <strong>ICML 2026</strong> <a href="https://github.com/shenchao188/ProOPF-Benchamrk-Dataset">[Code]</a> </li>

  <li><a href="https://arxiv.org/abs/2510.21583">Principled RL for Flow Matching Emerges From the Chunk-level Policy Optimization</a>, Yifu Luo, Haoyuan Sun, Xinhao Hu, <strong>Xu Wan</strong>, et.al, <strong>ICML 2026</strong> <a href="https://github.com/xingzhejun/GCPO">[Code]</a> </li>

  <li><a href="https://arxiv.org/abs/2506.18237">AdapThink: Adaptive Thinking Preferences for Reasoning Language Model</a>, Wenyue Xu, <strong>Xu Wan</strong>, Wei Wang,  Wotao Yin, Wenqi Huang, Shengjie Zhao, Mingyang Sun, <strong>ACL 2026 (Findings)</strong> <a href="https://github.com/waunx/AdapThink">[Code]</a> </li>

   <li><a href="https://arxiv.org/abs/2602.20722"> Buffer Matters, Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning</a>, <strong>Xu Wan</strong>, Yansheng Wang, Wenqi Huang, Mingyang Sun, <strong> ICLR 2026</strong> <a href="https://github.com/waunx/BAPO_ICLR">[Code]</a> </li>
</ul>

### 2025 
<ul>

  <li><a href="https://arxiv.org/abs/2602.20729"> Fuz-RL: A Fuzzy-Guided Robust Framework for Safe Reinforcement Learning under Uncertainty</a>, <strong>Xu Wan</strong>, Chao Yang, Cheng Yang, Jie Song, Mingyang Sun, <strong>NeurIPS 2025</strong> <a href="https://github.com/waunx/FuzRL">[Code]</a></li>

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


<span class='anchor' id='honors-and-awards'></span>

<h1 class="section-title"><i class="fas fa-award" aria-hidden="true"></i> Honors and Awards</h1>

<div class="award-list" markdown="1">

- *2026.06*: **Sun Youxian Academician Scholarship (孙优贤院士奖学金)**, awarded to only **5 Ph.D. students university-wide**, with a **RMB 30,000** scholarship
- *2025.07*: Named a **Hunyuan Scholar (混元学者)**, with **RMB 100,000** in project funding
- *2023.10*: **China Optics Valley Scholarship (中国光谷奖学金)**, with a **RMB 10,000** scholarship
- *2022.11*: **First Prize** in the 4th China Graduate Student Artificial Intelligence Innovation Competition (Huawei Cup), **Top 6 Nationally**, with a **RMB 30,000** cash award
- *2022.10*: **Second Prize** in Baidu PaddlePaddle China University Computer Competition, **Top 8 Nationally**, with a **RMB 10,000** cash award
- *2022.10*: **National Scholarship for Graduate Students**
- *2022.08*: **First Prize** in the 3rd National College Student Mathematical Modeling Competition (Huashu Cup), **Top 5% Nationally**
- *2020.04*: **First Prize** in American Mathematical Contest in Modeling (MCM), **Top 7.4% Globally**
- *2019.10*: **National Scholarship for Undergraduate Students**

</div>

<span class='anchor' id='services'></span>

<h1 class="section-title"><i class="fas fa-users" aria-hidden="true"></i> Services</h1>

<div class="service-list" markdown="1">

- Reviewer for ICML 2026

- Reviewer for ICLR 2026

- Reviewer for NeurIPS 2025

- Reviewer for TPWRS (Transactions on Power System)

- Program Committee for AAAI 2026 (Main Track and AIA track)

</div>

<span class='anchor' id='visitors'></span>

<h1 class="section-title"><i class="fas fa-globe-asia" aria-hidden="true"></i> Visitors</h1>

<div class="visitor-map">
  <a href="https://info.flagcounter.com/VyP7" target="_blank" rel="noopener noreferrer" aria-label="View detailed visitor statistics by country">
    <img src="https://s01.flagcounter.com/map/VyP7/size_s/txt_012F63/border_E2E8F0/pageviews_1/viewers_0/flags_0/" alt="Visitor map with total page views and countries" border="0">
  </a>
  <p>Visitors by country · total page views · since July 20, 2026</p>
</div>

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
