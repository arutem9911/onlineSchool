from django.db import models


class UserGroup(models.Model):
    user = models.ForeignKey(
        'accounts.User', related_name='user_groups',
        on_delete=models.CASCADE, verbose_name='User')
    group = models.ForeignKey(
        'accounts.StudyGroup', related_name='group_users',
        on_delete=models.CASCADE, verbose_name='Group')

    def __str__(self):
        return '{} | {}'.format(self.user, self.group)
