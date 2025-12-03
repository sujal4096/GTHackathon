def test_generate_response():
    from app.services.agent import generate_response

    # Test case 1: Basic response generation
    data = {
        'user_id': 'test_user',
        'message': 'Hello, how can I help you?',
        'lat': '40.7128',
        'lng': '-74.0060'
    }
    response = generate_response(data)
    assert 'response' in response
    assert response['response'] == "This is a response from the LLM."

    # Test case 2: Check for missing user_id
    data = {
        'message': 'What is the weather like?',
        'lat': '40.7128',
        'lng': '-74.0060'
    }
    response = generate_response(data)
    assert 'response' in response
    assert response['response'] == "This is a response from the LLM."

    # Test case 3: Check for missing message
    data = {
        'user_id': 'test_user',
        'lat': '40.7128',
        'lng': '-74.0060'
    }
    response = generate_response(data)
    assert 'response' in response
    assert response['response'] == "This is a response from the LLM."