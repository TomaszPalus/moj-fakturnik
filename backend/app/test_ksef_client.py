from app.services.ksef_client import (
    test_connection
)

result = test_connection(
    token="TEST_TOKEN"
)

print(result)