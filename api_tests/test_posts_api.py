import requests


class TestPostsAPI:
    """API tests for the /posts endpoints on JSONPlaceholder."""
    
    def test_get_all_posts_returns_200(self, base_url):
        response = requests.get(f"{base_url}/posts")
        assert response.status_code == 200
        assert len(response.json()) > 0
    
    def test_create_post_returns_201(self, base_url, headers):
        new_post = {
            "title": "Test post for QA",
            "body": "This is a test post created during API automation testing",
            "userId": 1,
        }
        response = requests.post(f"{base_url}/posts", json=new_post, headers=headers)
        
        assert response.status_code == 201, "POST should return 201 Created"
        created = response.json()
        
        # JSONPlaceholder echoes back what we sent + assigns an id
        assert created["title"] == new_post["title"]
        assert created["body"] == new_post["body"]
        assert "id" in created, "Created post should have an id"
    
    def test_update_post_returns_200(self, base_url, headers):
        updated_post = {
            "id": 1,
            "title": "Updated title",
            "body": "Updated body",
            "userId": 1,
        }
        response = requests.put(f"{base_url}/posts/1", json=updated_post, headers=headers)
        
        assert response.status_code == 200
        result = response.json()
        assert result["title"] == "Updated title"
    
    def test_delete_post_returns_200(self, base_url):
        response = requests.delete(f"{base_url}/posts/1")
        assert response.status_code == 200
    
    def test_filter_posts_by_user(self, base_url):
        # query parameter to filter posts by userId
        response = requests.get(f"{base_url}/posts", params={"userId": 1})
        
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) > 0
        
        # every returned post should belong to user 1
        for post in posts:
            assert post["userId"] == 1, f"Found post with wrong userId: {post['userId']}"