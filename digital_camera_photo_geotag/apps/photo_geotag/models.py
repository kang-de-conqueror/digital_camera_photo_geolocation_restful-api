from djongo import models
import uuid


# Create your models here.
class Route(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    route_data = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.TextField(null=True)

    def __str__(self):
        return str(self.id)
