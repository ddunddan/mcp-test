# MCP 리소스(Resource) 예시

## 리소스의 이해

리소스는 LLM이 접근할 수 있는 외부 데이터 소스입니다. 이를 통해 모델은 학습 데이터 외의 추가 정보에 액세스할 수 있습니다. 리소스는 모델의 응답을 향상시키고 최신 또는 특정 정보를 제공하는 데 중요합니다.

## 리소스 유형 및 예시

### 1. 문서 데이터베이스

제품 매뉴얼, 회사 정책, 기술 문서 또는 FAQ와 같은 텍스트 문서를 제공합니다.

```json
{
  "resources": [
    {
      "type": "document",
      "id": "company_policy",
      "title": "회사 출장 정책",
      "content": "1. 출장 승인: 모든 출장은 최소 1주일 전에 승인되어야 합니다.\n2. 경비 한도: 국내 출장의 경우 1일당 숙박비 15만원, 식비 3만원이 허용됩니다.\n3. 교통수단: 가능한 한 대중교통을 이용해야 합니다. 택시는 대중교통 이용이 불가능한 경우에만 허용됩니다.",
      "metadata": {
        "lastUpdated": "2025-02-01",
        "department": "HR",
        "version": "2.3"
      }
    }
  ]
}
```

### 2. 웹 콘텐츠

검색 결과, 웹 페이지 또는 뉴스 기사와 같은 웹에서 검색된 정보를 제공합니다.

```json
{
  "resources": [
    {
      "type": "web_search",
      "id": "ai_news",
      "query": "최신 AI 기술 발전",
      "results": [
        {
          "title": "2025년 주목해야 할 5가지 AI 기술 동향",
          "url": "https://example.com/ai-trends-2025",
          "snippet": "최근 발표된 연구에 따르면, 멀티모달 AI, 강화학습 개선, 및 저전력 AI 처리 기술이 2025년 인공지능 분야의 주요 동향으로 부상하고 있습니다..."
        },
        {
          "title": "생성형 AI의 최신 혁신",
          "url": "https://example.com/generative-ai-innovations",
          "snippet": "최근 발표된 생성형 AI 모델은 이전보다 50% 적은 학습 데이터로 더 정확한 결과를 생성할 수 있습니다..."
        }
      ],
      "metadata": {
        "searchDate": "2025-04-03",
        "resultCount": 2,
        "searchEngine": "ExampleSearch"
      }
    }
  ]
}
```

### 3. 구조화된 데이터

표, 데이터베이스 또는 JSON/CSV 형식의 구조화된 정보를 제공합니다.

```json
{
  "resources": [
    {
      "type": "structured_data",
      "id": "product_inventory",
      "format": "table",
      "schema": ["product_id", "name", "category", "price", "stock"],
      "data": [
        ["P001", "울트라 노트북", "전자제품", 1200000, 45],
        ["P002", "무선 이어버드", "오디오", 150000, 78],
        ["P003", "스마트 시계", "웨어러블", 350000, 23],
        ["P004", "게이밍 마우스", "컴퓨터 주변기기", 89000, 12]
      ],
      "metadata": {
        "lastUpdated": "2025-04-01",
        "warehouse": "서울 중앙",
        "currency": "KRW"
      }
    }
  ]
}
```

### 4. 개인 지식 저장소

개인 메모, 이메일, 일정 또는 연락처와 같은 사용자별 정보를 제공합니다.

```json
{
  "resources": [
    {
      "type": "personal_data",
      "id": "user_notes",
      "notes": [
        {
          "title": "회의 메모 - 제품 출시 계획",
          "date": "2025-03-22",
          "content": "- 마케팅 자료는 4월 10일까지 준비\n- 소셜 미디어 캠페인은 4월 15일 시작\n- 프레스 릴리스는 4월 20일 배포\n- 사용자 테스트 피드백 수집 필요"
        },
        {
          "title": "프로젝트 아이디어",
          "date": "2025-03-28",
          "content": "AI 기반 고객 서비스 챗봇 개발 - 기존 FAQ를 활용하여 훈련, 고객 문의 응답 자동화, 복잡한 질문은 담당자에게 전달"
        }
      ],
      "metadata": {
        "owner": "김철수",
        "device": "스마트폰",
        "app": "메모 앱"
      }
    }
  ]
}
```

### 5. 멀티미디어 콘텐츠

이미지, 오디오 또는 비디오의 텍스트 설명 또는 메타데이터를 제공합니다.

```json
{
  "resources": [
    {
      "type": "multimedia",
      "id": "product_images",
      "images": [
        {
          "filename": "product_front.jpg",
          "description": "제품의 전면 사진으로, 7인치 디스플레이와 메탈 프레임이 특징입니다.",
          "tags": ["전자제품", "태블릿", "전면"]
        },
        {
          "filename": "product_side.jpg",
          "description": "제품의 측면 사진으로, 두께는 7.5mm이며 USB-C 포트와 전원 버튼이 보입니다.",
          "tags": ["전자제품", "태블릿", "측면", "포트"]
        }
      ],
      "metadata": {
        "productName": "슈퍼 태블릿 X",
        "photoDate": "2025-02-15",
        "photographer": "박영희"
      }
    }
  ]
}
```

## 리소스 활용 모범 사례

1. **관련성 보장**: 작업에 직접 관련된 리소스만 제공하세요.
2. **신뢰성 검증**: 정확하고 최신 정보를 포함하는 리소스를 사용하세요.
3. **구조화**: 모델이 쉽게 처리할 수 있도록 정보를 논리적으로 구조화하세요.
4. **메타데이터 포함**: 출처, 날짜 및 버전과 같은 컨텍스트 정보를 제공하세요.
5. **양 조절**: 너무 많은 정보로 모델을 과부하시키지 마세요. 필요한 정보만 제공하세요.
