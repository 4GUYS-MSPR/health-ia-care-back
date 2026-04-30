from app.models import Client

def create_client(user, **kwargs):
    """
        Just a function to create a fake client
    """
    return Client.objects.create(
        user=user
    )
