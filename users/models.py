from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
	BaseUserManager, PermissionsMixin
from summiterhub import settings_core
import uuid
from utils import choices


def upload_path(instance, filename):
	ext = filename.split('.')[-1]
	return '/'.join([
		'profile_image',
		str(instance.id)+str('.')+str(ext)
	])


class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Email is must')

		user = self.model(email=self.normalize_email(email))
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, password):
		user = self.create_user(email, password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)

		return user


class User(AbstractBaseUser, PermissionsMixin):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email = models.EmailField(unique=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'

	def __str__(self):
		return self.email


class UserDetail(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	user_id = models.OneToOneField(
		settings_core.AUTH_USER_MODEL,
		related_name='user_detail_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	profile_name = models.CharField(max_length=100)
	profile_image = models.ImageField(blank=True, null=True, upload_to=upload_path)
	name = models.CharField(max_length=100)
	postal_code = models.CharField(max_length=8)
	prefecture = models.IntegerField(choices=choices.PREFECTURE)
	address = models.CharField(max_length=200)
	gender_type = models.IntegerField(choices=choices.GENDER_TYPE)
	blood_type = models.IntegerField(choices=choices.BLOOD_TYPE)
	home_phone_number = models.CharField(max_length=13, blank=True, null=True)
	cell_phone_number = models.CharField(max_length=13, blank=True, null=True)
	emergency_contact_name = models.CharField(max_length=100)
	emergency_contact_phone = models.CharField(max_length=13)
	emergency_contact_email = models.CharField(max_length=100, blank=True, null=True)
	insurance_name = models.CharField(max_length=100, blank=True, null=True)
	insurance_number = models.CharField(max_length=100, blank=True, null=True)
	hitococo_id = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.profile_name


class Friend(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='friend_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	approval_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='friend_approval_user_id',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return str(self.user_id) + ' & ' + str(self.approval_user_id)


class FriendRequest(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	src_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='friend_request_src_user_id',
		on_delete=models.CASCADE
	)
	dest_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='friend_request_dest_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	message = models.TextField()
	is_approved = models.BooleanField(default=False)

	class Meta:
		unique_together = (('src_user_id', 'dest_user_id'),)

	def __str__(self):
		return str(self.src_user_id) + ' -> ' + str(self.dest_user_id)


class BlockingFriend(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	src_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='blocking_friend_src_user_id',
		on_delete=models.CASCADE
	)
	dest_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='blocking_friend_dest_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		unique_together = (('src_user_id', 'dest_user_id'),)

	def __str__(self):
		return str(self.src_user_id) + ' -> ' + str(self.dest_user_id)


class Party(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='party_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	name = models.CharField(max_length=50)
	remarks = models.CharField(max_length=100, blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Parties'

	def __str__(self):
		return self.name


class PartyMember(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='party_member_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	party_id = models.ForeignKey(
		Party,
		related_name='party_member_party_id',
		on_delete=models.CASCADE
	)
	entry_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='party_member_entry_user_id',
		on_delete=models.CASCADE
	)
	sort_index = models.IntegerField()

	def __str__(self):
		return str(self.entry_user_id) + '(' + str(self.party_id) + ')'
