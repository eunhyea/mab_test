# 📌 우리fis아카데미 3기 2차 기술세미나(우수상)
<br>  

> [발표 PPT(하단 이미지 첨부)](https://www.miricanvas.com/v/13rcy9e) <br>
> [스트림릿 배포 링크](https://eunhyea-mab-test-mab-ls9xri.streamlit.app/)
<br>

# 📌 프레젠테이션 소개 및 요약
#### 프레젠테이션 목적
- **A/B 테스트에 대한 개념과 과정 소개**
  - 실무에서 자주 쓰이지만 정확하게 알지 못해 이를 학습하여 공유하고자 함
- **MAB 알고리즘 소개**
  - AB 테스트의 한계점 보완 및 심화적인 알고리즘 소개 

#### 프레젠테이션 피드백
- 강화학습을 이용한 테스트를 마케팅에서 사용할 수 있도록 고민해 본 것이 신선하다 
- 실제로 테스트 페이지를 만들어서 배포한 것이 좋았다
- Thompson Sampling의 한계점은?
- 카나리 배포 등 무중단 배포과정에서 사용할 수 있으니 실제로 프로젝트에서 진행해봤으면 좋겠다
<br>

# 📌 사용 알고리즘
- MAB(Multi-armed Bandit) | 실시간 최적화를 위한 알고리즘
<br>

# 📌 진행과정 1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟
<br>  

## 1️⃣ AB 테스트 학습
- [Udemy 강의 학습](https://e2.udemymail.com/ls/click?upn=u001.GTBULNEoSOR01el7mORRtIXwBcRzAVCT4CJpW90PbfU5YPqtpHCjQYECHKlzRtFG80ogttnVXdCCqx-2BTUaECDbd2fzMM8OsBYCv4mFY1ZIJkvj-2Fc9ntLRTmjPp-2Ff-2FAW10vxCptx9VsZGKXOeSEAfmUdDbq1umrh5MaDc2j7dZ10IfcB-2BJ2RvPn7Sp-2BBnG37Mk4auf0WVKW1SD6yDuTqER2NngwGRADS0Q5k0g7u96LcRQmbfaQkJASq3GawDVvtZl3aguqHY2CSbWv8kUOtPug-3D-3D1E95_vMh-2BD8PPlbXJMg-2B9M-2F6K2TowAqpetQYnwLUT86Lz5bMg6tGOpqmYighbwVgq0s9BfWYsHhNn8e8HQzwo-2FOIOvnE-2BCRrcU04d9tfxJV-2F7nvZmWlT1ysaaMnqEjJaW9vg19Ijh2DWk6hWrJktzeCZ1DkHU2p3wGDbhe-2B9yYzv6jOto94ZunX-2FDcxJSpgxAflqwTvOWnaAIJLYkU43PMkqcSpwt5klpeUCEvXAOH1k3tj8IwZ8l-2FOKB0gTLPPIkywx6n2y-2BRiQkTPtOau5J8Zk4hWPqTylF9rCgVNYMP4cX3h-2B5O-2BqEHVOHnKl2nyG4EsiCrPIGuRTkAFcCQN8Zdmm5T0cCRaM44y9QGF-2Blj6NemcUf3vfdx9-2Bf1thir3VpeXjr)
<br><br>

## 2️⃣ MAB 알고리즘 학습
- [github 코드](https://github.com/paul-stubley/portfolio/tree/master/multi_armed_bandit)  
- [Chapelle, Olivier, and Lihong Li. “An empirical evaluation of thompson sampling.”, 2011.
](https://proceedings.neurips.cc/paper_files/paper/2011/file/e53a0a2978c28872a4505bdb51db06dc-Paper.pdf)  
- [Komiyama, Junpei, Junya Honda, and Hiroshi Nakagawa. “Optimal regret analysis of thompson sampling in stochastic multi-armed bandit problem with multiple plays.”, 2015.
](https://arxiv.org/abs/1506.00779)  
<br><br>

## 3️⃣ Streamlit 테스트 페이지 배포
|![mab1](https://github.com/user-attachments/assets/2b5d8d0c-fa20-4cf3-959d-6c4869a8af88) | ![image](https://github.com/user-attachments/assets/b8acb724-ebac-41db-80ca-23ed3cea5be8) |
| --- | --- |

## 📌 트러블슈팅
- 이랬는데<br>
  **-> 요래됐슴당**
<br>

## 📌 디벨롭 방향
- 실제 사용자 로그 데이터 수집부터 시작하는 파이프라인 구축하기
- aws 아키텍쳐 위에서 환경 구축하기
- 카나리 배포 과정에서 실제 테스트 진행하기

