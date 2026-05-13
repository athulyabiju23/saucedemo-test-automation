import requests


class TestUsersAPI:
    """API tests for the /users endpoints on JSONPlaceholder."""
    
    def test_get_all_users_returns_200(self, base_url):
        response = requests.get(f"{base_url}/users")
        assert response.status_code == 200
    
    def test_get_all_users_returns_list(self, base_url):
        response = requests.get(f"{base_url}/users")
        data = response.json()
        assert isinstance(data, list), "Response should be a list"
        assert len(data) > 0, "Users list should not be empty"
    
    def test_get_single_user_returns_correct_structure(self, base_url):
        response = requests.get(f"{base_url}/users/1")
        
        assert response.status_code == 200
        user = response.json()
        
        # validate schema — these fields must exist
        required_fields = ["id", "name", "username", "email", "phone", "website"]
        for field in required_fields:
            assert field in user, f"Missing required field: {field}"
        
        # validate types
        assert isinstance(user["id"], int)
        assert isinstance(user["email"], str)
        assert "@" in user["email"], "Email should contain @"
    
    def test_get_nonexistent_user_returns_404(self, base_url):
        response = requests.get(f"{base_url}/users/9999")
        assert response.status_code == 404, "Nonexistent user should return 404"
    
    def test_response_time_under_2_seconds(self, base_url):
        response = requests.get(f"{base_url}/users")
        # response.elapsed is the time the server took to respond
        assert response.elapsed.total_seconds() < 2, \
            f"Response too slow: {response.elapsed.total_seconds()}s"