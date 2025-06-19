# Resource 예시 모음

## 이미지 Resource

이미지 Resource는 AI 모델이 시각적 정보를 분석하고 이해하는 데 사용됩니다.

### 활용 사례
- **이미지 분석**: "이 사진에 있는 물체들을 식별해주세요."
- **시각 자료 설명**: "이 그래프가 보여주는 추세를 분석해주세요."
- **시각적 컨텍스트 제공**: "이 도표를 바탕으로 데이터 특성을 설명해주세요."

### 예시 코드
```python
# 이미지를 MCP Resource로 로드하는 예시
with open("chart.png", "rb") as image_file:
    image_data = image_file.read()
    image_resource = MCPResource(
        type="image",
        content=image_data,
        mime_type="image/png"
    )
```

## 문서 Resource

문서 Resource는 텍스트 기반 정보를 AI 모델에 제공합니다.

### 활용 사례
- **문서 요약**: "이 PDF 보고서의 핵심 내용을 요약해주세요."
- **정보 추출**: "이 계약서에서 중요 조항을 찾아주세요."
- **지식 참조**: "이 기술 문서를 바탕으로 구현 방법을 설명해주세요."

### 예시 코드
```python
# PDF 문서를 MCP Resource로 로드하는 예시
with open("report.pdf", "rb") as pdf_file:
    pdf_data = pdf_file.read()
    pdf_resource = MCPResource(
        type="document",
        content=pdf_data,
        mime_type="application/pdf"
    )
```

## 데이터셋 Resource

데이터셋 Resource는 AI 모델이 구조화된 데이터를 분석하는 데 사용됩니다.

### 활용 사례
- **데이터 분석**: "이 판매 데이터의 월별 추세를 분석해주세요."
- **패턴 식별**: "이 사용자 데이터에서 중요한 패턴을 찾아주세요."
- **예측 모델링**: "이 과거 데이터를 바탕으로 다음 달 수요를 예측해주세요."

### 예시 코드
```python
# CSV 데이터셋을 MCP Resource로 로드하는 예시
import pandas as pd

data = pd.read_csv("sales_data.csv")
csv_resource = MCPResource(
    type="dataset",
    content=data.to_json(),
    mime_type="application/json"
)
```

## 웹 콘텐츠 Resource

웹 콘텐츠 Resource는 웹에서 가져온 정보를 AI 모델에 제공합니다.

### 활용 사례
- **웹 페이지 분석**: "이 웹사이트의 주요 내용을 요약해주세요."
- **최신 정보 활용**: "이 뉴스 기사를 바탕으로 최근 동향을 설명해주세요."
- **다국어 콘텐츠**: "이 외국어 웹페이지의 주요 내용을 번역해주세요."

### 예시 코드
```python
# 웹페이지를 MCP Resource로 로드하는 예시
import requests

response = requests.get("https://example.com/article")
web_resource = MCPResource(
    type="web_content",
    content=response.text,
    mime_type="text/html",
    metadata={"url": "https://example.com/article"}
)
```
