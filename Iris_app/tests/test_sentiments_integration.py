def test_sentiment_api_positive(test_client):
    input_text = "I love programming"
    response = test_client.post("/sentiment/predict", json={"text": input_text})
    assert response.status_code == 200
    result = response.json()
    assert result['sentiment'] == 'POSITIVE', f"Expected 'POSITIVE', got {result['sentiment']}"


def test_sentiment_api_negative(test_client):
    input_text = "I dont love programming"
    response = test_client.post("/sentiment/predict", json={"text": input_text})
    assert response.status_code == 200
    result = response.json()
    assert result['sentiment'] == 'NEGATIVE', f"Expected 'NEGATIVE', got {result['sentiment']}"