from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete


from products.models import Product
# Create your models here.


class CartItem(models.Model):
	cart = models.ForeignKey("Cart", null=True, on_delete=models.CASCADE)
	item = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1, null=True)
	line_item_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	def __str__(self):
		return self.item.title

	def remove(self):
		return self.item.remove_from_cart()


def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
	qty = instance.quantity
	if qty >= 1:
		price = instance.item.price
		line_item_total = Decimal(qty) * Decimal(price)
		instance.line_item_total = line_item_total

pre_save.connect(cart_item_pre_save_receiver, sender=CartItem)



def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
	instance.cart.update_total()

post_save.connect(cart_item_post_save_receiver, sender=CartItem)

post_delete.connect(cart_item_post_save_receiver, sender=CartItem)


class Cart(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=True, on_delete=models.CASCADE)
	items = models.ManyToManyField(Product, through=CartItem)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
	active = models.BooleanField(default=True)
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)

	def update_total(self):
		print("updating...")
		total = 0
		items = self.cartitem_set.all()
		for item in items:
			total += item.line_item_total
		self.total = "%.2f" %(total)
		self.save()

	def is_complete(self):
		self.active = False
		self.save()









