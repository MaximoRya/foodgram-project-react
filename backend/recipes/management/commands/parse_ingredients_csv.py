import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient
from recipes.serializers import IngredientSerializer

PATH = "/data"


class Command(BaseCommand):
    help = "import data from ingredients.csv"

    def handle(self, *args, **kwargs):
        with open(f"{PATH}/ingredients.csv", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            ingredients_to_add = [
                Ingredient(
                    name=row[0],
                    measurement_unit=row[1],
                )
                for row in reader
            ]
            Ingredient.objects.bulk_create(ingredients_to_add)

class IngredientViewSet(viewsets.ModelViewSet):
    help = "Сериализатор вывода ингредиентов."
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IngredientFilter
    pagination_class = None
