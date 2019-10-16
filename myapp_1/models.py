from django.db import models

class EmUser(models.Model):
    E_mail = models.CharField(max_length=100, unique=True, null=False )
    Password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.E_mail



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




class GnGroupType(models.Model):
    group_type = models.CharField(max_length=10, unique=True, null=False)

    def __str__(self):
        return self.group_type


class EmGroup(models.Model):
    group_name = models.CharField(max_length=100, unique=True, null=False)
    group_type_id = models.ForeignKey(GnGroupType, on_delete=models.CASCADE)
    create_date = models.DateTimeField(null=False)
    is_active = models.FileField(null=False)

    def __str__(self):
        return self.group_name





class EmUserGroup(models.Model):
    user_id = models.ForeignKey(EmUser, on_delete=models.CASCADE)
    group_id = models.ForeignKey(EmGroup, on_delete=models.CASCADE)
    create_date = models.DateTimeField(null=False)
    is_active = models.FileField(null=False)

    def __str__(self):
        return self.user_id




class EmCategory(models.Model):
    category_name = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self):
        return self.category_name

class EmEmail(models.Model):
    user_id = models.ForeignKey(EmUser, on_delete=models.CASCADE,null=False)
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    attachment_id = models.CharField(max_length=255)
    create_date = models.DateTimeField(null=False)
    is_active = models.BooleanField(null=False)
    parent_email_id = models.IntegerField()


    def __str__(self):
        return self.user_id


class EmReceiver(models.Model):
    user_id = models.ForeignKey(ScUser, on_delete=models.CASCADE,null=False)
    user_group_id = models.ForeignKey(EmUserGroup, on_delete=models.CASCADE)
    email_id = models.ForeignKey(EmEmail, on_delete=models.CASCADE)
    is_read = models.FileField()
    is_starred = models.FileField()
    is_active = models.FileField()

    def __str__(self):
        return self.user_id
























