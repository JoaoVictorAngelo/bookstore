from django.test import TestCase

from product.factories import ProductFactory, CategoryFactory
from product.serializers import ProductSerializer


class TestProductSerializer(TestCase):
    def setUp(self):
        self.category_1 = CategoryFactory()
        self.category_2 = CategoryFactory()
        self.product = ProductFactory(category=[self.category_1, self.category_2])
        self.serializer = ProductSerializer(self.product)

    def test_product_serializer_output(self):
        data = self.serializer.data

        assert data["title"] == self.product.title
        assert data["price"] == self.product.price
        assert data["active"] == self.product.active
        assert isinstance(data["category"], list)
        assert len(data["category"]) == 2
        assert data["category"][0]["title"] == self.category_1.title
        assert data["category"][1]["title"] == self.category_2.title
