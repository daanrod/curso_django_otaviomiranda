from unittest.mock import patch

from recipes.tests.test_recipe_base import RecipeTestBase


class MakePaginationTest(RecipeTestBase):

    @patch('recipes.views.PER_PAGE', new=9)
    def test_current_page(self):
        for i in range(18):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)
