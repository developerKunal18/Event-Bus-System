🧠 Why This Is Important

Instead of services directly calling each other:
Order Service
      ↓
Payment Service
      ↓
Notification Service

Using an Event Bus:
Order Service
      ↓
   Event Bus
   ↙      ↘
Payment   Notification
Service    Service

Benefits:
	•	✅ Loose coupling
	•	✅ Scalability
	•	✅ Fault tolerance
	•	✅ Asynchronous communication

⸻

Used By
	•	Kafka
	•	RabbitMQ
	•	AWS EventBridge
	•	Google Pub/Sub

⸻

🛠 Tech Stack
	•	Python
	•	Flask
	•	queue
	•	threading

⸻

📂 Project Structure
event-bus-system/
│
├── app.py
└── README.md
