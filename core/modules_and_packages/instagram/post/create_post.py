def create_post():
    """Create a post with a title, body, and tags."""
    title = input("Enter a title: ")
    body = input("Enter a body: ")
    tags = input("Enter tags: ").split(",")
    return {"title": title, "body": body, "tags": tags}