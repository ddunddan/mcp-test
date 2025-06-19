import uuid
from datetime import datetime
from typing import Dict, Any, Optional
from dataclasses import dataclass
import json

@dataclass
class Message:
    message_id: str
    sender: str
    receiver: str
    message_type: str
    content: Dict[str, Any]
    timestamp: str

class Agent:
    def __init__(self, agent_id: str, specialization: str):
        self.agent_id = agent_id
        self.specialization = specialization
        self.status = "active"
        self.current_task = None
        self.message_queue = []

    def create_message(self, receiver: str, message_type: str, content: Dict[str, Any]) -> Message:
        """메시지 생성"""
        return Message(
            message_id=str(uuid.uuid4()),
            sender=self.agent_id,
            receiver=receiver,
            message_type=message_type,
            content=content,
            timestamp=datetime.utcnow().isoformat()
        )

    def send_message(self, message: Message) -> None:
        """메시지 전송 (예시용 구현)"""
        print(f"메시지 전송: {self.agent_id} -> {message.receiver}")
        print(json.dumps(message.__dict__, indent=2, ensure_ascii=False))

    def receive_message(self, message: Message) -> None:
        """메시지 수신"""
        self.message_queue.append(message)
        self.process_message(message)

    def process_message(self, message: Message) -> None:
        """메시지 처리"""
        if message.message_type == "task_request":
            self.handle_task_request(message)
        elif message.message_type == "task_response":
            self.handle_task_response(message)

    def handle_task_request(self, message: Message) -> None:
        """작업 요청 처리"""
        if self.status == "active" and self.current_task is None:
            self.current_task = message.content["task"]
            response = self.create_message(
                receiver=message.sender,
                message_type="task_response",
                content={
                    "status": "accepted",
                    "task_id": message.content.get("task_id"),
                    "message": f"작업 '{self.current_task}' 수락됨"
                }
            )
            self.send_message(response)
        else:
            response = self.create_message(
                receiver=message.sender,
                message_type="task_response",
                content={
                    "status": "rejected",
                    "task_id": message.content.get("task_id"),
                    "message": "현재 작업을 처리할 수 없음"
                }
            )
            self.send_message(response)

    def handle_task_response(self, message: Message) -> None:
        """작업 응답 처리"""
        print(f"작업 응답 수신: {message.content['message']}")

# 사용 예시
if __name__ == "__main__":
    # 에이전트 생성
    agent1 = Agent("agent1", "데이터 수집")
    agent2 = Agent("agent2", "데이터 분석")

    # 작업 요청 메시지 생성
    task_request = agent1.create_message(
        receiver="agent2",
        message_type="task_request",
        content={
            "task_id": "task_001",
            "task": "데이터 분석 수행",
            "priority": "high",
            "parameters": {
                "dataset": "sales_data",
                "analysis_type": "trend"
            }
        }
    )

    # 메시지 전송 및 처리
    agent2.receive_message(task_request) 