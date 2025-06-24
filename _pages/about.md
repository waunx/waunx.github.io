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

**Xu Wan (万旭)** is a second-year PhD student at the College of Control Science and Engineering, Zhejiang University, and currently serves as a visiting student at the [IDEAL Lab](https://www.ideallab-smy.com/) of Peking University under the supervision of [Prof. Mingyang Sun](https://scholar.google.com/citations?user=Vq9aHxoAAAAJ&hl). During his graduate studies, he has gained valuable research experience as a research intern at NetEase Fuxi AI Lab, Ele.me, and Alibaba DAMO Academy, collaborating with [Dr. Yujing Hu](https://scholar.google.com/citations?user=IR5WY-wAAAAJ&hl), [Prof. Wotao Yin](https://scholar.google.com/citations?user=kpQGGFUAAAAJ&hl), and [Cheng Yang](https://scholar.google.com/citations?hl=en&user=5QdPzoAAAAAJ). He is currently a research intern with ByteDance's Seed-Robotic team.

His research interests encompass reinforcement learning, large language models, and large-scale AI applications, with a particular focus on power grid scheduling. He has published several first-author papers at top international AI conferences including ICML, AAAI, and IJCAI, as well as in leading journals such as IEEE Transactions on Power Systems. His work has received recognition in the academic community, as reflected in <a href='https://scholar.google.com/citations?user=NhsHZZwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

Beyond research, he is passionate about fitness and enjoys running and strength training. You can follow his training journey on his [Strava profile](https://www.strava.com/athletes/wan_kris). He is also enthusiastic about trail running and hiking.

# 🔥 News
- *2025.05*: &nbsp;🎉🎉 One paper about elastic cloud service got accepted at **SIGKDD 2025** (co-first author)!
- *2025.05*: &nbsp;🎉🎉 One paper about LLM and RL colloboratation got accepted at **ICML 2025** (first author)!
- *2024.12*: &nbsp;🎉🎉 One paper about multi-agent RL got accepted as an **oral** presentation at **AAAI 2025** (first author)!

# 📝 Selected Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/ACE-Motivation.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making](https://arxiv.org/pdf/2506.02522)

**Xu Wan**, Wenyue Xu, Chao Yang, Mingyang Sun*

- We propose Agents Co-Evolution (ACE), a synergistic framework between LLMs and RL agents for large-scale decision-making scenarios. 
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arxiv</div><img src='images/AdapThink-Framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AdapThink: Adaptive Thinking Preferences for Reasoning Language Model](https://arxiv.org/pdf/2506.18237)

**Xu Wan**, Wei Wang, Wenyue Xu, Wotao Yin, Jie Song, Mingyang Sun*

- We propose AdapThink, an adaptive post-training framework designed
to induce more efficient thinking while maintaining the performance of reasoning language models.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/SrSv-framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SrSv: Integrating Sequential Rollouts with Sequential Value Estimation for Multi-agent Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/download/34500/36655)

**Xu Wan**, Chao Yang, Cheng Yang, Jie Song, Mingyang Sun*

- We propose a novel framework: Sequential rollout with Sequential value estimation (SrSv). This framework aims to capture agent interdependence and provide a scalable solution for cooperative MARL.
</div>
</div>

## Full Publications

<ul class="publication-list">
<li class="publication-item">
<div class="publication-content">
<span class="conference-badge">SIGKDD 2025</span>
<span class="paper-title">IVMR suite: An Industrial-scale Virtual Machine Rescheduling Dataset and Benchmark for Elastic Cloud Service</span>, 
<span class="authors">Yupeng Zhang*, <span class="highlight-author">Xu Wan*</span>, Xiangyun Kong*, Chao Yang, Binda Ma, Wotao Yin, Jian Zhou</span>
</div>
</li>

<li class="publication-item">
<div class="publication-content">
<span class="conference-badge">ICML 2025</span>
<a href="https://arxiv.org/pdf/2506.02522" class="paper-title">Think Twice, Act Once: A Co-Evolution Framework of LLM and RL for Large-Scale Decision Making</a>, 
<span class="authors"><span class="highlight-author">Xu Wan</span>, Wenyue Xu, Chao Yang, Mingyang Sun</span>
</div>
</li>

<li class="publication-item">
<div class="publication-content">
<span class="conference-badge">AAAI 2025</span>
<a href="https://ojs.aaai.org/index.php/AAAI/article/download/34500/36655" class="paper-title">SrSv: Integrating Sequential Rollouts with Sequential Value Estimation for Multi-agent Reinforcement Learning</a>, 
<span class="authors"><span class="highlight-author">Xu Wan</span>, Wenyue Xu, Chao Yang, Mingyang Sun</span>
</div>
</li>

<li class="publication-item">
<div class="publication-content">
<span class="conference-badge">IEEE Trans. Power System</span>
<a href="https://ieeexplore.ieee.org/abstract/document/10726595/" class="paper-title">AdapSafe2: Prior-Free Safe-Certified Reinforcement Learning for Multi-Area Frequency Control</a>, 
<span class="authors"><span class="highlight-author">Xu Wan</span>, Mingyang Sun</span>
</div>
</li>

<li class="publication-item">
<div class="publication-content">
<span class="conference-badge">Energy Convers. Econ</span>
<a href="https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/enc2.12086" class="paper-title">Highly Transferable Adversarial Attack Against Deep-Reinforcement-Learning-Based Frequency Control</a>, 
<span class="authors">Zhongwei Li, Yang Liu, Peng Qiu, Hongyan Yin, <span class="highlight-author">Xu Wan</span> (Corresponding Author), Mingyang Sun</span>
</div>
</li>

<li class="publication-item">
<div class="publication-content">
<span class="conference-badge">AAAI 2023</span>
<a href="https://ojs.aaai.org/index.php/AAAI/article/view/25660" class="paper-title">AdapSafe: Adaptive and Safe-Certified Deep Reinforcement Learning-Based Frequency Control for Carbon-neutral Power Systems</a>, 
<span class="authors"><span class="highlight-author">Xu Wan</span>, Mingyang Sun, Boli Chen, Zhongda Chu, Fei Teng</span>
</div>
</li>

<li class="publication-item">
<div class="publication-content">
<span class="conference-badge">IEEE Trans. Power System</span>
<span class="paper-title">Physics-Constrained Vulnerability Assessment of Deep Reinforcement Learning-Based SCOPF</span>, 
<span class="authors">Lanting Zen, Mingyang Sun, <span class="highlight-author">Xu Wan</span>, Zhenyong Zhang, Ruilong Deng, Yan Xu</span>
</div>
</li>

<li class="publication-item">
<div class="publication-content">
<span class="conference-badge">IJCAI 2022</span>
<a href="https://www.ijcai.org/proceedings/2022/0549.pdf" class="paper-title">Exploring the Vulnerability of Deep Reinforcement Learning-based Emergency Control for Low Carbon Power Systems</a>, 
<span class="authors"><span class="highlight-author">Xu Wan</span>, Lanting Zen, Mingyang Sun</span>
</div>
</li>
</ul>
