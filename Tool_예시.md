# Tool 예시 모음

## 코드 실행 Tool

코드 실행 Tool은 AI 모델이 다양한 프로그래밍 언어의 코드를 실행하고 결과를 확인할 수 있게 합니다.

### 활용 사례
- **코드 테스트**: "이 Python 코드를 실행하고 결과를 보여주세요."
- **알고리즘 검증**: "이 정렬 알고리즘의 효율성을 테스트해주세요."
- **데이터 처리**: "이 CSV 파일을 파싱하고 통계를 계산해주세요."

### 예시 코드
```python
# 코드 실행 Tool 사용 예시
python_code = """
import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 결과 계산
mean_value = np.mean(y)
max_value = np.max(y)

print(f"Mean value: {mean_value}")
print(f"Max value: {max_value}")
"""

result = code_execution_tool.execute(
    code=python_code,
    language="python"
)
```

## 검색 Tool

검색 Tool은 AI 모델이 인터넷이나 특정 데이터베이스에서 정보를 검색할 수 있게 합니다.

### 활용 사례
- **최신 정보 검색**: "최근 인공지능 분야의 주요 연구 동향을 찾아주세요."
- **사실 확인**: "이 통계 데이터의 출처를 찾아 검증해주세요."
- **관련 정보 수집**: "이 제품에 대한 사용자 리뷰를 모아주세요."

### 예시 코드
```python
# 검색 Tool 사용 예시
search_results = search_tool.search(
    query="최신 딥러닝 모델 성능 비교",
    num_results=5,
    search_type="web"
)
```

## 계산기 Tool

계산기 Tool은 AI 모델이 수학적 계산을 정확하게 수행할 수 있게 합니다.

### 활용 사례
- **수학 문제 해결**: "이 미분방정식의 해를 구해주세요."
- **통계 분석**: "이 데이터셋의 표준편차와 신뢰구간을 계산해주세요."
- **재무 계산**: "이 투자의 5년 복리 수익률을 계산해주세요."

### 예시 코드
```python
# 계산기 Tool 사용 예시
import sympy as sp

x = sp.Symbol('x')
expression = x**2 + 2*x + 1

result = calculator_tool.evaluate(
    expression=expression,
    operation="solve",
    variable=x
)
```

## 파일 시스템 Tool

파일 시스템 Tool은 AI 모델이 파일을 읽고 쓰고 관리할 수 있게 합니다.

### 활용 사례
- **파일 내용 분석**: "이 로그 파일에서 오류 패턴을 찾아주세요."
- **문서 생성**: "분석 결과를 보고서 형태로 저장해주세요."
- **데이터 통합**: "여러 파일의 데이터를 하나로 통합해주세요."

### 예시 코드
```python
# 파일 시스템 Tool 사용 예시
file_content = file_system_tool.read_file(
    path="/path/to/data.csv",
    encoding="utf-8"
)

processed_content = process_data(file_content)

file_system_tool.write_file(
    path="/path/to/results.txt",
    content=processed_content
)
```

## API 호출 Tool

API 호출 Tool은 AI 모델이 외부 서비스와 통신할 수 있게 합니다.

### 활용 사례
- **외부 서비스 활용**: "이 주소의 위치 정보를 지도 API로 조회해주세요."
- **데이터 수집**: "이 제품의 현재 가격을 쇼핑 API에서 조회해주세요."
- **서비스 연동**: "이 메시지를 Slack에 전송해주세요."

### 예시 코드
```python
# API 호출 Tool 사용 예시
response = api_tool.call(
    method="GET",
    url="https://api.weather.com/forecast",
    params={"location": "Seoul", "days": 5},
    headers={"Authorization": "Bearer token123"}
)
```
