from django.db import models

class GnGroupType(models.Model):
    group_type = models.CharField(max_length=10, unique=True, null=False)

    def __str__(self):
        return self.group_type

class ScUser(models.Model):
    user_code = models.CharField(max_length=10, unique=True)
    user_name = models.CharField(max_length=100, null=False)
    user_node = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100,null=True )
    password = models.CharField(max_length=255,null=True)
    voice = models.FileField(null=True)
    face = models.FileField(null=True)
    salt = models.IntegerField()
    pin =  models.CharField(max_length=255)

    def __str__(self):
        return self.user_code

class User(models.Model):
    user_code = models.CharField(max_length=10, unique=True)
    user_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=255, null=True)
    voice = models.BooleanField( null=True)
    face = models.BooleanField( null=True)
    salt = models.IntegerField()
    pin = models.CharField(max_length=255)

    def __str__(self):
        return self.user_code


class EsUser(models.Model):
    email = models.CharField(max_length=100)
    sns_user_id =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class ChGroup(models.Model):
    group_name = models.CharField(max_length=100, unique=True,null=False)
    group_type_id = models.ForeignKey(GnGroupType, on_delete=models.CASCADE)
    user_id = models.ForeignKey(EsUser, on_delete=models.CASCADE)
    create_date = models.DateTimeField(null=False)
    is_active = models.BooleanField(null=False)

    def __str__(self):
        return self.group_name





class ChUserGroup(models.Model):
    user = models.ForeignKey(ScUser, on_delete=models.CASCADE,null=False, related_name='usergroup')
    group = models.ForeignKey(ChGroup, on_delete=models.CASCADE,null=False)
    add_date = models.DateTimeField(null=False)
    add_by = models.ForeignKey(ScUser, on_delete=models.CASCADE,null=False)
    is_active = models.BooleanField(null=False)

    def __str__(self):
        return self.user_id

class ChConversation(models.Model):
    conversation_name = models.CharField(max_length=100)
    user_id = models.ForeignKey(ScUser, on_delete=models.CASCADE, null=False)
    create_date = models.DateTimeField(null=False)
    is_active = models.BooleanField(null=False)

    def __str__(self):
        return self.conversation_name

class ChMessage(models.Model):
    user_id = models.ForeignKey(ScUser, on_delete=models.CASCADE, null=False)
    body = models.CharField(max_length=100)
    attachment_url = models.CharField(max_length=255)
    send_time = models.DateTimeField(null=False)

    def __str__(self):
        return self.user_id


class ChReceiver(models.Model):
    user_id = models.ForeignKey(ScUser, on_delete=models.CASCADE, null=False)
    user_group_id = models.ForeignKey(ChGroup, on_delete=models.CASCADE)
    message_id = models.ForeignKey(ChMessage, on_delete=models.CASCADE)
    conversation_id =  models.ForeignKey(ChConversation, on_delete=models.CASCADE)
    seen_date =  models.DateTimeField()

    def __str__(self):
        return self.user_id


