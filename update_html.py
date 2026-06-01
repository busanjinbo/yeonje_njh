import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title and Meta
html = html.replace('<title>일하는 구청장 연제사람 노정현</title>', '<title>진보구의원 후보 이정은</title>')
html = html.replace('content="진보당 노정현 연제구청장 후보 홈페이지 - 일하는 구청장, 연제사람 노정현의 공약과 약력을 확인하세요."', 'content="진보당 이정은 연제구의원 후보 홈페이지 - 언제나 주민 곁에 일하는 사람 이정은"')
html = html.replace('content="일하는 구청장 연제사람 노정현"', 'content="진보구의원 후보 이정은"')
html = html.replace('content="진보당 노정현 연제구청장 후보 홈페이지"', 'content="진보당 이정은 연제구의원 후보 홈페이지"')

# 2. Update Quick Menu
quick_menu_old = """                <div class="quick-menu-group" id="quick-pledge-group">
                    <button class="quick-menu-btn" id="quick-pledge-btn" style="padding-bottom: 0.5rem; gap: 0.15rem;">
                        <div style="display: flex; align-items: center; justify-content: center; height: 1.2rem;">
                            <i class="fas fa-bullhorn" style="font-size: 1.15rem;"></i>
                        </div>
                        <span>공약</span>
                        <i class="fas fa-chevron-left" style="font-size: 0.6rem; color: #94a3b8; margin-top: 0.15rem;"></i>
                    </button>
                    <div class="quick-sub">
                        <div class="quick-sub-btn nav-link" data-target="view-pledge4">좋은 일자리</div>
                        <div class="quick-sub-btn nav-link" data-target="view-pledge5">살고싶은 도시</div>
                        <div class="quick-sub-btn nav-link" data-target="view-pledge1">동백배달</div>
                        <div class="quick-sub-btn nav-link" data-target="view-pledge2">공공은행</div>
                        <div class="quick-sub-btn nav-link" data-target="view-pledge3">스쿨버스</div>
                    </div>
                </div>"""
quick_menu_new = """                <button class="quick-menu-btn nav-link" data-target="view-pledge">
                    <i class="fas fa-bullhorn"></i>
                    <span>공약</span>
                </button>"""
html = html.replace(quick_menu_old, quick_menu_new)

# 3. Update Top Nav
top_nav_old = """                    <div class="nav-dropdown">
                        <span class="nav-link nav-dropdown-toggle">공약 <i class="fas fa-chevron-down nav-dropdown-icon"></i></span>
                        <div class="nav-dropdown-content">
                            <a href="#" data-target="view-pledge4" class="nav-link">좋은 일자리</a>
                            <a href="#" data-target="view-pledge5" class="nav-link">살고싶은 도시 연제구</a>
                            <a href="#" data-target="view-pledge1" class="nav-link">공공배달앱</a>
                            <a href="#" data-target="view-pledge2" class="nav-link">공공은행</a>
                            <a href="#" data-target="view-pledge3" class="nav-link">워킹스쿨버스</a>
                        </div>
                    </div>"""
top_nav_new = """                    <a href="#" data-target="view-pledge" class="nav-link">이정은의 수첩</a>"""
html = html.replace(top_nav_old, top_nav_new)

# update names in nav
html = html.replace('alt="일하는 구청장"', 'alt="진보구의원 후보"')
html = html.replace('일하는 구청장</text>', '진보구의원 후보</text>')
html = html.replace('<span class="nav-candidate-name">노정현</span>', '<span class="nav-candidate-name">이정은</span>')

# 4. Hero Section updates
html = html.replace('alt="노정현 후보"', 'alt="이정은 후보"')
html = html.replace('alt="노정현"', 'alt="이정은"')
html = html.replace('노정현의 힘이 되어주십시오.', '오직, 주민에게만 빚지고 싶습니다.')
html = html.replace('113-2020-3080-07', '101-2095-7369-08')
html = html.replace('예금주 : 노정현후원회(연제구청장선거)', '예금주 : 이정은(연제구의원선거)')
html = html.replace('010-5840-3422', '010-9476-6924')
html = html.replace('노정현을<br>소개합니다', '이정은을<br>소개합니다')

# 5. Home Pledge section replace
home_pledge_match = re.search(r'<!-- Core Pledges Section.*?</div> <!-- End of home-pledge-section -->', html, re.DOTALL)
if home_pledge_match:
    home_pledge_new = """            <!-- Core Pledges Section (Sky Blue Background) -->
            <div class="home-pledge-section">
                <!-- Core Pledges Title -->
                <div class="home-pledge-header reveal">
                    <h2 class="home-pledge-title">이정은의 수첩</h2>
                </div>
                
                <!-- Core Pledges List (Cards) -->
                <div class="hero-pledge-list">
                    <a href="#" data-target="view-pledge" class="hz-pledge-card hero-pledge-item reveal">
                        <div class="hz-pledge-text" style="padding-left: 1.5rem;">
                            <span class="pledge-name" style="font-size: 1.1rem;"><span style="color:#0284c7; font-weight:900; margin-right:0.5rem;">1</span>돌봄 1번지 연제</span>
                            <i class="fas fa-chevron-right pledge-arrow"></i>
                        </div>
                    </a>
                    <a href="#" data-target="view-pledge" class="hz-pledge-card hero-pledge-item reveal">
                        <div class="hz-pledge-text" style="padding-left: 1.5rem;">
                            <span class="pledge-name" style="font-size: 1.1rem;"><span style="color:#e11d48; font-weight:900; margin-right:0.5rem;">2</span>안전/생활 강화</span>
                            <i class="fas fa-chevron-right pledge-arrow"></i>
                        </div>
                    </a>
                    <a href="#" data-target="view-pledge" class="hz-pledge-card hero-pledge-item reveal">
                        <div class="hz-pledge-text" style="padding-left: 1.5rem;">
                            <span class="pledge-name" style="font-size: 1.1rem;"><span style="color:#0284c7; font-weight:900; margin-right:0.5rem;">3</span>골목상권·시장 살리기</span>
                            <i class="fas fa-chevron-right pledge-arrow"></i>
                        </div>
                    </a>
                    <a href="#" data-target="view-pledge" class="hz-pledge-card hero-pledge-item reveal">
                        <div class="hz-pledge-text" style="padding-left: 1.5rem;">
                            <span class="pledge-name" style="font-size: 1.1rem;"><span style="color:#e11d48; font-weight:900; margin-right:0.5rem;">4</span>주차·교통 불편 해결</span>
                            <i class="fas fa-chevron-right pledge-arrow"></i>
                        </div>
                    </a>
                    <a href="#" data-target="view-pledge" class="hz-pledge-card hero-pledge-item reveal">
                        <div class="hz-pledge-text" style="padding-left: 1.5rem;">
                            <span class="pledge-name" style="font-size: 1.1rem;"><span style="color:#0284c7; font-weight:900; margin-right:0.5rem;">5</span>침수·하수·안전 대책</span>
                            <i class="fas fa-chevron-right pledge-arrow"></i>
                        </div>
                    </a>
                    <a href="#" data-target="view-pledge" class="hz-pledge-card hero-pledge-item reveal">
                        <div class="hz-pledge-text" style="padding-left: 1.5rem;">
                            <span class="pledge-name" style="font-size: 1.1rem;"><span style="color:#e11d48; font-weight:900; margin-right:0.5rem;">6</span>주민결정 정치제도화</span>
                            <i class="fas fa-chevron-right pledge-arrow"></i>
                        </div>
                    </a>
                </div>
            </div> <!-- End of home-pledge-section -->"""
    html = html.replace(home_pledge_match.group(0), home_pledge_new)

# 6. About Section Rewrite
about_match = re.search(r'<section class="section about-section".*?</section>', html, re.DOTALL)
if about_match:
    about_new = """<section class="section about-section" style="padding-top: 0; background-color: #f8fafc;">
                <div class="about-content-container reveal" style="max-width: 900px; margin: 0 auto; padding: 2rem 1.5rem 3rem 1.5rem;">
                    
                    <!-- 1. 이정은의 삶은 봉사입니다 -->
                    <div class="bio-section-designed reveal" style="background: white; border-radius: 16px; padding: 2.5rem 1.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 3rem;">
                        <div class="bio-header-container" style="text-align: center; margin-bottom: 2rem;">
                            <h2 class="bio-main-title" style="font-size: 2.2rem; color: #1e293b; font-weight: 900; margin-bottom: 1rem;"><span style="color: #0284c7;">이정은</span>의 삶은<br>봉사입니다</h2>
                        </div>
                        
                        <div class="bio-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
                            <!-- Column 1 -->
                            <div class="bio-col" style="background: #f1f5f9; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #0ea5e9;">
                                <h3 style="color: #0284c7; font-size: 1.15rem; font-weight: 800; margin-bottom: 1rem;">학교 현장과 함께한<br>교육 정책 전문가</h3>
                                <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.95rem; color: #334155; line-height: 1.5;">
                                    <li style="margin-bottom: 0.5rem;">· 전) 부산교육감직 인수위원회 자문위원</li>
                                    <li style="margin-bottom: 0.5rem;">· 전) 부산교육청 시민교육협의회 자문위원</li>
                                    <li style="margin-bottom: 0.5rem;">· 전) 부산교육청 인성교육진흥협의회 위원</li>
                                    <li style="margin-bottom: 0.5rem;">· 전) 부산교육청 혁신학교 추진위원 및 신설 심사위원</li>
                                    <li style="margin-bottom: 0.5rem;">· 신) 부산다행복학교 추진위원회 위원</li>
                                    <li>· 진) 연천초·과정초·연산중·남일고 학교운영위원</li>
                                </ul>
                            </div>
                            <!-- Column 2 -->
                            <div class="bio-col" style="background: #f1f5f9; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #10b981;">
                                <h3 style="color: #059669; font-size: 1.15rem; font-weight: 800; margin-bottom: 1rem;">주민과 마을을 사랑하는<br>실천가</h3>
                                <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.95rem; color: #334155; line-height: 1.5;">
                                    <li style="margin-bottom: 0.5rem;">· 전) 은빛노인학교 운영위원장</li>
                                    <li style="margin-bottom: 0.5rem;">· 신) 마을공동체 '어울마당' 대표</li>
                                    <li style="margin-bottom: 0.5rem;">· 신) 연제구 마을기업 '소풍' 대표</li>
                                    <li style="margin-bottom: 0.5rem;">· 전) 부산복지개발원 마을현장지원단</li>
                                    <li style="margin-bottom: 0.5rem;">· 전) 부산풀뿌리네트워크 운영위원</li>
                                    <li style="margin-bottom: 0.5rem;">· 전) 연제구 주민참여예산위원회 위원</li>
                                    <li>· 전) 연제통합돌봄자문위원</li>
                                </ul>
                            </div>
                            <!-- Column 3 -->
                            <div class="bio-col" style="background: #f1f5f9; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #f43f5e;">
                                <h3 style="color: #e11d48; font-size: 1.15rem; font-weight: 800; margin-bottom: 1rem;">여성과 아이들의<br>대변인</h3>
                                <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.95rem; color: #334155; line-height: 1.5;">
                                    <li style="margin-bottom: 0.5rem;">· 진) 토곡좋은엄마모임 회장</li>
                                    <li style="margin-bottom: 0.5rem;">· 진) 부산학부모연대 대표</li>
                                    <li style="margin-bottom: 0.5rem;">· 전) 부산여성회 부대표</li>
                                    <li style="margin-bottom: 0.5rem;">· 전) 부산교육희망네트워크 공동대표</li>
                                    <li>· 전) 초록우산어린이재단 <br><span style="font-size:0.85rem; color:#64748b;">(아이들의 신호에 응답하라. Face for Child 55인 대표)</span></li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <!-- 2. 마을에서 주민과 함께 해냈습니다! -->
                    <div class="bio-section-designed reveal" style="background: white; border-radius: 16px; padding: 2.5rem 1.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 3rem;">
                        <h2 style="font-size: 2rem; color: #1e3a8a; font-weight: 900; text-align: center; margin-bottom: 2rem;">마을에서 주민과 함께<br>해냈습니다!</h2>
                        
                        <div style="display: flex; flex-direction: column; gap: 2rem;">
                            <!-- Item 1 -->
                            <div style="border-bottom: 1px solid #e2e8f0; padding-bottom: 1.5rem;">
                                <h4 style="font-size: 1.25rem; color: #1e293b; font-weight: 800; margin-bottom: 0.5rem;"><span style="color:#0284c7;">1.</span> 모두가 불가능하다고 한 배산유아숲터 화장실 건립</h4>
                                <p style="color: #0284c7; font-weight: 700; margin-bottom: 0.8rem; background: #e0f2fe; padding: 0.6rem 1rem; border-radius: 8px;">“아이들이 간이 텐트와 구덩이에서 용변을 해결하고 있어요”</p>
                                <p style="color: #475569; font-size: 0.95rem; line-height: 1.6;">아이들을 위한 유아숲터에 아이들이 이용할 수 있는 화장실이 없다는 절박한 목소리. 구청은 "어렵다"고 말했습니다.<br>연제구 엄마·아빠 3,560명의 서명을 모아 끝까지 요구했고 구청을 끈질기게 설득했습니다. 마침내 우리 아이들을 위한 깨끗하고 안전한 친환경 화장실을 건립했습니다. <strong>결국 주민의 힘으로 해냈습니다.</strong></p>
                            </div>
                            <!-- Item 2 -->
                            <div style="border-bottom: 1px solid #e2e8f0; padding-bottom: 1.5rem;">
                                <h4 style="font-size: 1.25rem; color: #1e293b; font-weight: 800; margin-bottom: 0.5rem;"><span style="color:#0284c7;">2.</span> 엄마가 안심하고 아이들이 안전한 연제</h4>
                                <p style="color: #0284c7; font-weight: 700; margin-bottom: 0.8rem; background: #e0f2fe; padding: 0.6rem 1rem; border-radius: 8px;">“학교 주변 길이 너무 위험합니다. 모든 길이 안전하길 바랍니다”</p>
                                <ul style="list-style: none; padding: 0; margin: 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
                                    <li>· 등하교 동행도우미 '워킹스쿨버스' 도입 추진</li>
                                    <li>· 학교 앞 교통지도</li>
                                    <li>· 주민청구 아동통합돌봄조례 제정</li>
                                    <li>· 연제 어린이날 행사, 아파트 전래놀이, 물총놀이 개최</li>
                                    <li>· 느린학습자 부모모임 '맘 편한 느린숲' 결성</li>
                                </ul>
                            </div>
                            <!-- Item 3 -->
                            <div>
                                <h4 style="font-size: 1.25rem; color: #1e293b; font-weight: 800; margin-bottom: 0.5rem;"><span style="color:#0284c7;">3.</span> 소상공인, 어르신들께 진심</h4>
                                <ul style="list-style: none; padding: 0; margin: 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
                                    <li>· 취약계층 어르신 무료급식 지원예산 복원을 위한 활동</li>
                                    <li>· 교통지도 어르신들을 위한 '학교 내 에어컨 쉼터' 마련</li>
                                    <li>· 소상공인 부담경감 크레딧, 경영안정 바우처 등 소상공인 지원 신청부터 수령까지 끝까지 챙겨봐주는 사람</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <!-- 3. 후보가 전하는 메시지 -->
                    <div class="end-bio-section reveal" style="background: linear-gradient(135deg, #1e3a8a, #312e81); padding: 2.5rem 1.5rem; border-radius: 16px; color: white; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
                        <h2 style="font-size: 2.1rem; font-weight: 900; margin-bottom: 1.5rem; line-height: 1.3;"><span style="color: #60a5fa;">연산 8·9동</span> 구의원 2명 중<br>한 명은 <span style="color: #fca5a5;">진보구의원</span>으로!</h2>
                        <p style="font-size: 1.1rem; line-height: 1.7; opacity: 0.95; margin-bottom: 1.5rem; word-break: keep-all;">
                            공천만 받으면 당선되는 구의원은 주민 눈치를 보지 않습니다.<br>구의원 <strong style="color: #fca5a5;">해외연수부터 중단</strong>하고 4년 내내 주민을 향해 발로 뛰겠습니다.
                        </p>
                        <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem; border: 1px solid rgba(255,255,255,0.2);">
                            <p style="font-size: 1.3rem; font-weight: 800; margin-bottom: 0.5rem;">2등까지 당선되는 구의원</p>
                            <p style="font-size: 1.05rem;">주민후보 이정은을 주민의 힘으로 당선시켜주십시오.</p>
                        </div>
                        <p style="font-size: 1rem; line-height: 1.7; opacity: 0.8; margin-top: 1rem; word-break: keep-all;">
                            연산9동 한양아파트에서 신혼을 시작하며 이 동네에 뿌리를 내렸습니다.<br>
                            육아에 지친 엄마들과 함께 만든 토곡좋은엄마모임, 그곳이 제 출발이었습니다.<br><br>
                            노정현과 함께 골목을 돌며 주민의 목소리를 들었습니다.<br>
                            비 오는 날의 민원, 밤늦은 마을문제 토론 속에서 정치는 '주민의 삶을 바꾸는 일'임을 배웠습니다. 개발보다 사람, 성과보다 삶, 권력보다 주민. 그 원칙으로 20년을 현장에서 살아왔습니다.<br><br>
                            이제, 그 목소리를 의회로 가져가겠습니다. 오직 주민만 바라보며, 끝까지 함께 걷겠습니다.<br>
                            고맙습니다.
                        </p>
                        <div style="font-weight: 900; font-size: 1.25rem; margin-top: 2rem; color: #e0f2fe;">진보당 구의원 후보 이정은 드림</div>
                    </div>

                    <!-- 후원 정보 영역 -->
                    <div class="donation-box reveal" style="margin-top: 3rem; background: #fff; padding: 2rem 1.5rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center; border: 2px solid #e0f2fe; max-width: 600px; margin-left: auto; margin-right: auto;">
                        <h4 style="font-size: 1.35rem; color: #0284c7; margin-bottom: 0.8rem; font-weight: 800;"><i class="fas fa-heart" style="color: #ef4444; margin-right: 0.5rem;"></i>오직, 주민에게만 빚지고 싶습니다.</h4>
                        <div class="bank-account" style="font-size: 1.15rem; color: #1e293b; margin-bottom: 0.8rem; background: #f8fafc; padding: 0.8rem; border-radius: 8px;">
                            부산은행 <strong style="color: #0369a1; font-size: 1.4rem; letter-spacing: 1px;" id="copy-account-target">101-2095-7369-08</strong><br>
                            <span style="font-size: 1rem; color: #64748b; margin-top: 4px; display: inline-block;">예금주 : 이정은(연제구의원선거)</span>
                        </div>
                        
                        <div style="display: flex; flex-direction: column; align-items: center; gap: 0.5rem;">
                            <button class="btn-donate copy-account-btn" data-clipboard-target="#copy-account-target" style="width: 100%; max-width: 360px; padding: 0.8rem; background-color: #0284c7; color: white; border: none; border-radius: 30px; font-size: 1.15rem; font-weight: 700; cursor: pointer; display: flex; justify-content: center; align-items: center; gap: 0.5rem; transition: background-color 0.2s; margin-top: 0;">
                                후원계좌 복사하기 <i class="fas fa-copy"></i>
                            </button>
                            <a href="tel:010-9476-6924" class="btn-donate" style="width: 100%; max-width: 360px; padding: 0.8rem; background-color: #0f172a; color: white; border: none; border-radius: 30px; font-size: 1.15rem; font-weight: 700; cursor: pointer; display: flex; justify-content: center; align-items: center; gap: 0.5rem; text-decoration: none; margin-top: 0;">
                                후원문의 : 010-9476-6924
                            </a>
                        </div>
                    </div>
                </div>
            </section>"""
    html = html.replace(about_match.group(0), about_new)

# 7. Pledge sections rewrite
pledge_match = re.search(r'<!-- VIEW: PLEDGE 1 -->.*?<!-- VIEW: LOCATION \(SECTION 4\) -->', html, re.DOTALL)
if pledge_match:
    pledges_new = """<!-- VIEW: PLEDGE (이정은의 수첩) -->
        <div id="view-pledge" class="view-section" style="background-color: #f1f5f9; padding-bottom: 3rem;">
            <!-- Hero image for Pledges -->
            <div class="pledge-hero-wide reveal" style="background-color: #1e3a8a; padding: 4rem 1.5rem; text-align: center; color: white;">
                <h2 style="font-size: 3rem; font-weight: 900; margin-bottom: 1rem; color: white;">이정은의 수첩</h2>
                <p style="font-size: 1.25rem; font-weight: 500; opacity: 0.9;">주민의 말씀을 정책으로 실현합니다</p>
            </div>
            
            <div class="pledge-detail-container" style="max-width: 800px; margin: -2rem auto 0 auto; position: relative; z-index: 10; padding: 0 1.5rem;">
                
                <div style="display: grid; grid-template-columns: 1fr; gap: 1.5rem;">
                    <!-- 1 -->
                    <div class="reveal" style="background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid #0284c7;">
                        <h3 style="color: #0284c7; font-size: 1.4rem; font-weight: 900; margin-bottom: 0.3rem;"><span style="font-size:2rem; margin-right:0.5rem;">1</span>돌봄 1번지 연제</h3>
                        <p style="color: #1e293b; font-weight: 700; margin-bottom: 1rem; font-size: 1.1rem;">"아이 키우고 돌보기 좋은 동네"</p>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #475569; line-height: 1.6;">
                            <li>· 아동통합돌봄 플랫폼 구축</li>
                            <li>· 느린학습자 교육권 지원 조례</li>
                            <li>· 방학 중 학교 급식 지원</li>
                            <li>· 지자체 운영 육아용품 대여점 확대</li>
                        </ul>
                    </div>
                    
                    <!-- 2 -->
                    <div class="reveal" style="background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid #e11d48;">
                        <h3 style="color: #e11d48; font-size: 1.4rem; font-weight: 900; margin-bottom: 0.3rem;"><span style="font-size:2rem; margin-right:0.5rem;">2</span>아이·여성·노인 안전/생활 강화</h3>
                        <p style="color: #1e293b; font-weight: 700; margin-bottom: 1rem; font-size: 1.1rem;">"안전은 선택이 아니라 권리입니다"</p>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #475569; line-height: 1.6;">
                            <li>· 워킹스쿨버스 제도 도입 및 통학로 개선</li>
                            <li>· 여성·아동 안심귀갓길 확대</li>
                            <li>· 골목 CCTV·가로등 주민신청제</li>
                            <li>· 어르신 품위유지비 지원</li>
                        </ul>
                    </div>

                    <!-- 3 -->
                    <div class="reveal" style="background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid #0284c7;">
                        <h3 style="color: #0284c7; font-size: 1.4rem; font-weight: 900; margin-bottom: 0.3rem;"><span style="font-size:2rem; margin-right:0.5rem;">3</span>골목상권·전통시장 살리기</h3>
                        <p style="color: #1e293b; font-weight: 700; margin-bottom: 1rem; font-size: 1.1rem;">"동네가 살아야 경제가 삽니다"</p>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #475569; line-height: 1.6;">
                            <li>· 전통시장·골목상권 활성화 특별예산 확보</li>
                            <li>· 상인·주민 참여형 상권사업 운영</li>
                            <li>· 공공배달앱 도입</li>
                        </ul>
                    </div>

                    <!-- 4 -->
                    <div class="reveal" style="background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid #e11d48;">
                        <h3 style="color: #e11d48; font-size: 1.4rem; font-weight: 900; margin-bottom: 0.3rem;"><span style="font-size:2rem; margin-right:0.5rem;">4</span>주차·교통 생활불편 해결</h3>
                        <p style="color: #1e293b; font-weight: 700; margin-bottom: 1rem; font-size: 1.1rem;">"주차 스트레스는 줄이고, 보행권은 되찾고"</p>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #475569; line-height: 1.6;">
                            <li>· 공영주차장 확충 및 공유주차제 활성화</li>
                            <li>· 학교·시장 주변 교통 체계 개선</li>
                            <li>· 유모차와 휠체어가 마음 편히 다니는 '무장애 보행로' 조성</li>
                        </ul>
                    </div>

                    <!-- 5 -->
                    <div class="reveal" style="background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid #0284c7;">
                        <h3 style="color: #0284c7; font-size: 1.4rem; font-weight: 900; margin-bottom: 0.3rem;"><span style="font-size:2rem; margin-right:0.5rem;">5</span>침수·하수·도시안전 대책</h3>
                        <p style="color: #1e293b; font-weight: 700; margin-bottom: 1rem; font-size: 1.1rem;">"비 오면 불안한 동네 끝내겠습니다"</p>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #475569; line-height: 1.6;">
                            <li>· 상습침수 골목 하수관로 전면 점검·교체</li>
                            <li>· 재난 취약가구 우선 지원</li>
                            <li>· 빗물받이·배수시설 정기 점검 의무화</li>
                        </ul>
                    </div>

                    <!-- 6 -->
                    <div class="reveal" style="background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid #e11d48;">
                        <h3 style="color: #e11d48; font-size: 1.4rem; font-weight: 900; margin-bottom: 0.3rem;"><span style="font-size:2rem; margin-right:0.5rem;">6</span>주민결정 정치제도화</h3>
                        <p style="color: #1e293b; font-weight: 700; margin-bottom: 1rem; font-size: 1.1rem;">"주민이 명령하면 구청이 실행합니다"</p>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #475569; line-height: 1.6;">
                            <li>· 동별 생활불편 해결을 위한 예산 상설 배정</li>
                            <li>· '연제구주민대회' 제도화 및 주민발안제 도입</li>
                            <li>· 공공기관 유휴시설 야간·휴일 개방 추진</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- VIEW: LOCATION (SECTION 4) -->
"""
    html = html.replace(pledge_match.group(0), pledges_new)

# 8. Location & Footer
html = html.replace('부산시 연제구 월드컵대로 141, 동화빌딩 7층', '부산시 연제구 과정로 202, 2층')
html = html.replace('혜암뷔페 옆 건물', '') # remove building detail if no longer applicable
html = html.replace('010-4454-4094', '010-9476-6924')
html = html.replace('노정현 후보 선거캠프', '이정은 후보 선거캠프')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully.")
