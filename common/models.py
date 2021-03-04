from django.db import models
from django.utils.translation import gettext_lazy as _


class Sequence(models.Model):
    """ Sequence model """
    scope = models.CharField(verbose_name=_('scope'), max_length=40)
    crt_value = models.IntegerField(verbose_name=_('crt_value'), default=0)

    class Meta:
        db_table = 'sequence'
        verbose_name = _('sequence')
        verbose_name_plural = _('sequence')

    def __str__(self):
        return self.scope


class Seo(models.Model):
    """ SEO abstract model """
    seo_title = models.CharField(verbose_name=_('title'), blank=True, max_length=100)
    seo_description = models.CharField(verbose_name=_('description'), blank=True, max_length=250)
    seo_keywords = models.CharField(verbose_name=_('keywords'), blank=True, max_length=250)

    def get_seo_title(self):
        """ Function for return seo title """
        return self.seo_title if self.seo_title else ''

    def get_seo_description(self):
        """ Function for return seo description """
        return self.seo_description if self.seo_description else ''

    def get_seo_keywords(self):
        """ Function for return seo description """
        return self.seo_keywords if self.seo_keywords else ''

    class Meta:
        abstract = True


class Category(Seo):
    """ Categories for products """
    sequence_scope = 'C'
    name = models.CharField(verbose_name=_('name'), max_length=100, unique=True, db_index=True)
    code_name = models.CharField(verbose_name=_('code'), max_length=100, unique=True, db_index=True)
    category_id = models.CharField(verbose_name=_('category_id'), db_index=True, max_length=20)
    description = models.TextField(verbose_name=_('description'), blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=_('date created'), auto_now_add=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='category/')

    class Meta:
        db_table = 'categories'
        ordering = ['created_at']
        verbose_name = _('category')
        verbose_name_plural = _('category')

    def __str__(self):
        return f"{self.category_id} - {self.code_name}"

    def save(self, *args, **kwargs):
        if not self.category_id:
            from common.tools.app_tools import next_val
            self.category_id = f"{str(next_val(self.sequence_scope))}"
        super(Category, self).save(*args, **kwargs)


class Product(Seo):
    """ Product model """
    sequence_scope = 'P'
    name = models.CharField(verbose_name=_('name'), max_length=255)
    code = models.CharField(verbose_name=_('code'), max_length=255, unique=True, db_index=True)
    product_id = models.CharField(verbose_name=_('product_id'), max_length=55, unique=True, db_index=True)
    is_available = models.BooleanField(verbose_name=_('is_available'), default=True)
    price = models.DecimalField(verbose_name=_('price'), max_digits=15, decimal_places=2)
    old_price = models.DecimalField(verbose_name=_('old_price'), max_digits=15, decimal_places=2)
    quantity = models.IntegerField(verbose_name=_('quantity'), default=0)
    description = models.TextField(verbose_name=_('description'))
    created_at = models.DateTimeField(verbose_name=_('created_at'), auto_now_add=True)
    category_id = models.ForeignKey(verbose_name=_('category_id'), to=Category, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_('image'), upload_to='products/')

    class Meta:
        db_table = 'product'
        ordering = ['created_at']
        verbose_name = _('product')
        verbose_name_plural = _('product')

    def __str__(self):
        return f"{self.name} - {self.code}"

    def save(self, *args, **kwargs):
        if not self.product_id:
            from common.tools.app_tools import next_val
            self.product_id = f"{str(next_val(self.sequence_scope))}"
        super(Product, self).save(*args, **kwargs)
