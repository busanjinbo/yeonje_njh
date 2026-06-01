document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal Animation (스크롤 시 요소 페이드인 효과)
    const revealElements = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // 한 번만 애니메이션 발생
            }
        });
    }, {
        root: null,
        threshold: 0.1, // 10% 정도 요소가 보이면 발생
        rootMargin: "0px 0px -20px 0px"
    });

    revealElements.forEach(el => {
        // hero-content나 image-container 같이 처음에 바로 보여져야 하는 부분은 active 처리
        if (!el.classList.contains('active')) {
            revealObserver.observe(el);
        }
    });

    // Copy Account Number Logic (후원계좌 복사)
    const copyBtn = document.getElementById('copy-btn');
    const accountEl = document.getElementById('account-number');
    const accountNumberText = accountEl ? accountEl.innerText : '113-2020-3080-07';
    const toast = document.getElementById('toast');
    let toastTimeout;

    if (copyBtn) {
        copyBtn.addEventListener('click', () => {
            handleCopy(accountNumberText, '계좌번호가 복사되었습니다.');
        });
    }

    const copyAccountBtns = document.querySelectorAll('.copy-account-btn');
    copyAccountBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-clipboard-target');
            let textToCopy = "113-2020-3080-07"; // default
            if (targetId) {
                const targetEl = document.querySelector(targetId);
                if (targetEl) textToCopy = targetEl.innerText;
            }
            handleCopy(textToCopy, '계좌번호가 복사되었습니다.');
        });
    });

    function handleCopy(textToCopy, successMsg) {
        if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(textToCopy).then(() => {
                showToast(successMsg);
            }).catch(err => {
                console.error('클립보드 복사 실패:', err);
                fallbackCopyTextToClipboard(textToCopy, successMsg);
            });
        } else {
            fallbackCopyTextToClipboard(textToCopy, successMsg);
        }
    }

    function fallbackCopyTextToClipboard(text, msg) {
        const textArea = document.createElement("textarea");
        textArea.value = text;
        
        // 화면에서 보이지 않게 처리
        textArea.style.position = "fixed";
        textArea.style.top = "0";
        textArea.style.left = "0";
        textArea.style.width = "2em";
        textArea.style.height = "2em";
        textArea.style.padding = "0";
        textArea.style.border = "none";
        textArea.style.outline = "none";
        textArea.style.boxShadow = "none";
        textArea.style.background = "transparent";
        
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();

        try {
            document.execCommand('copy');
            showToast(msg);
        } catch (err) {
            console.error('Fallback: 복사 실패', err);
            alert('복사하지 못했습니다. 직접 복사해주세요: ' + text);
        }

        document.body.removeChild(textArea);
    }

    function showToast(msg = '계좌가 복사되었습니다.') {
        const toastMsg = document.getElementById('toast-msg');
        if(toastMsg) toastMsg.innerText = msg;

        // 이미 나타나 있으면 초기화
        toast.classList.remove('show');
        clearTimeout(toastTimeout);
        
        // 약간의 딜레이 후 다시 보여줌 (애니메이션 리셋 위함)
        setTimeout(() => {
            toast.classList.add('show');
            // 2.5초 후 닫기
            toastTimeout = setTimeout(() => {
                toast.classList.remove('show');
            }, 2500);
        }, 50);
    }

    // SPA Navigation & Routing Logic
    const navLinks = document.querySelectorAll('.nav-link, .nav-logo, .btn-pledge, .hz-pledge-card, .grid-pledge-card');
    const viewSections = document.querySelectorAll('.view-section');

    // 1. 새로고침 시 이전에 있던 스크롤 위치로 멋대로 복원되지 않도록 방지
    try {
        if ('scrollRestoration' in history) {
            history.scrollRestoration = 'manual';
        }
    } catch(e) {}

    // 2. 해시 주소를 기반으로 화면과 메뉴 상태를 바꾸는 함수
    function handleHashChange() {
        let hash = window.location.hash;
        let targetId = hash ? hash.substring(1) : 'view-home';

        let targetSect = document.getElementById(targetId);
        
        // 올바르지 않은 주소거나 해시가 없으면 기본으로 메인 화면 설정
        if (!targetSect) {
            targetId = 'view-home';
            targetSect = document.getElementById('view-home');
            try {
                history.replaceState(null, null, '#' + targetId);
            } catch(e) {}
        }

        // 모든 섹션 숨김 처리
        viewSections.forEach(sec => sec.classList.remove('active-section'));
        
        // 타겟 섹션 보이기
        if (targetSect) {
            targetSect.classList.add('active-section');
            
            // 새 섹션의 애니메이션 속성 초기화 (스크롤 올리면 다시 뜨도록)
            const reveals = targetSect.querySelectorAll('.reveal');
            reveals.forEach(el => {
                el.classList.remove('active');
                revealObserver.observe(el);
            });

            // location 섹션은 reveal 없이 즉시 표시 (IntersectionObserver 미트리거 방지)
            if (targetId === 'view-location') {
                setTimeout(() => {
                    targetSect.querySelectorAll('.reveal').forEach(el => el.classList.add('active'));
                }, 50);
            }
            
            // 유튜브 영상 뷰 전환 시 재생 방지를 위한 비디오 모달 클리어 로직
            if (targetId !== 'view-about') {
                const videoModal = document.getElementById('video-player-modal');
                if (videoModal && videoModal.classList.contains('show')) {
                    videoModal.classList.remove('show');
                    const wrap = document.getElementById('modal-video-wrap');
                    if (wrap) wrap.innerHTML = '';
                }
            }
        }

        // 메뉴 활성화(액티브) 상태 업데이트
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        const activeLink = document.querySelector(`.nav-link[data-target="${targetId}"]`);
        
        if (activeLink) {
            activeLink.classList.add('active');
            
            // 모바일 서브메뉴(Dropdown) 안의 링크면 부모 메뉴도 활성화
            if (activeLink.parentElement && activeLink.parentElement.classList.contains('nav-dropdown-content')) {
                const parentToggle = activeLink.parentElement.previousElementSibling;
                if (parentToggle && parentToggle.classList.contains('nav-dropdown-toggle')) {
                    parentToggle.classList.add('active');
                }
            }
        }

        // 화면 전환이 완료되었으므로 최상단으로 이동 (새로고침 시 문제 해결의 핵심 요소)
        window.scrollTo(0, 0);
    }

    // 3. 네비게이션 및 퀵메뉴 스크롤/이동 공통 처리
    let pendingScroll = null;
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('data-target');
            const scrollId = this.getAttribute('data-scroll');
            
            // 모바일 메뉴 버튼 클릭 시 메뉴 닫기 기능
            const quickMenuTrigger = document.getElementById('quick-menu-trigger');
            const quickMenuPanel = document.getElementById('quick-menu-panel');
            if (quickMenuPanel && quickMenuPanel.classList.contains('open')) {
                quickMenuPanel.classList.remove('open');
                if(quickMenuTrigger) {
                    quickMenuTrigger.classList.remove('active');
                    const menuIcon = quickMenuTrigger.querySelector('i');
                    if (menuIcon) {
                        menuIcon.classList.remove('fa-times');
                        menuIcon.classList.add('fa-bars');
                    }
                }
            }
            
            // 상단바 모바일 메뉴 닫기 기능
            const navMenu = document.querySelector('.nav-menu');
            const navMobileTrigger = document.getElementById('nav-mobile-trigger');
            if (navMenu && navMenu.classList.contains('open')) {
                navMenu.classList.remove('open');
                if (navMobileTrigger) {
                    navMobileTrigger.classList.remove('active');
                    const icon = navMobileTrigger.querySelector('i');
                    if (icon) {
                        icon.classList.remove('fa-times');
                        icon.classList.add('fa-bars');
                    }
                }
            }
            
            if (targetId) {
                e.preventDefault();
                const currentHash = window.location.hash.substring(1) || 'view-home';
                
                if (currentHash === targetId) {
                    // 이미 해당 뷰에 있으면 스크롤만 
                    if (scrollId) {
                        const scrollToEl = document.getElementById(scrollId);
                        if (scrollToEl) scrollToEl.scrollIntoView({behavior: 'smooth'});
                    } else {
                        window.scrollTo({top:0, behavior:'smooth'});
                    }
                } else {
                    // 해시를 변경하고 화면 렌더링 후 스크롤을 위해 저장
                    if (scrollId) pendingScroll = scrollId;
                    window.location.hash = targetId;
                }
            }
        });
    });

    // 4. 주소창(URL)의 해시 이벤트 발생 감지
    window.addEventListener('hashchange', () => {
        handleHashChange();
        // 화면 전환 후 보류해둔 스크롤 수행
        if (pendingScroll) {
            setTimeout(() => {
                const scrollToEl = document.getElementById(pendingScroll);
                if (scrollToEl) scrollToEl.scrollIntoView({behavior: 'smooth'});
                pendingScroll = null;
            }, 50);
        }
    });

    // 5. 스크립트 최초 로드/새로고침 시 해당 주소로 초기 렌더링
    handleHashChange();

    // 6. Mobile Top Nav Dropdown Toggle
    const navDropdownToggle = document.querySelector('.nav-dropdown-toggle');
    const navDropdown = document.querySelector('.nav-dropdown');
    if (navDropdownToggle && navDropdown) {
        navDropdownToggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                navDropdown.classList.toggle('open-mobile');
            }
        });
        
        // 클릭 외 공간 터치시 닫기
        document.addEventListener('click', (e) => {
            if (window.innerWidth <= 768 && !navDropdown.contains(e.target)) {
                navDropdown.classList.remove('open-mobile');
            }
        });
    }

    // 7. Quick Menu Trigger (FAB 팝업 열기/닫기)
    const quickMenuTrigger = document.getElementById('quick-menu-trigger');
    const quickMenuPanel = document.getElementById('quick-menu-panel');
    if (quickMenuTrigger && quickMenuPanel) {
        quickMenuTrigger.addEventListener('click', () => {
            quickMenuPanel.classList.toggle('open');
            quickMenuTrigger.classList.toggle('active');
            
            const icon = quickMenuTrigger.querySelector('i');
            if (quickMenuPanel.classList.contains('open')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // 8. Quick Menu Toggle (공약 항목 팝업)
    const quickPledgeBtn = document.getElementById('quick-pledge-btn');
    if (quickPledgeBtn) {
        quickPledgeBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const grp = quickPledgeBtn.parentElement;
            const sub = grp.querySelector('.quick-sub');
            if(sub) sub.classList.toggle('open');
        });
    }

    // Accordion Logic
    const accordionBtn = document.getElementById('accordion-btn');
    const accordionContent = document.getElementById('accordion-content');
    
    if (accordionBtn && accordionContent) {
        accordionBtn.addEventListener('click', () => {
            accordionContent.classList.toggle('open');
            const icon = accordionBtn.querySelector('i');
            if (icon) {
                if (accordionContent.classList.contains('open')) {
                    icon.classList.remove('fa-chevron-down');
                    icon.classList.add('fa-chevron-up');
                } else {
                    icon.classList.remove('fa-chevron-up');
                    icon.classList.add('fa-chevron-down');
                }
            }
        });
    }

    // Kakao Map Initialization removed (Using static image map instead)

    // SNS Deep Linking
    const snsBtns = document.querySelectorAll('.sns-btn');
    const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

    snsBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const webUrl = this.getAttribute('data-web');
            const intentUrl = this.getAttribute('data-aos');

            if (isMobile && intentUrl) {
                // Try to open app via intent (mostly Android)
                window.location.href = intentUrl;
                
                // Fallback to web if app doesn't open
                setTimeout(() => {
                    window.open(webUrl, '_blank');
                }, 1500);
            } else {
                window.open(webUrl, '_blank');
            }
        });
    });

    // Address & Phone Copy Logic
    const copyAddressBtn = document.getElementById('copy-address');
    if (copyAddressBtn) {
        copyAddressBtn.addEventListener('click', () => {
            handleCopy("부산시 연제구 월드컵대로 141, 동화빌딩 7층", "주소가 복사되었습니다.");
        });
    }

    const copyPhoneBtns = document.querySelectorAll('.copy-phone');
    copyPhoneBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            handleCopy("010-5840-3422", "전화번호가 복사되었습니다.");
        });
    });

    const copyMainPhoneBtns = document.querySelectorAll('.copy-main-phone');
    copyMainPhoneBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            handleCopy("010-4454-4094", "전화번호가 복사되었습니다.");
        });
    });

    // Modal Image Zoom Logic
    const mapImgBtn = document.getElementById('location-map-img');
    const imageModal = document.getElementById('image-modal');
    const modalImage = document.getElementById('modal-image');
    const closeModal = document.getElementById('close-modal');

    if (mapImgBtn && imageModal) {
        mapImgBtn.addEventListener('click', () => {
            modalImage.src = mapImgBtn.src;
            imageModal.classList.add('show');
        });

        closeModal.addEventListener('click', () => {
            imageModal.classList.remove('show');
        });

        imageModal.addEventListener('click', () => {
            imageModal.classList.remove('show');
        });
    }

    // 9. Mobile Top Nav Hamburger Menu
    const navMobileTrigger = document.getElementById('nav-mobile-trigger');
    const navMenu = document.querySelector('.nav-menu');
    if (navMobileTrigger && navMenu) {
        navMobileTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            navMenu.classList.toggle('open');
            navMobileTrigger.classList.toggle('active');
            
            const icon = navMobileTrigger.querySelector('i');
            if (navMenu.classList.contains('open')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (window.innerWidth <= 768 && navMenu.classList.contains('open') && !navMenu.contains(e.target) && !navMobileTrigger.contains(e.target)) {
                navMenu.classList.remove('open');
                navMobileTrigger.classList.remove('active');
                const icon = navMobileTrigger.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    }

    // 반응형 비디오 슬라이더 로직
    const track = document.getElementById('youtube-slider-track');
    const prevBtn = document.getElementById('video-prev-btn');
    const nextBtn = document.getElementById('video-next-btn');
    const indicators = document.querySelectorAll('#video-slider-indicators .indicator');
    const trackWrap = document.querySelector('.video-slider-track-wrap');
    
    let currentSlideIndex = 0;
    const totalSlides = 6;
    
    function getSlideWidth() {
        if (!track) return 0;
        const firstSlide = track.querySelector('.video-slide');
        return firstSlide ? firstSlide.getBoundingClientRect().width : 0;
    }
    
    function getGap() {
        if (window.innerWidth > 768) {
            // styles.css에 정의된 PC에서의 .video-slider-track gap은 1rem (= 16px)
            return 16;
        }
        return 0; // 모바일에서는 gap이 없고 슬라이드가 100% 꽉 찹니다.
    }

    function updateSlider() {
        if (!track) return;
        const isMobile = window.innerWidth <= 768;
        const slideWidth = getSlideWidth();
        const gap = getGap();
        
        // 인덱스 범위 초과 방지
        const maxIndex = isMobile ? totalSlides - 1 : totalSlides - 3;
        if (currentSlideIndex > maxIndex) currentSlideIndex = maxIndex;
        if (currentSlideIndex < 0) currentSlideIndex = 0;
        
        if (isMobile) {
            // 모바일은 100% 단위로 이동
            track.style.transform = `translateX(-${currentSlideIndex * 100}%)`;
        } else {
            // PC는 실제 슬라이드 너비 + gap 만큼 이동
            const moveX = currentSlideIndex * (slideWidth + gap);
            track.style.transform = `translateX(-${moveX}px)`;
        }
        
        // 인디케이터 업데이트 (모바일 환경 또는 인디케이터가 활성화된 상황 대응)
        indicators.forEach((ind, index) => {
            if (index === currentSlideIndex) {
                ind.classList.add('active');
            } else {
                ind.classList.remove('active');
            }
        });
    }

    if (track) {
        // PC용 화살표 클릭 핸들러
        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                if (currentSlideIndex > 0) {
                    currentSlideIndex--;
                    updateSlider();
                }
            });
        }
        
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                const maxIndex = window.innerWidth <= 768 ? totalSlides - 1 : totalSlides - 3;
                if (currentSlideIndex < maxIndex) {
                    currentSlideIndex++;
                    updateSlider();
                }
            });
        }
        
        // 인디케이터 클릭 핸들러
        indicators.forEach(indicator => {
            indicator.addEventListener('click', function() {
                const idx = parseInt(this.getAttribute('data-slide-index'), 10);
                currentSlideIndex = idx;
                updateSlider();
            });
        });
        
        // 리사이즈 이벤트 대응
        window.addEventListener('resize', () => {
            updateSlider();
        });
        
        // 모바일 터치 스와이프 (손가락 드래그) 이벤트 추가
        let touchStartX = 0;
        let touchEndX = 0;
        
        if (trackWrap) {
            trackWrap.addEventListener('touchstart', (e) => {
                touchStartX = e.changedTouches[0].screenX;
            }, { passive: true });
            
            trackWrap.addEventListener('touchend', (e) => {
                touchEndX = e.changedTouches[0].screenX;
                handleSwipe();
            }, { passive: true });
        }
        
        function handleSwipe() {
            const swipeDistance = touchEndX - touchStartX;
            const threshold = 50; // 스와이프 최소 감지 거리 (50px)
            
            if (swipeDistance < -threshold) {
                // 왼쪽으로 스와이프 -> 다음 영상 보기
                const maxIndex = window.innerWidth <= 768 ? totalSlides - 1 : totalSlides - 3;
                if (currentSlideIndex < maxIndex) {
                    currentSlideIndex++;
                    updateSlider();
                }
            } else if (swipeDistance > threshold) {
                // 오른쪽으로 스와이프 -> 이전 영상 보기
                if (currentSlideIndex > 0) {
                    currentSlideIndex--;
                    updateSlider();
                }
            }
        }
    }

    // Video Fullscreen Modal Logic
    const videoSlides = document.querySelectorAll('.video-slide');
    const videoPlayerModal = document.getElementById('video-player-modal');
    const videoPlayerModalWrap = document.getElementById('modal-video-wrap');
    const closeVideoModal = document.getElementById('close-video-modal');

    if (videoSlides.length > 0 && videoPlayerModal && videoPlayerModalWrap) {
        videoSlides.forEach(slide => {
            const thumbWrap = slide.querySelector('.video-thumbnail-wrap');
            if (thumbWrap) {
                thumbWrap.addEventListener('click', () => {
                    const videoId = slide.getAttribute('data-video-id');
                    const title = slide.querySelector('.video-slide-title').innerText;
                    
                    // iframe 동적 주입 및 자동재생 활성화
                    videoPlayerModalWrap.innerHTML = `<iframe width="100%" height="100%" src="https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0&vq=hd1080" title="${title}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute; top:0; left:0; width:100%; height:100%; border:none;"></iframe>`;
                    
                    // 모달 노출
                    videoPlayerModal.classList.add('show');
                });
            }
        });

        const hideVideoModal = () => {
            videoPlayerModal.classList.remove('show');
            videoPlayerModalWrap.innerHTML = ''; // iframe 제거하여 재생 정지
        };

        if (closeVideoModal) {
            closeVideoModal.addEventListener('click', hideVideoModal);
        }

        videoPlayerModal.addEventListener('click', (e) => {
            // 모달 콘텐츠 바깥쪽 클릭 시 닫기
            if (e.target === videoPlayerModal) {
                hideVideoModal();
            }
        });
    }
});
