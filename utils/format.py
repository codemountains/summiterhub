from rest_framework import serializers


def created_at():
	fmt_created_at = serializers.DateTimeField(
		format="%Y-%m-%d %H:%M",
		read_only=True
	)
	return fmt_created_at


def updated_at():
	fmt_updated_at = serializers.DateTimeField(
		format="%Y-%m-%d %H:%M",
		read_only=True
	)
	return fmt_updated_at


def expiration_at():
	fmt_expiration_at = serializers.DateTimeField(
		format="%Y-%m-%d %H:%M",
		read_only=True
	)
	return fmt_expiration_at
