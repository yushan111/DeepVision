import redis
import json
import threading
import time
from ONA.DockerInteractor import DockerInteractor

class CognitiveSynergyAgent:
    def __init__(self, agent_type, config):
        self.agent_type = agent_type
        self.config = config
        self.is_running = False
        self._thread = None
        self.ona = DockerInteractor(['docker', 'exec', '-i', 'ONA', '/app/NAR', 'shell'])

        # Set up Redis client
        #self.redis_client = redis.Redis(host='localhost', port=6379, db=0)

    def _run(self):
        iterations = 0
        print(f"Agent of type {self.agent_type} is starting...")

        while self.is_running:
            # Process data and publish results to Redis
            data = {}  # Your data here
            #self.redis_client.publish('channel_name', json.dumps(data))
            iterations = iterations + 1
            print(f"Agent of type {self.agent_type} is running...iteration {iterations}")
            response = self.ona.execute_command("<cat --> furry_animal>.\n<cat --> furry_animal>?\n0\n", "done with 0 additional inference steps")
            print(f"Response: {response}")
            time.sleep(1)

        print(f"Agent of type {self.agent_type} has stopped.")

    def start(self):
        # Start the agent
        self.is_running = True
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    def stop(self):
        # Stop the agent
        self.is_running = False
        if self._thread is not None:
            self._thread.join()