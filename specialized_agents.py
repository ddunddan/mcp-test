from agent import Agent, Message
import pandas as pd
import numpy as np
from typing import Dict, Any

class DataCollectorAgent(Agent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "데이터 수집")
        self.data_sources = {
            "sales_data": "sales_database",
            "customer_data": "customer_database"
        }

    def handle_task_request(self, message: Message) -> None:
        """데이터 수집 작업 처리"""
        if message.content["task"] == "데이터 수집":
            dataset = message.content["parameters"]["dataset"]
            
            # 실제로는 데이터베이스에서 데이터를 가져오는 로직이 들어갈 부분
            collected_data = self.collect_data(dataset)
            
            response = self.create_message(
                receiver=message.sender,
                message_type="task_response",
                content={
                    "status": "completed",
                    "task_id": message.content["task_id"],
                    "data": collected_data,
                    "message": f"{dataset} 데이터 수집 완료"
                }
            )
            self.send_message(response)

    def collect_data(self, dataset: str) -> Dict[str, Any]:
        """데이터 수집 시뮬레이션"""
        return {
            "source": self.data_sources.get(dataset, "unknown"),
            "timestamp": self.create_message("", "", {}).timestamp,
            "sample_data": {
                "values": [100, 200, 300, 400, 500],
                "labels": ["A", "B", "C", "D", "E"]
            }
        }

class DataAnalyzerAgent(Agent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "데이터 분석")
        self.analysis_methods = {
            "trend": self.analyze_trend,
            "clustering": self.analyze_clustering
        }

    def handle_task_request(self, message: Message) -> None:
        """데이터 분석 작업 처리"""
        if message.content["task"] == "데이터 분석 수행":
            analysis_type = message.content["parameters"]["analysis_type"]
            
            if analysis_type in self.analysis_methods:
                analysis_result = self.analysis_methods[analysis_type](message.content["parameters"])
                
                response = self.create_message(
                    receiver=message.sender,
                    message_type="task_response",
                    content={
                        "status": "completed",
                        "task_id": message.content["task_id"],
                        "result": analysis_result,
                        "message": f"{analysis_type} 분석 완료"
                    }
                )
                self.send_message(response)
            else:
                self.send_error_response(message, f"지원하지 않는 분석 유형: {analysis_type}")

    def analyze_trend(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """트렌드 분석 시뮬레이션"""
        return {
            "trend_type": "increasing",
            "confidence": 0.85,
            "summary": "지속적인 상승 트렌드 감지"
        }

    def analyze_clustering(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """클러스터링 분석 시뮬레이션"""
        return {
            "clusters": 3,
            "silhouette_score": 0.75,
            "cluster_sizes": [100, 150, 200]
        }

    def send_error_response(self, original_message: Message, error_message: str) -> None:
        """에러 응답 전송"""
        response = self.create_message(
            receiver=original_message.sender,
            message_type="task_response",
            content={
                "status": "error",
                "task_id": original_message.content["task_id"],
                "message": error_message
            }
        )
        self.send_message(response)

# 사용 예시
if __name__ == "__main__":
    # 특화된 에이전트 생성
    collector = DataCollectorAgent("collector1")
    analyzer = DataAnalyzerAgent("analyzer1")

    # 데이터 수집 요청
    collection_request = collector.create_message(
        receiver="collector1",
        message_type="task_request",
        content={
            "task_id": "collect_001",
            "task": "데이터 수집",
            "parameters": {
                "dataset": "sales_data"
            }
        }
    )
    collector.receive_message(collection_request)

    # 데이터 분석 요청
    analysis_request = analyzer.create_message(
        receiver="analyzer1",
        message_type="task_request",
        content={
            "task_id": "analyze_001",
            "task": "데이터 분석 수행",
            "parameters": {
                "analysis_type": "trend",
                "dataset": "sales_data"
            }
        }
    )
    analyzer.receive_message(analysis_request) 