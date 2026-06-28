from django.db import models


class Category(models.Model):
    """
    E.g. : Hill Station, Beach, Religious, Adventure
    """

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)        # use in url

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class TourPackage(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy',   'Easy'),
        ('medium', 'Moderate'),
        ('hard',   'Challenging'),
    ]


    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True)         # SEO-friendly URL
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    highlights  = models.TextField(help_text="One highlight per line")
    itinerary   = models.TextField(help_text="Day-wise plan")

    # Pricing
    price_per_person = models.DecimalField(max_digits=8, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    # Details
    duration_days    = models.PositiveIntegerField()
    max_group_size   = models.PositiveIntegerField(default=20)
    difficulty       = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    destination      = models.CharField(max_length=200)


    # Media
    cover_image      = models.ImageField(upload_to='tours/covers/')

    # Metadata
    is_featured      = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    @property
    def final_price(self):
        """Returns discounted price if available, else regular price."""
        return self.discounted_price if self.discounted_price else self.price_per_person

    @property
    def discount_percentage(self):
        if self.discounted_price:
            return int(((self.price_per_person - self.discounted_price) / self.price_per_person) * 100)
        return 0

    class Meta:
        ordering = ['-created_at']


